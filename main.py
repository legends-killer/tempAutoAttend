import sys
from time import sleep
import pyautogui as pg
import pytweening
import datetime
import os
ISOTIMEFORMAT_F = '%H%M'
log = '%Y-%m-%d %H:%M'
last_time = "0000"
def my_click():
    width, height = pg.size()
    print(width ,height)
    width = width*0.92
    height = height*0.2
    pg.moveTo(width,height)
    sleep(3)
    pg.click(pg.position())
    sleep(10)
    width, height = pg.size()
    width = width*0.977
    height = height*0.101
    pg.moveTo(width,height)
    pg.click(pg.position())
    sleep(10)
    width, height = pg.size()
    width = width*0.99
    height = height*0.017
    pg.moveTo(width,height)
    pg.click(pg.position())

def main():
    os.system("start DingtalkLauncher.exe")
    sleep(10)
    my_click()
    sleep(10)


print("自动签到已启动,上次签到于：" + last_time)
file = open('log' + '.txt','w')
file.close()
file = open('time' + '.txt','w')
file.close()
cnt = 0
while 1:
    cnt = cnt+1
    if cnt >= 10:
        cnt = 0
        f = open('time.txt','r+')
        f.truncate()
    sleep(1)
    time = datetime.datetime.now().strftime(ISOTIMEFORMAT_F)
    print("当前时间:" + time)
    with open('time.txt','w') as f:
        f.write('当前时间')
        f.write(time)
        f.write('\n')
    if time >= '0825' and time <= '0835':
        last_time = datetime.datetime.now().strftime(log)
        main()
        with open('log.txt','w') as f:
            f.write('自动签到成功！于：')
            f.write(last_time)
            f.write('\n')
    if time >= '2125' and time <= '2135':
        last_time = datetime.datetime.now().strftime(log)
        main()
        with open('log.txt','w') as f:
            f.write('自动签到成功！于：')
            f.write(last_time)
            f.write('\n')