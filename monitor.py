import inspect
import os


# 部署服务器用 输出文件名和进程pid 记录到主目录
# 因为 Windows垃圾转义问题 d的split('\\')在pycharm里应该会报错
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


if __name__ == '__main__':
    main()
