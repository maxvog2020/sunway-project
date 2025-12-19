from datetime import date, datetime

########################################################
# Constants
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
END_COLOR = '\033[0m'

########################################################
# Classes
class Facility:
    def __init__(self, name: str, booker_id: int):
        self.name = name
        self.booker_id = booker_id  # 0 - not booked, other - booker_id

class User:
    def __init__(self, id: int, password: str, name: str, status: str):
        self.id = id
        self.password = password
        self.name = name
        self.status = status

class Booking:
    def __init__(self, booker_id: int, number_of_people: int, duration: int, date: str, name: str):
        self.booker_id = booker_id
        self.number_of_people = number_of_people
        self.duration = duration
        self.date = date
        self.name = name

########################################################
# Functions
def read_database_file(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        lines = filter(lambda x: x != "", file.read().splitlines()[1:])
        return list(lines)

def load_users() -> list[User]:
    users = []
    lines = read_database_file("database/users.txt")
    for line in lines:
        fields = map(str.strip, line.split(","))
        id, password, name, status = fields
        user = User(int(id), password, name, status)
        users.append(user)
    return users

def load_bookings() -> list[Booking]:
    bookings = []
    lines = read_database_file("database/bookings.txt")
    for line in lines:
        fields = map(str.strip, line.split(","))
        booker_id, number_of_people, duration, date, name = fields
        booking = Booking(int(booker_id), int(number_of_people), int(duration), date, name)
        bookings.append(booking)
    return bookings

def load_facilities() -> list[Facility]:
    facilities = []
    lines = read_database_file("database/facilities.txt")
    for line in lines:
            fields = map(str.strip, line.split(","))
            name, booker_id = fields
            facility = Facility(name, int(booker_id))
            facilities.append(facility)
    return facilities

def verify_user(id: int, password: str) -> bool:
    for user in users:
        if user.id == id and user.password == password:
            return True
    return False

def print_invoice(booking: Booking):
    print(f"Number of people: {booking.number_of_people}")
    print(f"Duration: {booking.duration} days")
    print(f"Date: {booking.date}")
    print(f"Name: {booking.name}")

########################################################
# Main
users = load_users()
bookings = load_bookings()
facilities = load_facilities()

print("Welcome to <...>!\n")

id = int(input("Enter your ID: "))
password = input("Enter your password: ")

if not verify_user(id, password):
    print(f"\n{RED}Invalid ID or password{END_COLOR}")
    exit(1)

while True:
    print("\nBooking facilities:")
    for (index, facility) in enumerate(facilities):
        if facility.booker_id == 0:
            print(f"{index + 1}. {facility.name:<15} {GREEN}Available{END_COLOR}")
        elif facility.booker_id == id:
            print(f"{index + 1}. {facility.name:<15} {BLUE}Booked{END_COLOR}")
        else:
            print(f"{index + 1}. {facility.name:<15} {RED}Unavailable{END_COLOR}")
    print("\n5. Exit\n")

    exit_code = len(facilities) + 1

    choice = int(input("Pick a facility (or exit): "))

    if choice < 1 or choice > exit_code:
        print(f"\n{RED}Invalid choice{END_COLOR}")
        continue

    if choice == exit_code:
        print("\nBye!")
        exit(0)

    selected_facility = facilities[choice - 1]

    # if unavailable
    if selected_facility.booker_id != id and selected_facility.booker_id != 0:
        print(f"{RED}This facility is not available{END_COLOR}")
        continue  # go back to the main menu

    # if available
    if selected_facility.booker_id == 0:
        want_to_book = input("Do you want to book this facility? (Y/N): ").upper()

        if want_to_book not in ["Y", "N"]:
            print(f"{RED}\nInvalid input{END_COLOR}")
            continue

        if want_to_book == "N":
            continue  # go back to the main menu

        # if yes
        pax = int(input("Enter number of people: "))
        duration = int(input("Enter duration in days: "))
        date_booking_string = input("Enter the date (dd/mm/yyyy): ")
        booking_name = input("Enter your name: ")

        if pax < 1:
            print(f"{RED}Number of people must be at least 1{END_COLOR}")
            continue
        
        if duration < 1:
            print(f"{RED}Duration must be at least 1 day{END_COLOR}")
            continue
        
        today = date.today()
        date_booking = datetime.strptime(date_booking_string, "%d/%m/%Y").date()

        if date_booking < today:
            print(f"{RED}\nInvalid date{END_COLOR}")
            continue
        
        selected_facility.booker_id = id
        booking = Booking(id, pax, duration, date_booking, booking_name)
        bookings.append(booking)
        print(f"{GREEN}\nYou have successfully booked this facilty!{END_COLOR}\n")

        print_invoice(booking)
        continue  # go back to the main menu
    
    # if booked by you
    if selected_facility.booker_id == id:
        booking = [booking for booking in bookings if booking.booker_id == id][0]
        print()
        print_invoice(booking)

        want_to_cancel = input("\nThis facility is booked. Cancel booking? (Y/N): ").upper()

        if want_to_cancel not in ["Y", "N"]:
            print(f"{RED}\nInvalid input{END_COLOR}")
            continue

        if want_to_cancel == "Y":
            selected_facility.booker_id = 0
            bookings.remove(booking)
            print(f"{GREEN}\nBooking cancelled!{END_COLOR}")
        continue  # go back to the main menu
    
