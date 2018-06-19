import datetime
import time

'''
下面这个函数就相当于一个路障，结束时间到了就会放下路障原代码停止运行
开始时间到了就会收起来路障，原代码来继续运行
可以只提供开始时间
和结束小时相同时,结束分钟可以不同,超过了结束时间就会自动结束
'''


# beginhour beginminute开始时间  overhour overminute结束时间
def main(beginhour=0, overhour=0, beginminute=0, overminute=0):
    wait = 10
    if overhour == 0 and overminute == 0:
        while True:
            now = datetime.datetime.now()
            if now.hour == beginhour and now.minute == beginminute:  # 到达设定时间，进入函数外循环
                break
            time.sleep(wait)  # 等几秒后检测
        return
    else:
        now = datetime.datetime.now()
        if now.hour == overhour and now.minute >= overminute:
            while True:
                now = datetime.datetime.now()
                if now.hour == beginhour and now.minute == beginminute:
                    break
                time.sleep(wait)
        else:
            return


if __name__ == '__main__':
    for i in range(500):
        time.sleep(2)
        print(i)
        main(beginhour=22, beginminute=29, overhour=22, overminute=25)
