from typing import Dict, List
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
print(solution)
