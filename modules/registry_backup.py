import os
import subprocess
import json
import winreg
from datetime import datetime
from typing import Dict, Any, List, Optional

class RegistryBackup:

    def __init__(self):
        self.backup_dir = os.path.join(os.path.expanduser("~"), "Documents", "PC_Optimizer_Backups")
        self.ensure_backup_dir()

        self.monitored_keys = [

            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\GameBar"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR"),

            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"),

            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"),
            (winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop"),

            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl"),
        ]

    def ensure_backup_dir(self):

        try:
            os.makedirs(self.backup_dir, exist_ok=True)
        except Exception as e:
            print(f"Error creating backup directory: {e}")

    def create_backup(self) -> str:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"registry_backup_{timestamp}.json"
        backup_path = os.path.join(self.backup_dir, backup_filename)

        backup_data = {
            'timestamp': timestamp,
            'version': '1.0',
            'keys': {}
        }

        try:
            for hkey, key_path in self.monitored_keys:
                try:
                    key_data = self._backup_registry_key(hkey, key_path)
                    if key_data:
                        backup_data['keys'][f"{hkey}\\{key_path}"] = key_data
                except Exception as e:
                    print(f"Error backing up key {key_path}: {e}")

            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2, ensure_ascii=False)

            self._create_system_backup(timestamp)

            return backup_path

        except Exception as e:
            print(f"Error creating backup: {e}")
            raise

    def _backup_registry_key(self, hkey: int, key_path: str) -> Optional[Dict[str, Any]]:

        try:
            with winreg.OpenKey(hkey, key_path) as key:
                key_data = {
                    'values': {},
                    'subkeys': {}
                }

                try:
                    i = 0
                    while True:
                        try:
                            value_name, value_data, value_type = winreg.EnumValue(key, i)
                            key_data['values'][value_name] = {
                                'data': self._serialize_registry_value(value_data, value_type),
                                'type': value_type
                            }
                            i += 1
                        except WindowsError:
                            break
                except Exception as e:
                    print(f"Error backing up values for {key_path}: {e}")

                try:
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey_path = f"{key_path}\\{subkey_name}"
                            subkey_data = self._backup_registry_key(hkey, subkey_path)
                            if subkey_data:
                                key_data['subkeys'][subkey_name] = subkey_data
                            i += 1
                        except WindowsError:
                            break
                except Exception as e:
                    print(f"Error backing up subkeys for {key_path}: {e}")

                return key_data

        except FileNotFoundError:

            return None
        except Exception as e:
            print(f"Error accessing key {key_path}: {e}")
            return None

    def _serialize_registry_value(self, value_data: Any, value_type: int) -> Any:

        if value_type == winreg.REG_BINARY:

            if isinstance(value_data, bytes):
                return value_data.hex()
            return str(value_data)
        elif value_type in [winreg.REG_DWORD, winreg.REG_QWORD]:
            return int(value_data)
        elif value_type in [winreg.REG_SZ, winreg.REG_EXPAND_SZ]:
            return str(value_data)
        elif value_type == winreg.REG_MULTI_SZ:
            return list(value_data)
        else:
            return str(value_data)

    def _create_system_backup(self, timestamp: str):

        try:
            backup_file = os.path.join(self.backup_dir, f"system_backup_{timestamp}.reg")

            hives_to_backup = [
                ("HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\GameBar", "gamemode"),
                ("HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "gpu"),
                ("HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "gamedvr"),
            ]

            for hive_path, name in hives_to_backup:
                try:
                    reg_file = os.path.join(self.backup_dir, f"{name}_backup_{timestamp}.reg")
                    subprocess.run([
                        "regedit", "export", hive_path, reg_file, "/y"
                    ], capture_output=True, check=False)
                except Exception as e:
                    print(f"Error exporting {hive_path}: {e}")

        except Exception as e:
            print(f"Error creating system backup: {e}")

    def restore_backup(self, backup_path: Optional[str] = None) -> bool:

        try:
            if backup_path is None:

                backup_path = self._get_latest_backup()
                if not backup_path:
                    return False

            if not os.path.exists(backup_path):
                print(f"Backup file not found: {backup_path}")
                return False

            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)

            for key_identifier, key_data in backup_data['keys'].items():
                try:

                    parts = key_identifier.split('\\', 1)
                    if len(parts) != 2:
                        continue

                    hkey = int(parts[0])
                    key_path = parts[1]

                    self._restore_registry_key(hkey, key_path, key_data)

                except Exception as e:
                    print(f"Error restoring key {key_identifier}: {e}")

            return True

        except Exception as e:
            print(f"Error restoring backup: {e}")
            return False

    def _restore_registry_key(self, hkey: int, key_path: str, key_data: Dict[str, Any]):

        try:

            with winreg.CreateKey(hkey, key_path) as key:

                for value_name, value_info in key_data.get('values', {}).items():
                    try:
                        value_data = self._deserialize_registry_value(
                            value_info['data'],
                            value_info['type']
                        )
                        winreg.SetValueEx(key, value_name, 0, value_info['type'], value_data)
                    except Exception as e:
                        print(f"Error restoring value {value_name}: {e}")

                for subkey_name, subkey_data in key_data.get('subkeys', {}).items():
                    try:
                        subkey_path = f"{key_path}\\{subkey_name}"
                        self._restore_registry_key(hkey, subkey_path, subkey_data)
                    except Exception as e:
                        print(f"Error restoring subkey {subkey_name}: {e}")

        except Exception as e:
            print(f"Error restoring key {key_path}: {e}")

    def _deserialize_registry_value(self, value_data: Any, value_type: int) -> Any:

        if value_type == winreg.REG_BINARY:

            if isinstance(value_data, str):
                return bytes.fromhex(value_data)
            return value_data
        elif value_type in [winreg.REG_DWORD, winreg.REG_QWORD]:
            return int(value_data)
        elif value_type in [winreg.REG_SZ, winreg.REG_EXPAND_SZ]:
            return str(value_data)
        elif value_type == winreg.REG_MULTI_SZ:
            return list(value_data)
        else:
            return value_data

    def _get_latest_backup(self) -> Optional[str]:

        try:
            backup_files = []
            for filename in os.listdir(self.backup_dir):
                if filename.startswith("registry_backup_") and filename.endswith(".json"):
                    backup_path = os.path.join(self.backup_dir, filename)
                    backup_files.append((os.path.getmtime(backup_path), backup_path))

            if backup_files:

                backup_files.sort(reverse=True)
                return backup_files[0][1]

        except Exception as e:
            print(f"Error finding latest backup: {e}")

        return None

    def list_backups(self) -> List[Dict[str, Any]]:

        backups = []

        try:
            for filename in os.listdir(self.backup_dir):
                if filename.startswith("registry_backup_") and filename.endswith(".json"):
                    backup_path = os.path.join(self.backup_dir, filename)

                    try:

                        stat = os.stat(backup_path)

                        with open(backup_path, 'r', encoding='utf-8') as f:
                            backup_data = json.load(f)

                        backups.append({
                            'filename': filename,
                            'path': backup_path,
                            'timestamp': backup_data.get('timestamp', 'Unknown'),
                            'size': stat.st_size,
                            'created': datetime.fromtimestamp(stat.st_ctime),
                            'modified': datetime.fromtimestamp(stat.st_mtime),
                            'key_count': len(backup_data.get('keys', {}))
                        })

                    except Exception as e:
                        print(f"Error reading backup {filename}: {e}")

        except Exception as e:
            print(f"Error listing backups: {e}")

        backups.sort(key=lambda x: x['created'], reverse=True)
        return backups

    def delete_backup(self, backup_path: str) -> bool:

        try:
            if os.path.exists(backup_path):
                os.remove(backup_path)

                backup_dir = os.path.dirname(backup_path)
                backup_name = os.path.basename(backup_path)
                timestamp = backup_name.replace("registry_backup_", "").replace(".json", "")

                for filename in os.listdir(backup_dir):
                    if timestamp in filename and filename.endswith(".reg"):
                        try:
                            os.remove(os.path.join(backup_dir, filename))
                        except Exception:
                            pass

                return True
        except Exception as e:
            print(f"Error deleting backup: {e}")

        return False

    def cleanup_old_backups(self, keep_count: int = 10):

        try:
            backups = self.list_backups()

            if len(backups) > keep_count:

                for backup in backups[keep_count:]:
                    self.delete_backup(backup['path'])

        except Exception as e:
            print(f"Error cleaning up backups: {e}")

    def export_backup_to_reg(self, backup_path: str, output_path: str) -> bool:

        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)

            reg_content = ["Windows Registry Editor Version 5.00", ""]

            for key_identifier, key_data in backup_data['keys'].items():

                parts = key_identifier.split('\\', 1)
                if len(parts) != 2:
                    continue

                hkey_num = int(parts[0])
                key_path = parts[1]

                hkey_names = {
                    winreg.HKEY_CURRENT_USER: "HKEY_CURRENT_USER",
                    winreg.HKEY_LOCAL_MACHINE: "HKEY_LOCAL_MACHINE",
                    winreg.HKEY_CLASSES_ROOT: "HKEY_CLASSES_ROOT",
                    winreg.HKEY_USERS: "HKEY_USERS",
                    winreg.HKEY_CURRENT_CONFIG: "HKEY_CURRENT_CONFIG"
                }

                hkey_name = hkey_names.get(hkey_num, f"HKEY_{hkey_num}")
                full_key_path = f"{hkey_name}\\{key_path}"

                reg_content.append(f"[{full_key_path}]")

                for value_name, value_info in key_data.get('values', {}).items():
                    value_line = self._format_reg_value(value_name, value_info)
                    if value_line:
                        reg_content.append(value_line)

                reg_content.append("")

            with open(output_path, 'w', encoding='utf-16le') as f:
                f.write('\n'.join(reg_content))

            return True

        except Exception as e:
            print(f"Error exporting to .reg format: {e}")
            return False

    def _format_reg_value(self, value_name: str, value_info: Dict[str, Any]) -> str:

        try:
            value_data = value_info['data']
            value_type = value_info['type']

            if value_name == "":
                name_part = "@"
            else:
                name_part = f'"{value_name}"'

            if value_type == winreg.REG_SZ:
                return f'{name_part}="{value_data}"'
            elif value_type == winreg.REG_DWORD:
                return f'{name_part}=dword:{value_data:08x}'
            elif value_type == winreg.REG_BINARY:
                hex_data = value_data if isinstance(value_data, str) else value_data.hex()
                return f'{name_part}=hex:{",".join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))}'
            else:

                return f'{name_part}=hex({value_type:x}):{value_data}'

        except Exception as e:
            print(f"Error formatting registry value: {e}")
            return ""
