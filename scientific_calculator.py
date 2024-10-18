import streamlit as st
import math

def main():
    st.title("Scientific Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Dropdown menu for operations
    operation = st.selectbox("Select an operation:", [
        '+', '-', '*', '/', 
        'Power', 'Square Root', 'Logarithm', 'Sine', 'Cosine', 'Tangent'
    ])

    # Buttons for calculation and reset
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Calculate"):
            result = calculate(num1, num2, operation)
            st.success(f"The result is: {result}")

    with col2:
        if st.button("Reset"):
            st.experimental_rerun()

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
