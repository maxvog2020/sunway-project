########################################################
class Facility:
    def __init__(self, name, booker_id):
        self.name = name
        self.booker_id = booker_id  # 0 - not booked, other - booker_id

class User:
    def __init__(self, id, password, name, status):
        self.id = id
        self.password = password
        self.name = name
        self.status = status

class Booking:
    def __init__(self, booker_id, number_of_people, duration, date, name):
        self.booker_id = booker_id
        self.number_of_people = number_of_people
        self.duration = duration
        self.date = date
        self.name = name

########################################################
def load_users():
    users = []
    with open("database/users.txt", "r") as file:
        lines = filter(lambda x: x != "", file.read().splitlines()[1:])
        for line in lines:
            fields = map(str.strip, line.split(","))
            id, password, name, status = fields
            users.append(User(id, password, name, status))
    return users

def load_bookings():
    bookings = []
    with open("database/bookings.txt", "r") as file:
        lines = filter(lambda x: x != "", file.read().splitlines()[1:])
        for line in lines:
            fields = map(str.strip, line.split(","))
            booker_id, number_of_people, duration, date, name = fields
            bookings.append(Booking(booker_id, number_of_people, duration, date, name))
    return bookings

def load_facilities():
    facilities = []
    with open("database/facilities.txt", "r") as file:
        lines = filter(lambda x: x != "", file.read().splitlines()[1:])
        for line in lines:
            fields = map(str.strip, line.split(","))
            name, booker_id = fields
            facilities.append(Facility(name, booker_id))
    return facilities

def verify_user(id, password):
    for user in users:
        if user.id == id and user.password == password:
            return True
    return False

########################################################
users = load_users()
bookings = load_bookings()
facilities = load_facilities()

print("Welcome to <...>!\n")

id = input("Enter your ID: ")
password = input("Enter your password: ")

if not verify_user(id, password):
    exit("Invalid ID or password")

while True:
    print("\nBooking facilities:")
    for facility in facilities:
        if facility.booker_id == 0:
            print(f"{facility.name:<20} Available")
        elif facility.booker_id == id:
            print(f"{facility.name:<20} Booked")
        else:
            print(f"{facility.name:<20} Unavailable")
    print("\n5. Exit\n")

    exit_code = 5

    choice = int(input("Pick a facility (or exit): "))
    if choice == exit_code:
        print("\nBye!")
        exit(0)
    
