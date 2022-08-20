import time

import pyautogui as pg

time.sleep(3)
i = 0
#while True:
for j in range(3460):
    time.sleep(1)
    #centers = pg.locateCenterAllOnScreen("kin.png", grayscale=True, confidence=0.6)
    #centers = pg.locateAllOnScreen("kin.png", grayscale=True, confidence=0.9)
    #lst = list(centers)
    #print(len(lst))

    following = pg.locateOnScreen("following.png", confidence=0.9)
    pg.click(following)
    time.sleep(0.5)
    unfollow = pg.locateOnScreen("unfollow.png", grayscale=True, confidence=0.9)
    pg.click(unfollow)
    if i==4:
        pg.hotkey("shiftleft","ctrlleft","r")
        i = 0
        time.sleep(4)

    #下スクロール
    for n in range(i):
        pg.press("down")
        pg.press("down")
        pg.press("down")
        pg.press("down")
        pg.press("down")
    i = i + 1
