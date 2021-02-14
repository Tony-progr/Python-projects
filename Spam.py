import pyautogui, time

time.sleep(10) #<-- Take some time to prepare:

f = open("Spam.txt", 'r') #<-- Open the Spam.txt file:
words = f.readline() #<-- Get the massage
times_spam = f.readline() #<-- How many times it will send the message.

#Start sending:
for x in range(int(times_spam)):
    pyautogui.press('shiftleft')
    pyautogui.press('enter')
    pyautogui.typewrite(words)
    pyautogui.press('enter')
