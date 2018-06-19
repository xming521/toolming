import inspect
import os


# 部署服务器用 输出文件名和进程pid 记录到主目录
def main():
    d = inspect.stack()[1][1].split('/')[-1].replace('.py', '')
    with open('../process.conf', 'a', encoding='UTF-8') as f:
        f.writelines('\n')
        f.write(d + '|')
        f.write(str(os.getpid()))


if __name__ == '__main__':
    main()
