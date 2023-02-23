#Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

privileged_users = ("Dovydas", "Neringa", "Dane", "Dijora")
entered_name = input("Enter your name :")

if entered_name in privileged_users:
    print(f" Hello beauty {entered_name}")
else:
    print("You're are not in the list buddy")