Main_Database = []

def add_contact(name, surname, phone):
    contact = {"name": name, "surname": surname, "phone": phone}
    Main_Database.append(contact)
    print(f"Contact {name} added successfully!")

def search_contact(name):
    for contact in Main_Database:
        if contact["name"].lower() == name.lower():
            print(f"Contact found: {contact['name']} {contact['surname']} - {contact['phone']}")
            return
    print("Contact not found.") 

def display_contacts():
    if not Main_Database:
        print("No contacts in the database.")
        return
    print("Contact List:")
    for contact in Main_Database:
        print(f"{contact['name']} {contact['surname']} - {contact['phone']}")


print("Welcome to the Contact Book!")
while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone = input("Enter phone number: ")
        add_contact(name, surname, phone)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# End