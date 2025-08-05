
def convert_temperature(temp, unit):
    if unit.upper() == 'F':
        return round((temp - 32) * 5/9, 2)
    elif unit.upper() == 'C':
        return round((temp * 9/5) + 32, 2)
    else:
        return "Invalid unit"


import streamlit as st

st.title("Temperature Converter")

temp = st.number_input("Enter temperature:")
unit = st.selectbox("Select the input unit:", ['C', 'F'])

if st.button("Convert"):
    result = convert_temperature(temp, unit)
    st.success(f"Converted Temperature: {result}")
