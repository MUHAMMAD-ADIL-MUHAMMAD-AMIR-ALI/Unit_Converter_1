import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    # Conversion logic
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "Conversion not supported!"

def main():
    st.title("Unit Converter")
    st.write("Welcome to the unit converter!")

    # Input from the user using Streamlit widgets
    value = st.number_input("Enter the value you want to convert:", value=1.0)
    unit_from = st.selectbox("Select the unit to convert from:", ["meters", "kilometers", "grams", "kilograms"])
    unit_to = st.selectbox("Select the unit to convert to:", ["meters", "kilometers", "grams", "kilograms"])

    if st.button("Convert"):
        # Call the conversion function
        result = convert_units(value, unit_from, unit_to)
        st.write(f"Converted value is: {result}")

if __name__ == "__main__":
    main()

st.markdown("---")
st.write("MUHAMMAD ADIL AMIR ALI")
st.write("Roll number 8286")