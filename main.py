from typing import Dict, List
import translate
import recognition


import pymongo


client = pymongo.MongoClient(
    "mongodb://crepusculum.xyz:27017/",
    username="cube",
    password="123"
)
cubeDB = client["cube"]
collection = cubeDB["direct_pass"]


string = recognition.get_solution()
cubeStr: str = string
req: Dict = collection.find_one({"cube_str": cubeStr})
solution: List = req["pass"]

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

for i in commandList:
    print(i)
