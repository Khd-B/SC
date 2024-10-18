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

    # Reset button
    if st.button("Reset"):
        st.experimental_rerun()

    # Calculate the result based on the selected operation
    if st.button("Calculate"):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        elif operation == 'Power':
            result = num1 ** num2
        elif operation == 'Square Root':
            result = math.sqrt(num1) if num1 >= 0 else "Error! Negative number."
        elif operation == 'Logarithm':
            result = math.log(num1) if num1 > 0 else "Error! Logarithm of non-positive number."
        elif operation == 'Sine':
            result = math.sin(math.radians(num1))
        elif operation == 'Cosine':
            result = math.cos(math.radians(num1))
        elif operation == 'Tangent':
            result = math.tan(math.radians(num1))

        st.success(f"The result is: {result}")

    # Footnote
    st.markdown("**By KB, thanks to Aspire Pakistan**")

if __name__ == "__main__":
    main()
