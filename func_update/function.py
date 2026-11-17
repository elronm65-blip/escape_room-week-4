from jsons.func_jsons import show_all_rooms  ,update_lavel ,level_dificult,push_rooms 
from inputim.inputs import search_id , input_num , new_name , choose_price
from shows.show import update_room_show

def update_room():
    all_id  = all_id_rooms()
    id =search_id()
    while id not in all_id:
       print("this id not exsist!!!")
       id = search_id()
    rooms = show_all_rooms()
    update_room_show()
    choose = input_num(3)
    for room in rooms:
        if room["room_id"] == id:
            if choose == "1":
                level = level_dificult()
                print(update_lavel(room , level))
                push_rooms(rooms)
                return
            elif choose == "2":
                name = new_name()
                room["name"] = name
                print("name update succces")
                push_rooms(rooms)
                return
                
            else:
                price =  choose_price()
                room["price_per_player"] = price
                print("price  update succces")
                push_rooms(rooms)
                return
                
def update_active_room():
    rooms  = show_all_rooms()
    id =search_id()
    for room in rooms:
        if room["room_id"] == id:
            if room["is_active"] == "true":
                room["is_active"] = "false"
                push_rooms(rooms)
                return
            elif room["is_active"] == "false":
                room["is_active"] = "true"
                push_rooms(rooms)
                return
    return 'id not exixsting'        
    



             
          
          

    


      
   


def all_id_rooms():
    arr = []
    rooms = show_all_rooms()
    for room in rooms:
      arr.append(room["room_id"])
    return arr

