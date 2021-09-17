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

def get_salary_data():
    """
    Get users monthly salary.
    """
    print("Please enter your monthly salary.")
    print("This should be a number with no decimal point.")
    print("Example: 1000,2000,3000,4000\n")

    monthly_salary = input("Enter your salary here:\n")
    print(f"Your salary this month is {monthly_salary}")

get_salary_data()