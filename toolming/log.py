import requests
from random import randint
from logging import *
global logger,hander,console
logger=getLogger(__name__)
hander=FileHandler('log.txt')
# console=StreamHandler()  直接print不用这个了

logger.setLevel(INFO)
hander.setLevel(INFO)
# console.setLevel(INFO)

formmatter = Formatter('%(asctime)s %(message)s')
hander.setFormatter(formmatter)

logger.addHandler(hander)


def push(string='',text=''):
    text='ID '+str(randint(0,999))+'  '+text
    url = 'https://sc.ftqq.com/SCU26255T056cec246e3b3a38201ee60da7718e9b5af5093d4bd69.send'
    data = {'text': string, 'desp': text}
    requests.post(url=url, data=data)

def easylog(filename='',string='',text=''):
    print(string+text)
    logger.info('-'+filename+'-'+string+'-'+text)

def easypush(string,filename='',text='',):
    print(string+text)
    push(string=string,text=text)
    logger.info('-' + filename + '-' + string + '-' + text)


# 1 新建loggger,FileHandler(输出到文件),StreamHandler(输出到其他流，如控制台)这里我直接print了
# 2 给loggger FileHandler StreamHandler设置日志级别
# 3 Formatter设置日志格式 赋给需要的
# 4 把FileHandler，StreamHandler用addHandler到loggger里
# 5 输出


if __name__ == '__main__':
    easypush(string='我爱你啊',filename='log',text='emmm')

# class logs:   #本来是打算在里面报错五次微信提醒...一想好蠢
#     def __init__(self):
#         self.count=1
#     def exportlog(self,str,filename='',text=''):    # 附上默认值就是不必要函数了
#         print(str)
#         logger.info('-'+filename+'-'+str+'-'+text)
#         if self.count==5:                                              # 报错五次微信提醒
#             push(str=str,text=text)
#         self.count = self.count + 1
#     def setcount0(self):
#         self.count=1