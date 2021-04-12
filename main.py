from typing import Dict, List
import translate
import recognition
import json

import pymongo

client = pymongo.MongoClient(
    "mongodb://crepusculum.xyz:27017/",
    username="cube",
    password="123"
)
cubeDB = client["cube"]
direct_pass_collection = cubeDB["direct_pass"]
mini_cmd_collection = cubeDB["mini_cmd"]

string = recognition.get_solution()
print(string)
cubeStr: str = string
req: Dict = direct_pass_collection.find_one({"cube_str": cubeStr})
solution: List = req["pass"]

print(solution)
commandList: List = []
for commandChar in solution:
    if commandChar == 'u':
        translate.cube_twist_clockwise(commandList)

    elif commandChar == 'cu':
        translate.cube_twist_anti_clockwise(commandList)

    elif commandChar == 'r':
        translate.cube_spin_right(commandList)
        translate.cube_up_turn_forward(commandList)
        translate.cube_twist_anti_clockwise(commandList)
        translate.cube_down_turn_forward(commandList)
        translate.cube_spin_left(commandList)

    elif commandChar == 'cr':
        translate.cube_spin_right(commandList)
        translate.cube_up_turn_forward(commandList)
        translate.cube_twist_clockwise(commandList)
        translate.cube_down_turn_forward(commandList)
        translate.cube_spin_left(commandList)

    elif commandChar == 'b':
        translate.cube_up_turn_forward(commandList)
        translate.cube_twist_anti_clockwise(commandList)
        translate.cube_down_turn_forward(commandList)

    elif commandChar == 'cb':
        translate.cube_up_turn_forward(commandList)
        translate.cube_twist_clockwise(commandList)
        translate.cube_down_turn_forward(commandList)

print(commandList)
print(len(commandList))
translate.simplify_command(commandList)
print(commandList)
mini_cmd_collection.delete_many({})
mini_cmd_collection.insert_one({"mini_cmd": commandList})  # 保存到mini_cmd
