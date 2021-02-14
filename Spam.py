import pyautogui, time

time.sleep(10)

f = open("Spam.txt", 'r')
words = f.readline()
times_spam = f.readline()

for x in range(int(times_spam)):
    pyautogui.press('shiftleft')
    pyautogui.press('enter')
    pyautogui.typewrite(words)
    pyautogui.press('enter')