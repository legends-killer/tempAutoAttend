import sys
from time import sleep
import pyautogui as pg
import pytweening
import datetime
import os

def my_click():
    width, height = pg.size()
    print(width ,height)
    width = width*0.92
    height = height*0.2
    pg.moveTo(width,height)
    sleep(3)
    pg.click(pg.position())
    sleep(10)
    pg.click(1876,111)
    sleep(10)
    pg.click(1900,17)

def main():
    os.system("start DingtalkLauncher.exe")
    my_click()
    sleep(5)

ISOTIMEFORMAT_F = '%H%M'
log = '%Y-%m-%d %H:%M'
last_time = "0000"
print("自动签到已启动,上次签到于：" + last_time)
cnt = 0
while 1:
    cnt = cnt+1
    if cnt >= 10:
        cnt = 0
        os.system("cls")
        print("自动签到已启动,上次签到于：" + last_time)
    sleep(1)
    time = datetime.datetime.now().strftime(ISOTIMEFORMAT_F)
    print("当前时间:" + time)
    if time >= '0825' and time <= '0835':
        last_time = datetime.datetime.now().strftime(log)
        main()
    if time >= '2125' and time <= '2135':
        last_time = datetime.datetime.now().strftime(log)
        main()