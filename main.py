# TODO: load users from database/users.txt

class Facility:
    def __init__(self, name, booker_id):
        self.name = name
        self.booker_id = booker_id

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


#####################
# TODO: load everything from database/users.txt, database/bookings.txt, database/facilities.txt
users = [
    User("345", "admin123", "Maksim Volgin", "teacher"),
    User("258", "qwerty45", "Andrew Low Zhi Lun", "student"),
    User("912", "mypaswrd", "Neo Yu Jay", "student"),
]

facilities = [
    Facility("Name1", "345"),
    Facility("Name2", "0"),
    Facility("Name3", "0"),
    Facility("Name4", "0"),
]

bookings = [
    Booking("345", 10, 10, "12/12/25", "Maksim"),
]
#####################

def verify_user(id, password):
    return True  # TODO: verify

print("Welcome to <...>!\n")

id = input("Enter your ID: ")
password = input("Enter your password: ")

if not verify_user(id, password):
    exit("Invalid ID or password")

name = "Temp name"
print(f"Welcome, {name}!")

while True:
    print("\nBooking facilities:")
    print("1. Name1   Available")  # replace with actual facilities
    print("2. Name2   Unavalable")  # replace with actual facilities
    print("3. Name3   Available")  # replace with actual facilities
    print("4. Name4   Booked")  # replace with actual facilities
    print("\n5. Exit")

    exit_code = 5

    choice = int(input("Pick a facility (or exit): "))
    if choice == exit_code:
        print("Bye!")
        exit(0)
    

