import pandas as pd
#from datetime import datetime
#import matplotlib.pyplot as plt

FILE_NAME="expenses.csv"

#ADD EXPENSES

def add_expense(date, category, amount, description):

   # date=input("Enter date(YYYY-MM-DD) or press enter for today: ")

   # if date == "":
    #    date = datetime.today().strftime('%Y-%m-%d')
    
   # category = input("Enter Category (Food,Travel,shopping,etc): ")
   # amount = float(input("Enter the amount: "))
   # description = input("enter description: ")
    if not category:
        category = "Other"
    new_data = {
        "Date": [date],
        "Category": [category],
        "Amount": [amount],

        "Description": [description]
    }
    
    df = pd.DataFrame(new_data)

    try:
        old_df = pd.read_csv(FILE_NAME)
        df= pd.concat([old_df,df],ignore_index=True)
    except(FileNotFoundError,pd.errors.EmptyDataError):
        pass

    df.to_csv(FILE_NAME,index=False)
    return "Expense added successfully!"

#GET EXPENSES
def get_expenses():
    try:
        df=pd.read_csv(FILE_NAME)
        df = df.sort_values(by="Date", ascending=False)
        return df
    except:
        return None

#VIEW EXPENSES

#def view_expenses():
 #   try:
  #      df=pd.read_csv(FILE_NAME)
   #     print(df)
    #except FileNotFoundError:
     #   print("No expenses found yet")

#TOTAL SPENDING

def get_total_spending():
    try:
        df=pd.read_csv(FILE_NAME)
        return df["Amount"].sum()
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return 0

#VISUALZATION

def get_category_summary():
    try:
        df = pd.read_csv(FILE_NAME)
        return df.groupby("Category")["Amount"].sum()
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return None
    
def filter_by_category(category):
    try:
        df = pd.read_csv(FILE_NAME)
        return df[df["Category"] == category]
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return None

#filter by date range

def filter_by_date(start_date,end_date):
    try: 
        df=pd.read_csv(FILE_NAME)
        df["Date"] = pd.to_datetime(df["Date"])
        return df[(df["Date"]>= start_date)&(df["Date"]<= end_date)]
    except (FileNotFoundError,pd.errors.EmptyDataError):
        return None


         