# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import platform  # 导入platform模块

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} os{os.name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('操作系统名称：', platform.system())  # 获取操作系统名称
    print('操作系统名称及版本号：', platform.platform())  # 获取操作系统名称及版本号
    print('操作系统版本号：', platform.version())  # 获取操作系统版本号
    print('操作系统的位数：', platform.architecture())  # 获取操作系统的位数
    print('计算机类型：', platform.machine())  # 计算机类型
    print('计算机的网络名称：', platform.node())  # 计算机的网络名称
    print('计算机处理器信息：', platform.processor())  # 计算机处理器信息
    print('包含上面所有的信息汇总：', platform.uname())  # 包含上面所有的信息汇总
    exit(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
