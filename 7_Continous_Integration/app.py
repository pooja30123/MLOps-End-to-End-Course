import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cude, and fifth power.")

# Get user input 
n = st.number_input("Enter an integer",value=1, step=1)

#Calculate result
sq = n**2
cube = n**3
fifth_power = n**5 

# Display the result
st.write(f"the square of {n} is : {sq}")
st.write(f"The Cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")