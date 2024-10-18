import streamlit as st
import math

def main():
    st.title("Scientific Calculator")

    # Session state for inputs
    if 'num1' not in st.session_state:
        st.session_state.num1 = 0.0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 0.0
    if 'operation' not in st.session_state:
        st.session_state.operation = '+'

    # Input fields for numbers
    st.session_state.num1 = st.number_input("Enter the first number:", value=st.session_state.num1)
    st.session_state.num2 = st.number_input("Enter the second number:", value=st.session_state.num2)

    # Dropdown menu for operations
    st.session_state.operation = st.selectbox("Select an operation:", [
        '+', '-', '*', '/', 
        'Power', 'Square Root', 'Logarithm', 'Sine', 'Cosine', 'Tangent'
    ], index=0)

    # Calculate result
    if st.button("Calculate"):
        result = calculate(st.session_state.num1, st.session_state.num2, st.session_state.operation)
        st.success(f"The result is: {result}")

    # Clear button
    if st.button("Clear"):
        st.session_state.num1 = 0.0
        st.session_state.num2 = 0.0
        st.session_state.operation = '+'

    # Footnote
    st.markdown("**By KB, thanks to Aspire Pak**")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return "Error! Division by zero." if num2 == 0 else num1 / num2
    elif operation == 'Power':
        return num1 ** num2
    elif operation == 'Square Root':
        return "Error! Negative number." if num1 < 0 else math.sqrt(num1)
    elif operation == 'Logarithm':
        return "Error! Logarithm of non-positive number." if num1 <= 0 else math.log(num1)
    elif operation == 'Sine':
        return math.sin(math.radians(num1))
    elif operation == 'Cosine':
        return math.cos(math.radians(num1))
    elif operation == 'Tangent':
        return math.tan(math.radians(num1))

if __name__ == "__main__":
    main()
