import sys
import config

if "win" in sys.platform:
    config.OS = "windows"
else:
    config.OS = "linux"
