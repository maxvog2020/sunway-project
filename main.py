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

print("\nBooking facilities:")