from inputim.inputs import search_id ,input_num ,  choose_num ,new_name
import json




def show_all_rooms():
    with open("jsons/room.json" , "r") as file:
        rooms = json.load(file)
    return rooms 

def show_room(id):
    rooms = show_all_rooms()
    for room in rooms:
        if room["room_id"] == id:
            return room

def add_new_room():
    room = {
    "room_id": "",
    "name": "",
    "difficulty":"",
    "duration":"" ,
    "min_players": "",
    "max_players":"" ,
    "price_per_player": "",
    "is_active": "true"
    } 
    last_id = last_id_rooms()
    new_id =get_next_id(last_id)
    room["room_id"] = new_id 
    room["duration"] = choose_num("duration")
    room["min_players"] =  choose_num("min_players")
    room["max_players"] = choose_num("max_players")
    room["price_per_player"] = choose_num("price_per_player")
    room["name"] = new_name()
    level = level_dificult()
    print(update_lavel(room , level))
    print(append_room(room))


def append_room(room):
    rooms  = show_all_rooms()
    rooms .append(room)
    with open("jsons/room.json", "w", encoding="utf-8") as file:
        json.dump(rooms, file, ensure_ascii=False, indent=4)
    return "new room add succces"



def last_id_rooms():
    last_id = " "
    rooms =show_all_rooms()
    for room in rooms:
        last_id = room["room_id"]
    return last_id
   


def get_next_id(last_id):
    next_number = int(last_id[1:]) + 1
    return f"R{next_number:03d}"

def level_dificult():
    print("""
    1.hard
    2.easy
    3. medium
    """)
    level = input_num(3)
    return level

def update_lavel(room , level):
    if level == "1":
        room[ "difficulty"] = "hard"
    elif level == "2":
        room[ "difficulty"] = "easy"    
    else: 
        room[ "difficulty"] = "medium"
    return f'{room["room_id"]} update to level :{level}'    
     
    
          

def push_rooms(rooms):
    with open("jsons/room.json", "w", encoding="utf-8") as file:
        json.dump(rooms, file, ensure_ascii=False, indent=4)
    print("the rooms is push sucsses!!!")    

def all_rooms_id():
    arr = []
    rooms  =show_all_rooms()
    for room in rooms:
        arr.append(room["room_id"])  
    return arr      

