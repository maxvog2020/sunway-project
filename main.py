# TODO: load users from database/users.txt

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
    
    
   
