import csv
import os

FILE_NAME = "contacts.csv"

# Create the CSV file with column headings if it does not exist
def initialize_file():
    try:
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"])
    except OSError as error:
        print("Error creating file:", error)


# Add a new contact
def add_contact():
    try:
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()

        if not name or not phone or not email:
            print("Error: All fields are required.")
            return

        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

        print("Contact added successfully!")

    except (OSError, csv.Error) as error:
        print("Error saving contact:", error)


# Display all saved contacts
def view_contacts():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip column headings

            contacts = list(reader)

            if not contacts:
                print("No contacts found.")
                return

            print("\n========== SAVED CONTACTS ==========")

            for number, contact in enumerate(contacts, start=1):
                if len(contact) == 3:
                    print(f"\nContact {number}")
                    print("Name :", contact[0])
                    print("Phone:", contact[1])
                    print("Email:", contact[2])

            print("\n====================================")

    except FileNotFoundError:
        print("Contact file not found. Initializing a new file.")
        initialize_file()

    except (OSError, csv.Error) as error:
        print("Error reading contacts:", error)


# Search for a contact by name
def search_contact():
    search_name = input("Enter the name to search: ").strip().lower()

    if not search_name:
        print("Please enter a name to search.")
        return

    try:
        found = False

        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip column headings

            for contact in reader:
                if len(contact) == 3 and search_name in contact[0].lower():
                    print("\nContact found!")
                    print("Name :", contact[0])
                    print("Phone:", contact[1])
                    print("Email:", contact[2])
                    found = True

        if not found:
            print("No matching contact found.")

    except FileNotFoundError:
        print("Contact file not found. Initializing a new file.")
        initialize_file()

    except (OSError, csv.Error) as error:
        print("Error searching contacts:", error)


# Main menu
def main():
    initialize_file()

    while True:
        print("\n================================")
        print("     CONTACT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thank you for using Contact Management System!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()