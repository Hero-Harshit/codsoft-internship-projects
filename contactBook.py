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

