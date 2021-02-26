import cv2


class OneSideOfCube:
    block0 = ""  # 二阶魔方某个单面的左上角
    block1 = ""  # 二阶魔方某个单面的右上角
    block2 = ""  # 二阶魔方某个单面的右下角
    block3 = ""  # 二阶魔方某个单面的左下角


Side = [OneSideOfCube.block0, OneSideOfCube.block1, OneSideOfCube.block2, OneSideOfCube.block3]

colorDict = {"white": "0", "yellow": "0", "green": '0', "blue": '0', "orange": '0', "red": '0'}
oppositeDict = {"white": "yellow", "yellow": "white", "green": "blue", "blue": "green", "orange": "red", "red": "orange"}


def get_opposite_side(side):
    return oppositeDict[side]


def color_set(block_color, model):  # 函数返回值为颜色对应的面
    if model == 0:
        forward3 = block_color
        colorDict[forward3] = "F"
        colorDict[get_opposite_side(forward3)] = "B"
    elif model == 1:
        left2 = block_color
        colorDict[left2] = "L"
        colorDict[get_opposite_side(left2)] = "R"
    elif model == 2:
        down0 = block_color
        colorDict[down0] = "D"
        colorDict[get_opposite_side(down0)] = "U"


def color_recognition(b, g, r, flag=0):  # flag为1时是用于识别颜色并输出字符串，为0时是用于判断forward3的颜色以确定正面的颜色
    # rgb转hsv
    # 基础量计算
    B = b / 255
    G = g / 255
    R = r / 255
    C_max = max(B, G, R)
    C_min = min(B, G, R)
    delta = C_max - C_min
    # 计算h大小
    if delta == 0:
        h = 0
    else:
        if C_max == R:
            h = 60 * (G - B) / delta
        elif C_max == G:
            h = 60 * (B - R) / delta + 120
        elif C_max == B:
            h = 60 * (R - G) / delta + 240
    h = abs(h)  # 红色有时是负数，所以取个绝对值
    # 计算s大小
    if C_max == 0:
        s = 0
    else:
        s = delta / C_max
    # 计算v大小
    v = C_max
    # 根据hsv进行比较判断
    if 0 <= h <= 360 and 0 <= s <= 30 / 255 and 120 / 255 <= v <= 1:  # white
        return colorDict["white"] if flag else "white"
    elif 0 <= h <= 10 and 43 / 255 <= s <= 1 and 46 / 255 <= v <= 1:  # red
        return colorDict["red"] if flag else "red"
    elif 10 < h <= 40 and 43 / 255 <= s <= 1 and 46 / 255 <= v <= 1:  # orange
        return colorDict["orange"] if flag else "orange"
    elif 40 < h <= 80 and 43 / 255 <= s <= 1 and 46 / 255 <= v <= 1:  # yellow
        return colorDict["yellow"] if flag else "yellow"
    elif 100 <= h <= 160 and 43 / 255 <= s <= 1 and 46 / 255 <= v <= 1:  # green
        return colorDict["green"] if flag else "green"
    elif 160 <= h <= 240 and 43 / 255 <= s <= 1 and 46 / 255 <= v <= 1:  # blue
        return colorDict["blue"] if flag else "blue"


def color_extraction(side, flag=0):
    solution = ""
    init_img = cv2.imread(side + ".jpg")                # 获得初始图片
    resize_img = cv2.resize(init_img, (576, 768))       # 缩放初始图片
    final_img = resize_img[0:600, 0:576]                # 图片适当裁剪
    for block in range(2):
        b = final_img[150, 288 * block + 144, 0]
        g = final_img[150, 288 * block + 144, 1]
        r = final_img[150, 288 * block + 144, 2]
        Side[block] = color_recognition(b, g, r, flag)
        if flag == 1:
            solution += Side[block]
    b = final_img[450, 432, 0]
    g = final_img[450, 432, 1]
    r = final_img[450, 432, 2]
    Side[2] = color_recognition(b, g, r, flag)
    if flag == 1:
        solution += Side[2]
    b = final_img[450, 144, 0]
    g = final_img[450, 144, 1]
    r = final_img[450, 144, 2]
    Side[3] = color_recognition(b, g, r, flag)
    if flag == 1:
        solution += Side[3]
    return solution


def get_solution():
    solution = ""
    color_extraction("forward", 0)  # 识别forward3的颜色
    color_set(Side[3], 0)
    color_extraction("left", 0)  # 识别left2的颜色
    color_set(Side[2], 1)
    color_extraction("down", 0)  # 识别down0的颜色
    color_set(Side[0], 2)
    cube_side = ["back", "down", "forward", "left", "right", "up"]
    for single_side in cube_side:  # 识别所有面的颜色
        solution += color_extraction(single_side, 1)
    return solution
