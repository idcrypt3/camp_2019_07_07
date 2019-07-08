password="secret1234"
message="Monkeys can fly."
while True:
    attempt=input("Password: ")
    if attempt==password:
        print(message)
        break
    else:
        print("Incorrect password.\n")