class LeaveApplication:
    def _init_(self, name, start_date, end_date, reason):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason

    def _str_(self):
        return f"Name: {self.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nReason: {self.reason}"

applications = []

def submit_leave_application():
    name = input("Enter your name: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    reason = input("Enter reason for leave: ")
    application = LeaveApplication(name, start_date, end_date, reason)
    applications.append(application)
    print("Leave application submitted successfully.")

def view_leave_applications():
    if not applications:
        print("No leave applications found.")
    else:
        for idx, application in enumerate(applications, start=1):
            print(f"Application {idx}:")
            print(application)
            print()

while True:
    print("\n1. Submit Leave Application\n2. View Leave Applications\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        submit_leave_application()
    elif choice == '2':
        view_leave_applications()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")