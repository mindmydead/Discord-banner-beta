import os
import platform

os_name = platform.system()
if "windows" in os_name or "Windows" in os_name:
    os.system("python src/index.py")
else:
    os.system("python3 src/index.py")