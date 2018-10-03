import inspect
import os


# 部署服务器用 输出文件名和进程pid 记录到父目录
# 因为 Windows垃圾转义问题 d的split('\\')在pycharm里应该会报错
# process.conf  process_moreinfo.conf (内容需要一个{})  请自行在父目录新建
def main():
    d = inspect.stack()[1][1].split('\\')[-1].replace('.py', '')
    with open('../process.conf', 'r', encoding='UTF-8') as f:
        try:
            dict1 = eval(f.read())
            print(dict1)
        except:
            dict1 = {}
    with open('../process.conf', 'w', encoding='UTF-8') as f:
        dict1[d] = os.getpid()
        f.write(str(dict1))


def self_info(string):
    d = inspect.stack()[1][1].split('\\')[-1].replace('.py', '')
    with open('../process_moreinfo.conf', 'r', encoding='UTF-8') as f:
        try:
            dict1 = eval(f.read())
        except:
            dict1 = {}
    with open('../process_moreinfo.conf', 'w', encoding='UTF-8') as f:
        dict1[d] = string
        f.write(str(dict1))




if __name__ == '__main__':
    main()
