# Dictionary to store leave types and their codes
leave_types = {
    "Annual": "AN",
    "Sick": "SK",
    "Maternity": "MT",
    "Paternity": "PT",
    "Bereavement": "BR"
}

# Function to display leave types and their codes
def display_leave_types():
    print("Leave Types:")
    for leave_type, code in leave_types.items():
        print(f"{leave_type}: {code}")

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. Display leave types and codes")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_leave_types()
    elif choice == "2":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
