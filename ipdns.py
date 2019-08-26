import subprocess
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    subprocess.call("netsh interface show interface".split())
    # subprocess.call("netsh interface ipv4 add dnsserver Wi-Fi address=8.8.8.8 index=1".split())
    # subprocess.call("netsh Interface ip set address Wi-Fi static 192.168.2.65 255.255.255.0 192.168.2.1".split())
    subprocess.call("netsh Interface ip set address Wi-Fi dhcp".split())

else:

    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
# subprocess.call("netsh interface show interface".split())
# subprocess.call("netsh Interface ip set address Wi-Fi static 192.168.2.64 255.255.255.0 192.168.2.1".split())