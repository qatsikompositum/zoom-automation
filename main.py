import pyautogui
import time
import subprocess

id = input("id:")
subprocess.Popen("C:\\Users\\ilhan\\AppData\\Roaming\\Zoom\\bin\\Zoom")
time.sleep(3)
x = [950, 760, 760, 1000, 970, 970]
y = [540, 650, 690, 740, 500, 740]
print("Opening...")
# index 0 = join a meeting and entering id
# index 1 and 2 = selecting options
# index 3 = join
# index 4 = meeting passcode
# index 5 = join meeting
for i in range(6):
    pyautogui.click(x[i], y[i])
    time.sleep(2)
    if i == 0:
        time.sleep(3)
        pyautogui.write(id)
    elif i == 4:
        time.sleep(3)
        pyautogui.write("Bhyal.2020")
        time.sleep(3)
