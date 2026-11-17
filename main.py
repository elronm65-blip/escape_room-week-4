from shows.show import print_main_manue , show_managment_rooms , show_managment_booking
from inputim.inputs import input_num ,search_id
from jsons.func_jsons import show_all_rooms , show_room , add_new_room 
from func_update.function import update_room , update_active_room
from booking.func_booking import   new_booking
import json
while True:
    
    print_main_manue()
    choose = input_num(6)
    if choose == "1":
        show_managment_rooms()
        choose = input_num(6)
        if choose == "1":
            print(show_all_rooms())
        if choose == "2":
            id = search_id()
            print(show_room(id))
        if choose == "3":
            add_new_room()
        if choose == "4":
            update_room()
        if choose == "5":
            print(update_active_room())
    if choose == "2":
        show_managment_booking()
        choose = input_num(7)  
        if choose == "1":
            new_booking()

        




        



