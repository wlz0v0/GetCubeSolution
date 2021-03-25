from typing import List


"""
"m1_up_only"
"m1_down_only"
"m1_up_both"
"m1_down_both"
"m2_clockwise"
"m2_anti"
"m3_clockwise"
"m3_anti"
"""


def cube_up_turn_forward(motor_cmd):            # 魔方上面翻到正面
    motor_cmd.append("m2_clockwise")
    motor_cmd.append("m1_up_both")
    motor_cmd.append("m2_anti")
    motor_cmd.append("m1_down_both")


def cube_down_turn_forward(motor_cmd):  # 魔方下面翻到正面
    motor_cmd.append("m1_up_both")
    motor_cmd.append("m2_clockwise")
    motor_cmd.append("m1_down_both")
    motor_cmd.append("m2_anti")


def cube_spin_left(motor_cmd):  # 魔方向左旋转
    motor_cmd.append("m1_up_only")
    motor_cmd.append("m3_clockwise")
    motor_cmd.append("m1_down_only")


def cube_spin_right(motor_cmd):       # 魔方向右旋转
    motor_cmd.append("m1_up_only")
    motor_cmd.append("m3_anti")
    motor_cmd.append("m1_down_only")


def cube_twist_clockwise(motor_cmd):  # 顺时针拧魔方
    motor_cmd.append("m1_up_both")
    motor_cmd.append("m3_clockwise")
    motor_cmd.append("m1_down_both")


def cube_twist_anti_clockwise(motor_cmd):  # 逆时针拧魔方
    motor_cmd.append("m1_up_both")
    motor_cmd.append("m3_anti")
    motor_cmd.append("m1_down_both")
