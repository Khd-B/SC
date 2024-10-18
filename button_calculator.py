import streamlit as st
import math

# Initialize session state
if 'current_input' not in st.session_state:
    st.session_state.current_input = ''
if 'operation' not in st.session_state:
    st.session_state.operation = ''
if 'result' not in st.session_state:
    st.session_state.result = ''

def clear():
    st.session_state.current_input = ''
    st.session_state.operation = ''
    st.session_state.result = ''

def press(num):
    st.session_state.current_input += str(num)

def set_operation(op):
    if st.session_state.current_input:
        st.session_state.operation = op
        st.session_state.result = st.session_state.current_input
        st.session_state.current_input = ''

def calculate():
    if st.session_state.result and st.session_state.current_input:
        num1 = float(st.session_state.result)
        num2 = float(st.session_state.current_input)
        if st.session_state.operation == '+':
            st.session_state.result = num1 + num2
        elif st.session_state.operation == '-':
            st.session_state.result = num1 - num2
        elif st.session_state.operation == '*':
            st.session_state.result = num1 * num2
        elif st.session_state.operation == '/':
            st.session_state.result = "Error! Division by zero." if num2 == 0 else num1 / num2
        elif st.session_state.operation == 'Power':
            st.session_state.result = num1 ** num2
        elif st.session_state.operation == 'Square Root':
            st.session_state.result = "Error! Negative number." if num1 < 0 else math.sqrt(num1)
        elif st.session_state.operation == 'Logarithm':
            st.session_state.result = "Error! Logarithm of non-positive number." if num1 <= 0 else math.log(num1)
        elif st.session_state.operation == 'Sine':
            st.session_state.result = math.sin(math.radians(num1))
        elif st.session_state.operation == 'Cosine':
            st.session_state.result = math.cos(math.radians(num1))
        elif st.session_state.operation == 'Tangent':
            st.session_state.result = math.tan(math.radians(num1))
        st.session_state.current_input = ''

def main():
    st.title("Scientific Calculator")

    # Display current input and result
    st.write("Current Input: ", st.session_state.current_input)
    st.write("Result: ", st.session_state.result)

    # Number buttons
    cols = st.columns(3)
    for i in range(1, 10):
        with cols[(i-1) % 3]:
            if st.button(str(i)):
                press(i)

    # Zero button
    if st.button('0'):
        press(0)

    # Operation buttons
    operation_buttons = ['+', '-', '*', '/', 'Power', 'Square Root', 'Logarithm', 'Sine', 'Cosine', 'Tangent']
    cols = st.columns(5)
    for op in operation_buttons:
        with cols[operation_buttons.index(op) % 5]:
            if st.button(op):
                set_operation(op)

    # Equals and Clear buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Calculate'):
            calculate()
    with col2:
        if st.button('Reset'):
            clear()

    # Footnote
    st.markdown("**By KB, thanks to Aspire Pak**")

if __name__ == "__main__":
    main()
