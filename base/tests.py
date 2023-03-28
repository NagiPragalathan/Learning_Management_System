import pyautogui
import random
import time
sorry = ['sorry deeeeeeeee', 'sorry de eni epade panna matan',
         'un kal le kudhe vilere', 'So sorryy', 'Sorry diiii']
time.sleep(2)


for i in range(100):
    if random.choice([1]) == 1:
        pyautogui.typewrite(random.choice(sorry))
        pyautogui.press('enter')
        time.sleep(1)
    else:
        pyautogui.typewrite(
            "sorry d"+random.choice(["e", 'i'])*(random.choice([i for i in range(10)])))
        pyautogui.press('enter')
        time.sleep(1)
