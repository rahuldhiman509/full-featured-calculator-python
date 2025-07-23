import streamlit as st
from src.calculator import Calculator
from src.memory import Memory
from src.history import History

st.set_page_config(page_title="Full-Featured Calculator", page_icon="🧮")
st.title("🧮 Full-Featured Calculator")

st.markdown("""
### 🧠 Features Included:
- Basic arithmetic operations (Add, Subtract, Multiply, Divide)
- Advanced functions (Square root, Power, Log, Trigonometry)
- Memory functions (M+, M-, MR, MC)
- Calculation history
""")

calc = Calculator()
mem = Memory()
hist = History()

operation = st.selectbox("Choose Operation", [
    "Add", "Subtract", "Multiply", "Divide",
    "Square Root", "Power", "Log10",
    "Sine", "Cosine", "Tangent"
])

with st.container():
    if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
        col1, col2 = st.columns([1,1])
        with col1:
            num1 = st.number_input("Enter first number", key="num1")
        with col2:
            num2 = st.number_input("Enter second number", key="num2")
    else:
        num1 = st.number_input("Enter number", key="num1")
        num2 = None

calc_button = st.button("Calculate")

if calc_button:
    try:
        if operation == "Add":
            result = calc.add(num1, num2)
        elif operation == "Subtract":
            result = calc.subtract(num1, num2)
        elif operation == "Multiply":
            result = calc.multiply(num1, num2)
        elif operation == "Divide":
            result = calc.divide(num1, num2)
        elif operation == "Square Root":
            result = calc.sqrt(num1)
        elif operation == "Power":
            result = calc.power(num1, num2)
        elif operation == "Log10":
            result = calc.log10(num1)
        elif operation == "Sine":
            result = calc.sin(num1)
        elif operation == "Cosine":
            result = calc.cos(num1)
        elif operation == "Tangent":
            result = calc.tan(num1)
        st.success(f"Result: {result}")
        hist.add(f"{operation} → {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()

st.subheader("🧠 Memory")
mcols = st.columns(4)
with mcols[0]:
    if st.button("M+", help="Add to memory"):
        mem.add(num1)
with mcols[1]:
    if st.button("M-", help="Subtract from memory"):
        mem.subtract(num1)
with mcols[2]:
    if st.button("MR", help="Recall memory"):
        st.info(f"Memory: {mem.recall()}")
with mcols[3]:
    if st.button("MC", help="Clear memory"):
        mem.clear()
        st.success("Memory cleared")

st.divider()
st.subheader("📜 History")
history_items = hist.get_last(10)
if history_items:
    for item in history_items:
        st.code(item)
    if st.button("Clear History"):
        hist.clear()
else:
    st.info("No history yet. Perform a calculation.")
