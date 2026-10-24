📒 Contact Management System Using Python

📌 Project Overview

The Contact Management System is a beginner-friendly Python mini project developed using file handling concepts. It allows users to add, view, and search contact records. The contact details are stored permanently in a CSV file.

This project demonstrates the practical use of Python file handling, CSV operations, functions, and exception handling.

🎯 Objectives

- To understand file handling in Python.
- To store and retrieve contact information using CSV files.
- To implement operations such as adding, viewing, and searching records.
- To handle file-related errors and invalid user inputs.
- To develop a simple menu-driven application.

✨ Features

- Add Contact: Add a contact's name, phone number, and email address.
- View Contacts: Display all saved contact records.
- Search Contact: Search for contacts by name.
- CSV File Storage: Save contact details in a CSV file.
- Exception Handling: Handle missing files and other basic errors.
- Interactive Menu: Navigate through the program using simple menu options.

🛠️ Technologies Used

- Python 3
- CSV Module
- File Handling
- Exception Handling
- Visual Studio Code (VS Code)

📂 Project Structure

Contact-Management-System/
│
├── contact_manager.py
├── contacts.csv
└── README.md

File descriptions:

- "contact_manager.py" — Contains the main Python program.
- "contacts.csv" — Stores contact records and is created automatically when the program runs.
- "README.md" — Provides information about the project.

⚙️ Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible code editor.

Note: No external Python libraries are required because the project uses built-in modules.

🚀 How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal by selecting Terminal → New Terminal.
4. Run the following command:

python contact_manager.py

If the command does not work on Windows, try:

py contact_manager.py

5. Choose an option from the menu displayed in the terminal.
6. Follow the instructions to add, view, or search contacts.

🖥️ Sample Output

================================
     CONTACT MANAGEMENT SYSTEM
================================
1. Add Contact
2. View Contacts
3. Search Contact
4. Exit
================================
Enter your choice (1-4): 1

Enter name: Afsha
Enter phone number: 9876543210
Enter email address: afsha@example.com

Contact added successfully!

Searching for a Contact

Enter your choice (1-4): 3
Enter the name to search: Afsha

Contact found!
Name : Afsha
Phone: 9876543210
Email: afsha@example.com

The sample outputs are illustrative. Actual results depend on the information entered by the user.

📚 Python Concepts Demonstrated

- Functions and modular programming
- Conditional statements
- Loops
- User input and output
- File creation, reading, and writing
- CSV file operations
- Exception handling using "try-except"
- Searching records

🔮 Future Enhancements

- Update existing contact details.
- Delete unwanted contacts.
- Prevent duplicate contact entries.
- Validate phone numbers and email addresses.
- Add a graphical user interface (GUI).
