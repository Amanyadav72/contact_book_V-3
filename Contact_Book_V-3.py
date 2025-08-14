
import json
import os

# Load contacts from file if exists
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
else:
    contacts = []

# Function to save to JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Function to find contact index by name
def find_contact(name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            return i
    return -1

# Main menu loop
while True:
    print("\n📒 Contact Book v3")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Edit Contact")
    print("5. Search by Name")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        save_contacts()
        print("✅ Contact added!")

    elif choice == "2":
        print("\n📋 All Contacts:")
        if not contacts:
            print("No contacts found.")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']}")

    elif choice == "3":
        name = input("Enter name to delete: ")
        index = find_contact(name)
        if index != -1:
            deleted = contacts.pop(index)
            save_contacts()
            print(f"🗑️ Deleted contact: {deleted['name']}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        name = input("Enter name to edit: ")
        index = find_contact(name)
        if index != -1:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            contacts[index] = {"name": new_name, "phone": new_phone}
            save_contacts()
            print("✏️ Contact updated.")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        name = input("Enter name to search: ")
        index = find_contact(name)
        if index != -1:
            c = contacts[index]
            print(f"🔍 Found: {c['name']} - {c['phone']}")
        else:
            print("❌ Contact not found.")

    elif choice == "6":
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1–6.")
