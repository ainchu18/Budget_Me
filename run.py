import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('salary_budget')

def get_monthly_data():
    """
    Get users monthly salary and expenses.
    """
    while True:
        print("Please enter your monthly salary and expenses.")
        print("This should be 4 numbers separated by commas. Write salary first, rent second, food third, extras fourth.")
        print("Example: 4000,550,200,100\n")

        monthly_salary_expenses = input("Enter your monthly salary and expenses here:\n")

        salary_expenses_data = monthly_salary_expenses.split(",")
    
        if validate_figures(salary_expenses_data):
            print("Values entered are valid!\n")
            break
    
    return salary_expenses_data

def validate_figures(values):
    """
    This function will convert all strings to integeres.
    Raises a ValueError if the string cannot be converted to integer,
    or if there are not exactly 4 values entered by the user.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"You need to enter exactly 4 values, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Incorrect data! {e}, please try again.\n")
        return False

    return True

def update_salary_expenses_worksheet(monthly_data):
    """
    This function updates the monthly salary and expenses worksheet.
    Add new row with the list data provided by the user.
    """
    print("Updating salary expenses worksheet... Please stand by!\n")
    salary_expenses_worksheet = SHEET.worksheet("salary_expenses")
    salary_expenses_worksheet.append_row(monthly_data)
    print("Salary expenses worksheet updated successfully!\n")

monthly_data = get_monthly_data()
salary_expenses_data = [int(num) for num in monthly_data]
update_salary_expenses_worksheet(salary_expenses_data)