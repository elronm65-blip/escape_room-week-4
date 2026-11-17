
def input_num(num):
    choose = input(f'choose option from 1 -{num}')
    while not choose.isdigit():
        print("must be a number !!!")
        choose = input(f'choose option from 1 -{num}')
    while  1  > int(choose)  or   int(choose)> num:
        print(f"must be 1 - {num}")
        choose = input(f'choose option from 1 -{num}')
    return choose


def search_id():
    id = input("choose id")
    while id.isdigit():
        print("id cannot be only nums")
        id = input("choose id")
    while len(id) <= 0:
        print("id canot be empty")
        id = input("choose id")
    return id    

def new_name():
    name = input("choose name")
    while name.isdigit():
        print("name cannot be only nums")
        name = input("choose name")
    while len(name) <= 0:
        print("name canot be empty")
        name = input("choose name")
    return name    



def choose_num(num):
    choose = input(f'choose :{num}')
    while not choose.isdigit():
        print("must be a number !!!")
        choose = input(f'choose {num}')
    return int(choose)

def choose_price():
    price =("input price")
    while not price.isdigit():
        print("must be a number !!!")
        price =("input price")
    while int(price) <= 0:
        print("price canot be empty")
        price =("input price")
    return int(price)        
      

def count_players(id):
    from jsons.func_jsons import show_all_rooms
    rooms = show_all_rooms()
    selected_room = None
    for room in rooms:
        if room["room_id"] == id:
            selected_room = room
            break
    while True:
        players = input("how much players")
        while not players.isdigit():
            players = input("how much players")
        
        if selected_room["min_players"]  <= int(players) <=selected_room[ "max_players"]:
            return(int(players))
        else:
            print("the count of players not in the range")
       