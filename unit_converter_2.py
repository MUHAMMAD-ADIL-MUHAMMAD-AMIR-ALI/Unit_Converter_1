import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    # Length Conversion
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "miles" and unit_to == "kilometers":
        return value * 1.60934
    elif unit_from == "kilometers" and unit_to == "miles":
        return value * 0.621371

    # Time Conversion
    elif unit_from == "seconds" and unit_to == "minutes":
        return value / 60
    elif unit_from == "minutes" and unit_to == "seconds":
        return value * 60
    elif unit_from == "hours" and unit_to == "minutes":
        return value * 60
    elif unit_from == "minutes" and unit_to == "hours":
        return value / 60

    # Area Conversion
    elif unit_from == "square meters" and unit_to == "square kilometers":
        return value / 1_000_000
    elif unit_from == "square kilometers" and unit_to == "square meters":
        return value * 1_000_000
    elif unit_from == "square feet" and unit_to == "square meters":
        return value * 0.092903
    elif unit_from == "square meters" and unit_to == "square feet":
        return value * 10.7639

    # Temperature Conversion
    elif unit_from == "celsius" and unit_to == "fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "fahrenheit" and unit_to == "celsius":
        return (value - 32) * 5/9
    elif unit_from == "celsius" and unit_to == "kelvin":
        return value + 273.15
    elif unit_from == "kelvin" and unit_to == "celsius":
        return value - 273.15
    else:
        return "Conversion not supported!"

def main():
    st.title("Unit Converter")
    st.write("Welcome to the unit converter!")
    st.markdown("---")

    st.subheader("Enter values for conversion:")   
    conversion_type = st.selectbox(
        "Select conversion type:",
        ["Length","Time", "Area", "Temperature"]
    )
               
    value = st.number_input("value:", value = 1.0)

    unit_from = ""
    unit_to = ""

    if conversion_type == "Length":
        unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "miles"])
        unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "miles"])
    elif conversion_type == "Time":
        unit_from = st.selectbox("Convert from:", ["seconds", "minutes", "hours"])
        unit_to = st.selectbox("Convert to:", ["seconds", "minutes", "hours"])
    elif conversion_type == "Area":
        unit_from = st.selectbox("Convert from:", ["square meters", "square kilometers", "square feet"])
        unit_to = st.selectbox("Convert to:", ["square meters", "square kilometers", "square feet"])
    elif conversion_type == "Temperature":
        unit_from = st.selectbox("Convert from:", ["celsius", "fahrenheit", "kelvin"])
        unit_to = st.selectbox("Convert to:", ["celsius", "fahrenheit", "kelvin"])

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write(f"Converted value is: {result}")

if __name__ == "__main__":
    main()

st.markdown("---")
st.write("MUHAMMAD ADIL AMIR ALI")
st.write("Roll number 8286")