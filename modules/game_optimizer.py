import winreg
import subprocess
import os
from typing import Dict, Any
from .utils import run_command_silent, run_powershell_silent

class GameOptimizer:

    def __init__(self):
        self.game_mode_key = r"SOFTWARE\Microsoft\GameBar"
        self.gpu_scheduling_key = r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers"
        self.xbox_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR"

    def toggle_game_mode(self, enable: bool) -> bool:

        try:

            run_command_silent([
                "reg", "add",
                f"HKCU\\{self.game_mode_key}",
                "/v", "AllowAutoGameMode",
                "/t", "REG_DWORD",
                "/d", "1" if enable else "0",
                "/f"
            ])

            result = run_command_silent([
                "reg", "add",
                f"HKCU\\{self.xbox_key}",
                "/v", "GameDVR_Enabled",
                "/t", "REG_DWORD",
                "/d", "1" if enable else "0",
                "/f"
            ])

            result = run_command_silent([
                "reg", "add",
                f"HKCU\\{self.xbox_key}",
                "/v", "GameDVR_FSEBehaviorMode",
                "/t", "REG_DWORD",
                "/d", "2" if enable else "0",
                "/f"
            ])

            return True
        except Exception as e:
            print(f"Error toggling Game Mode: {e}")
            return False

    def toggle_gpu_scheduling(self, enable: bool) -> bool:

        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.gpu_scheduling_key, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "HwSchMode", 0, winreg.REG_DWORD, 2 if enable else 1)
            return True
        except Exception as e:
            print(f"Error toggling GPU scheduling: {e}")
            return False

    def toggle_ultimate_performance(self, enable: bool) -> bool:

        try:
            if enable:

                subprocess.run([
                    "powercfg", "/duplicatescheme",
                    "e9a42b02-d5df-448d-aa00-03f14749eb61"
                ], capture_output=True, check=False)

                result = subprocess.run([
                    "powercfg", "/setactive",
                    "e9a42b02-d5df-448d-aa00-03f14749eb61"
                ], capture_output=True, check=True)
            else:

                result = subprocess.run([
                    "powercfg", "/setactive",
                    "381b4222-f694-41f0-9685-ff5bb260df2e"
                ], capture_output=True, check=True)

            return True
        except Exception as e:
            print(f"Error setting power plan: {e}")
            return False

    def toggle_xbox_features(self, disable: bool) -> bool:

        try:

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.xbox_key, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0 if disable else 1)
                winreg.SetValueEx(key, "GameDVR_Enabled", 0, winreg.REG_DWORD, 0 if disable else 1)
                winreg.SetValueEx(key, "HistoricalCaptureEnabled", 0, winreg.REG_DWORD, 0 if disable else 1)

            game_bar_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, game_bar_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "AllowGameDVR", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            policy_key = r"SOFTWARE\Policies\Microsoft\Windows\GameDVR"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, policy_key) as key:
                    winreg.SetValueEx(key, "AllowGameDVR", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error toggling Xbox features: {e}")
            return False

    def get_current_states(self) -> Dict[str, Any]:

        states = {
            'game_mode': False,
            'gpu_scheduling': False,
            'ultimate_performance': False,
            'xbox_disabled': False
        }

        try:

            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.game_mode_key) as key:
                    value, _ = winreg.QueryValueEx(key, "AutoGameModeEnabled")
                    states['game_mode'] = bool(value)
            except Exception:
                pass

            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.gpu_scheduling_key) as key:
                    value, _ = winreg.QueryValueEx(key, "HwSchMode")
                    states['gpu_scheduling'] = value == 2
            except Exception:
                pass

            try:
                result = run_command_silent(["powercfg", "/getactivescheme"])
                if result.returncode == 0:
                    states['ultimate_performance'] = "e9a42b02-d5df-448d-aa00-03f14749eb61" in result.stdout
            except Exception:
                pass

            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.xbox_key) as key:
                    value, _ = winreg.QueryValueEx(key, "GameDVR_Enabled")
                    states['xbox_disabled'] = value == 0
            except Exception:
                pass

        except Exception as e:
            print(f"Error getting current states: {e}")

        return states
