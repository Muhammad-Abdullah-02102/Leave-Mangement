# Initialize leave balances
leave_balances = {
    'sick_leave': 10,
    'vacation_leave': 15,
    'personal_leave': 5
}

# Function to check leave balance
def check_leave_balance(leave_type):
    if leave_type in leave_balances:
        return leave_balances[leave_type]
    else:
        return 'Leave type not found'

# Function to take leave
def take_leave(leave_type, days):
    if leave_type in leave_balances:
        if leave_balances[leave_type] >= days:
            leave_balances[leave_type] -= days
            return f'{days} days {leave_type} taken. Remaining {leave_type} balance: {leave_balances[leave_type]}'
        else:
            return f'Insufficient {leave_type} balance. Available balance: {leave_balances[leave_type]}'
    else:
        return 'Leave type not found'

# Example usage
print(check_leave_balance('sick_leave'))  # Output: 10
print(take_leave('sick_leave', 3))         # Output: 3 days sick_leave taken. Remaining sick_leave balance: 7
print(take_leave('vacation_leave', 20))    # Output: Insufficient vacation_leave balance. Available balance: 15
print(take_leave('unpaid_leave', 5))        # Output: Leave type not found
