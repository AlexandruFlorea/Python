import win32com.client
import time
import subprocess


shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("Notepad")
time.sleep(1)
shell.AppActivate("Notepad")

msg = """Good morning, you beautiful ray of sunshine! I wish you a great day, because you're awesome and I feel good having you around.
Now let's enjoy a delicious cup of coffee together before I slap your hotbuns silly...
"""

delay = 0.07
for i in msg:
    time.sleep(delay)
    shell.SendKeys(i, 0)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

        print(f'Message destroying in {t}')

countdown(5)

subprocess.call(["taskkill", "/F", "/IM", "Notepad.exe"])
