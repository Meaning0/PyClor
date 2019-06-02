import sys
import use_color

def welcome():
    use_color.print_green_text(r'''
 mmmmm           mmm  ""#
 #   "# m   m  m"   "   #     mmm    m mm
 #mmm#" "m m"  #        #    #" "#   #"  "
 #       #m#   #        #    #   #   #
 #       "#     "mmm"   "mm  "#m#"   #
         m"
        ""
''')
    print("\n")

def insert_enter(lines):
    """对需要空行的地方加上空行"""
    for num in range(len(lines)):
        # import检测
        sign = import_detector(lines, num)
        if sign:
            continue
        # 对class的检测
        sign = class_detector(lines, num)
        if sign:
            continue
        # 对def的检测
        def_detector(lines, num)

def insert_tab(lines):
    """在需要缩进的地方缩进"""
    tab = " "
    # 打印所有代码及行数
    for num in range(len(lines)):
        print(lines[num].rstrip() + " " + str(num) + "\n")

    # 输入行数，缩进大小，间隔
    num_1 = input("Please enter the number of starting lines to be sorted out[number/q]: ")
    num_2 = input("Please enter the number of endpoint rows to be collated[number/q]: ")
    num_3 = input("Please enter the indentation size[number/q]: ")
    hrn = input("Please enter the number of jumping rows[number/q]: ")
    # 如果输入为“q”或者瞎输就退出
    if (num_1 or num_2 or hrn) == "q":
        print("\nFinished " + "[" + time.strftime('%Y.%m.%d', time.localtime(time.time())) + "]")
        sys.exit()
    elif not (num_1 or num_2 or hrn or num_3).isdigit():
        print("Please enter the correct number ! ! !")
        sys.exit()
        
    try:
        num_1 = int(num_1)
        temp = num_1
        num_2 = int(num_2)
        num_3 = int(num_3)
        hrn = int(hrn)
    except:
        color.print_red_text("Error")
        sys.exit()

    # 开始添加缩进
    for line in lines[num_1:num_2 + 1]:
        # 反添加缩进，也就是删除缩进
        if num_3 < 0:
            if temp == num_1:
                lines[num_1] = line.lstrip(abs(num_3)*tab)
            else:
                try:
                    lines[num_1 + hrn] = lines[num_1 + hrn].lstrip(abs(num_3)*tab)
                except:
                    pass
                if hrn:
                    hrn += 1

        # 添加缩进
        elif temp == num_1:
            lines[num_1] = num_3*tab + line
        else:
            try:
                lines[num_1+hrn] = num_3*tab + lines[num_1+hrn]
            except:
                pass
            if hrn:
                hrn += 1
        num_1 += 1

def detect_tab(lines):
    """检测在冒号后有无缩进"""
    # 请用户输入缩进尺寸
    tab_size = input("Please enter the indentation size[number/q]: ")
    if tab_size == "q":
        print("\nFinished " + "[" + time.strftime('%Y.%m.%d', time.localtime(time.time())) + "]")
        sys.exit()
    elif not tab_size.isdigit():
        print("Please enter the correct number ! ! !")
        sys.exit()

    tab_size = int(tab_size)
    tab = " "*tab_size
    for num in range(len(lines)):
        if (":" in lines[num]) and ("#" not in lines[num]):
            if "class" in lines[num]:
                num_2 = lines[num+2].count(tab)
            else:
                num_2 = lines[num+1].count(tab)
            num_1 = lines[num].count(tab)
            if num_1 < num_2:
                pass
            else:
                use_color.print_red_text("[Warning] No indentation or irregularity is suspected after line " + str(num))
        else:
            pass

def import_detector(lines, num):
    """import检测"""
    try:
        if "import" in lines[num] and ("#" not in lines[num]):
            if (len(lines[num+1].strip()) == 0) or (("import" in lines[num+1]) and ("#" not in lines[num+1])):
                return True
            else:
                lines.insert(num+1, "\n")
                return True
        return False
    except:
        pass

def class_detector(lines, num):
    """对class的检测"""
    try:
        if "class" in lines[num] and ("#" not in lines[num]):
            if len(lines[num+1].strip()) == 0:
                return True
            else:
                lines.insert(num+1, "\n")
                return True
        return False
    except:
        pass

def def_detector(lines, num):
    """对def的检测"""
    try:
        if "def" in lines[num] and ("#" not in lines[num]):
            if len(lines[num-1].strip()) == 0:
                return
            else:
                lines.insert(num, "\n")
    except:
        pass
