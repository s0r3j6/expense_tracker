import streamlit as st
from datetime import datetime
import expense_tracker as et

st.set_page_config(page_title="EXPENSE TRACKER",layout="centered")

st.title("Personal Expense tracker")

#Add expense section

st.header("➕ Add new expense")

col1, col2 = st.columns(2)


with col1:
    date=st.date_input("Date", datetime.today())
    category=st.selectbox("Category", ["Food","Travel","Shopping","Other"])
with col2:
    amount=st.number_input("Amount",min_value=0.0)
    description=st.text_input("Description")

if st.button("➕ Add Expense"):
    if amount == 0:
        st.warning("Please enter a valid number")
    else:
        msg=et.add_expense(str(date),category,amount,description)
        st.success(msg)
        
#Total Spending
st.header("Total Spending")

total=et.get_total_spending()
st.metric(label="Total Spent", value= f"Euros: {total}")


#VIEW Expenses
st.header("All Expense")

df=et.get_expenses()
if df is not None:
    st.dataframe(df)
    #download button
    csv=df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download data",csv,"expenses.csv","text/csv")
else:
        st.warning("No data found")



#Visualization
st.header("Expense Visualization")

data=et.get_category_summary()
if data is not None:
        col1,col2 = st.columns(2)

        with col1:
             st.subheader("Bar Chart")
             st.bar_chart(data)
        with col2:
             st.subheader("Pie chart")
             st.pyplot(data.plot.pie(autopct='%1.1f%%').figure)
else:
        st.warning("No data to visualize")

