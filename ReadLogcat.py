import threading
import subprocess

THREAD = None
PROCESS = None
file = open("log.txt", "w", encoding="utf-8")

def read_log(process):
    for line in iter(process.stdout.readline, b""):
        file.write(line.decode())
        # print(line.decode(), end=''),


def read_log_thread():
    global THREAD
    global PROCESS
    PROCESS = subprocess.Popen(["adb logcat"], shell=False, stdout=subprocess.PIPE)
    THREAD = threading.Thread(target=read_log, args=(PROCESS,))
    THREAD.start()


def main():
    read_log_thread()
    if PROCESS and PROCESS.poll():
        PROCESS.terminate()
    THREAD.join()

if __name__ == '__main__':
    main()