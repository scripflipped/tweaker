
import subprocess
import sys

def run_command_silent(command, shell=False, timeout=30, **kwargs):

    try:

        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

            creation_flags = subprocess.CREATE_NO_WINDOW

            result = subprocess.run(
                command,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=timeout,
                startupinfo=startupinfo,
                creationflags=creation_flags,
                **kwargs
            )
        else:

            result = subprocess.run(
                command,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=timeout,
                **kwargs
            )

        return result

    except subprocess.TimeoutExpired:
        print(f"Command timed out: {command}")
        raise
    except Exception as e:
        print(f"Command failed: {command}, Error: {e}")
        raise

def run_powershell_silent(command, timeout=30):

    powershell_cmd = ["powershell", "-WindowStyle", "Hidden", "-Command", command]
    return run_command_silent(powershell_cmd, timeout=timeout)

def run_reg_command_silent(command, timeout=30):

    return run_command_silent(command, timeout=timeout)
