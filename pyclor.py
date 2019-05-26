import time
import sys

import functions as fc

def main():
    """主函数"""
    # 欢迎
    fc.welcome()

    # 加载文件
    try:
        filename = sys.argv[1]
    except:
        sys.exit()
    print("PyClor started "+"["+time.strftime('%Y.%m.%d',time.localtime(time.time()))+"]\n")
    try:
        f = open(filename, "r")
    except:
        color.print_red_text("file does not exist.")
        sys.exit()
    lines = f.readlines()
    f.close()

    # 处理文件内容
    fc.insert_enter(lines)
    try:
        if sys.argv[2] == "insert_tab":
            fc.insert_tab(lines)
        elif sys.argv[2] == "detect_tab":
            fc.detect_tab(lines)
        else:
            pass
    except:
        pass

    # 写入修改内容
    f = open(filename, "w")
    for line in lines:
        f.write(line)
    print("\nFinished " + "[" + time.strftime('%Y.%m.%d', time.localtime(time.time())) + "]")

if __name__ == "__main__":
    main()
