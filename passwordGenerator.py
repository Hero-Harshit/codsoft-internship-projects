Main_Database = []

def add_contact(name, surname, phone):
    contact = {"name": name, "surname": surname, "phone": phone}
    Main_Database.append(contact)
    print(f"Contact {name} added successfully!")

def search_contact(query):
    found = False
    for contact in Main_Database:
        if (contact["name"].lower() == query.lower() or
            contact["surname"].lower() == query.lower()):
            print(f"Found: {contact['name']} {contact['surname']} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def display_contacts():
    if not Main_Database:
        print("No contacts in the database.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(Main_Database, start=1):
        print(f"{idx}. {contact['name']} {contact['surname']} - {contact['phone']}")

print("Welcome to the Contact Book!")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        name = input("Enter name: ").strip()
        surname = input("Enter surname: ").strip()
        phone = input("Enter phone number: ").strip()

        if not name or not surname or not phone:
            print("All fields are required!")
            continue

        if not phone.isdigit():
            print("Phone number should contain only digits.")
            continue

        add_contact(name, surname, phone)

    elif choice == '2':
        query = input("Enter name or surname to search: ").strip()
        if query:
            search_contact(query)
        else:
            print("Please enter something to search.")

    elif choice == '3':
        display_contacts()

    elif choice == '4':
        print("Exiting the Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")