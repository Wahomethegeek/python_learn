username = input("Whats your name: ")
if username == "Wahome":
    print("User exist")
else:
    print("Username accepted")
age = int(input("Whats your age: "))
if age < 18:
    print("Unable to assign ID")
    exit()
else:
    print("Proceed to apply for ID")
# conditional statements
x = 10
y = 13
if x > y:
    print("achieved")
elif y==x :
    print("no way")
else:
    print("No we did it")
