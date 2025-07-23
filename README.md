

# Full-Featured Calculator Web App

## Overview

A modern, responsive calculator web app built with Streamlit, supporting both basic and advanced mathematical operations, memory functions, and calculation history.

---

## Features

- **Basic Arithmetic:** Addition, Subtraction, Multiplication, Division
- **Advanced Functions:**
  - Square root
  - Power
  - Logarithms (base 10)
  - Trigonometric functions (sin, cos, tan; input in degrees)
- **Memory Functions:**
  - M+ (Add to Memory)
  - M- (Subtract from Memory)
  - MR (Memory Recall)
  - MC (Memory Clear)
- **Calculation History:** View and clear recent calculations
- **Responsive UI:** Works across devices and screen sizes
- **Error Handling:** Handles invalid operations (e.g., division by zero)

---

## Technologies Used

- Python 3.x
- Streamlit
- Standard Python math library

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd full-featured-calculator-python
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run src/app.py
   ```

---

## Usage

- Open the app in your browser at the URL provided by Streamlit (usually `http://localhost:8501`).
- Use the calculator interface for basic and advanced calculations.
- Use memory buttons to store, recall, or clear values.
- View and clear calculation history as needed.

---

## File Structure

```
full-featured-calculator-python/
├── calculator_web.py         # (Optional entry point)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── src/
│   ├── app.py                # Streamlit app UI & logic
│   ├── calculator.py         # Calculator logic
│   ├── memory.py             # Memory functions
│   └── history.py            # History tracking
└── venv/                     # Virtual environment (optional)
```

---

## Notes

- Trigonometric functions expect input in degrees.
- Error messages are shown for invalid operations.
- Future improvements: more advanced functions, theming, export history.

---

## Contact

For questions or feedback, contact [Your Name or Email].
