import streamlit as st
from forex_python.converter import CurrencyRates

# Custom Styles for Advanced UI
st.markdown("""
    <style>
        body { background-color: #0e0e0e; color: white; font-family: 'Poppins', sans-serif; }
        .stApp { background-color: #0e0e0e; }
        .stSidebar { background-color: #141414; color: white; }
        .stButton > button { background-color: #ff4757; color: white; border-radius: 10px; font-size: 18px; }
        .stSelectbox, .stTextInput, .stNumberInput { background-color: #222; color: white; border-radius: 8px; }
        .title { color: #f1c40f; text-align: center; font-size: 40px; font-weight: bold; text-shadow: 2px 2px #ff4757; }
        .convert-box { background-color: #222; padding: 20px; border-radius: 12px; box-shadow: 0px 0px 15px #ff4757; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">⚡ Multi-Unit Converter</p>', unsafe_allow_html=True)
st.write("Convert Length, Weight, Temperature & Currency in Real-Time!")

# Sidebar Navigation
option = st.sidebar.radio("Select a Conversion Type", ("📏 Length", "⚖️ Weight", "🌡 Temperature", "💰 Currency"))

# Conversion Boxes
st.markdown('<div class="convert-box">', unsafe_allow_html=True)

# Length Converter
if option == "📏 Length":
    st.subheader("📏 Length Converter")
    length_units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Feet": 0.3048, "Inches": 0.0254, "Miles": 1609.34}
    from_unit = st.selectbox("From:", list(length_units.keys()))
    to_unit = st.selectbox("To:", list(length_units.keys()))
    value = st.number_input("Enter Value:", min_value=0.0, step=0.1)
    
    if st.button("Convert 🔄"):
        result = (value * length_units[from_unit]) / length_units[to_unit]
        st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

# Weight Converter
elif option == "⚖️ Weight":
    st.subheader("⚖️ Weight Converter")
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    from_unit = st.selectbox("From:", list(weight_units.keys()))
    to_unit = st.selectbox("To:", list(weight_units.keys()))
    value = st.number_input("Enter Value:", min_value=0.0, step=0.1)
    
    if st.button("Convert 🔄"):
        result = (value * weight_units[from_unit]) / weight_units[to_unit]
        st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

# Temperature Converter
elif option == "🌡 Temperature":
    st.subheader("🌡 Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", temp_units)
    to_unit = st.selectbox("To:", temp_units)
    value = st.number_input("Enter Value:", step=0.1)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    if st.button("Convert 🔄"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {round(result, 2)} {to_unit}")

# Currency Converter
elif option == "💰 Currency":
    st.subheader("💰 Currency Converter")
    c = CurrencyRates()
    currencies = ["USD", "EUR", "GBP", "PKR", "INR", "JPY", "CNY", "CAD", "AUD"]
    from_currency = st.selectbox("From Currency:", currencies)
    to_currency = st.selectbox("To Currency:", currencies)
    amount = st.number_input("Enter Amount:", min_value=0.0, step=1.0)

    if st.button("Convert 🔄"):
        result = c.convert(from_currency, to_currency, amount)
        st.success(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")

st.markdown('</div>', unsafe_allow_html=True)


