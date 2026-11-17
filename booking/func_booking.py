import json
from datetime import datetime ,timedelta ,time
from inputim.inputs import new_name , search_id ,count_players
from jsons.func_jsons import all_rooms_id ,show_all_rooms

def all_booking(): 
    with open("jsons/booking.json" , "r") as file:
        all_booking = json.load(file)
    return all_booking    


def last_booking_id(all_booking):
    id_booking =""
    for booking in all_booking:
        id_booking =booking["booking_id"]
    return id_booking   

def next_booking_id(id_booking):
    next_number = int(id_booking[1:]) + 1
    return f"B{next_number:03d}"

def all_booking_id(all_booking):
    arr = []
    for booking in all_booking:
        arr.append(booking["booking_id"])
    return arr    


def new_booking():
    booking =    {
        "booking_id": " ",
        "customer_name": "",
        "room_id": "",
        "booking_date": "",
        "start_time": "",
        "players":"",
        "total_price":"",
        "status": "Active",
        "cancellation_fee": 0.0
    }
# בדיקת איי די אוטומטי
    bookings = all_booking()
    last = last_booking_id(bookings)
    id  = next_booking_id (last)
    booking["booking_id"] = id

#עדכון שם מבעל הזמנה
    customer = new_name()
    booking["customer_name"] = customer

 #הזנת חדר ובדיקה שאכן קיים  וגם שהוא זמין
    room_id =search_id()
    rooms_id =all_rooms_id()
    while room_id not in rooms_id:
        print("room id not found in rooms list")
        room_id = search_id()
    rooms = show_all_rooms() 
    for room in rooms :
        if room["room_id"] == room_id:
            if room["is_active"] == "true":
                break
            else:
                print("the room not activeee")
                return   
    booking["room_id"] = room_id


#שליפת משך זמן  משחק וכמה עולה לשחקן
    for room in rooms:
        if room["room_id"] == room_id:
            game_diraction = room["duration"]
            price_game = room["price_per_player"]
            break

    
    plus = timedelta(minutes = game_diraction +15)
    open_time = time(10, 0)
    close_time = time(22, 0)
    latest_start = (datetime.combine(datetime.today(), close_time) - timedelta(minutes=game_diraction)).time()
#הכנסת תאריכים בפורמט דייט טיים ופיצול לשעה ותאריך
    while True:
        dt = get_booking_datetime()
        only_date = dt.date()
        only_time = dt.time() 

        if only_time < open_time or only_time > latest_start:
            print(f"Error: Must be between 10:00 and {latest_start.strftime('%H:%M')}")
            continue

       

    #יצירת מערך של כל השעות התפוסות לפי הזמנות פעילות ובאותו איידי של חדר ובאותו היום בלבד
        all_bookings = all_booking()
        all_hours = []
        for book in all_bookings:
            if book["booking_date"] == only_date.isoformat() and book["room_id"] == room_id and book["status"] == "Active":
                hour_obj = datetime.strptime(book["start_time"], "%H:%M").time()
                all_hours.append(hour_obj)     
#יצירת טווח על כל שעה  לפני ואחרי כולל  15 דקות מנוחה 
        is_avalibale = True
        for hour in all_hours:
            whole_date = datetime.combine( only_date ,hour)
            block_start = (whole_date - plus).time()
            block_end = (whole_date + plus).time()
            if  block_start < only_time < block_end:
                is_avalibale = False
                print("the time is already in use try anothet time")
                break
        if is_avalibale:
            break

    
#הגדרת המפתחות במילון סופית כסטרינג        
    booking["booking_date"] =only_date.strftime("%Y-%m-%d")
    booking["start_time"] = only_time.strftime("%H:%M")
   
#הזנת מספר שחקנים ובדיקה שהוא בטווח             
    booking["players"] = count_players(room_id)

#בדיקת הנחה והאם זה סופש ועדכון מחיר סופי    

    booking["total_price"] = calculate_discount(only_date ,booking["players"] ,price_game )
#דחיפת הזמנה להזמנות     
    push_booking(bookings,booking)
    print("the booking add succesee!!!")
    


def calculate_discount(date_day , persons ,price):
    total = persons * price
    if persons in [5,6]:
        total = total*0.9
    elif persons >= 7:
        total = total*0.85
    if   date_day.weekday() in [4,5]:
        total *= 1.15
    return round(total, 2)   


    
def get_booking_datetime():
    while True:
        date_str = input("Enter date (DD/MM/YYYY): ")
        time_str = input("Enter time (HH:MM): ")
        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")
            if dt < datetime.now():
                print("Error: Date and time cannot be in the past.")
                continue
            return dt
        except ValueError:
            print("Invalid format! Use DD/MM/YYYY (4-digit year) and HH:MM.")


def push_booking( bookings,book):
    bookings.append(book)
    with open("jsons/booking.json", "w", encoding="utf-8") as file:
        json.dump(bookings, file, ensure_ascii=False, indent=4)
    print("the bookings is push sucsses!!!")   
    



    


def calculate_total_price(players, price_per_player, booking_dt):
    price = players * price_per_player
    if 5 <= players <= 6:
        price *= 0.90  
    elif players >= 7:
        price *= 0.85  
    if booking_dt.weekday() in (4, 5):
        price *= 1.15  
    return round(price, 2)
