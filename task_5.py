contacts = []

def show_menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📒 All Contacts:")
        for idx, c in enumerate(contacts, 1):
            print(f"{idx}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c['name'].lower() or keyword in c['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name   : {c['name']}")
            print(f"Phone  : {c['phone']}")
            print(f"Email  : {c['email']}")
            print(f"Address: {c['address']}")
            found = True
            break
    if not found:
        print("❌ No matching contact found.")

def update_contact():
    phone = input("Enter phone number of contact to update: ")
    for c in contacts:
        if c['phone'] == phone:
            print("Leave blank to keep current value.")
            name = input(f"New Name ({c['name']}): ") or c['name']
            email = input(f"New Email ({c['email']}): ") or c['email']
            address = input(f"New Address ({c['address']}): ") or c['address']
            c.update({"name": name, "email": email, "address": address})
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")
    for c in contacts:
        if c['phone'] == phone:
            contacts.remove(c)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 6.")
