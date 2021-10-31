# ReadAdbLogcat
Simple python script that reads logs from adb logcat in realtime (with a 20-ish seconds delay). <br />
The script creates a new subprocess that runs "adb logcat" command, sets it in a new thread, starts the thread, and saves the information that comes from adb logcat in the "log.txt" file with utf-8 encoding.<br/>
<br/>
# Prerequisites:
"adb" command set in the PATH environment variable
