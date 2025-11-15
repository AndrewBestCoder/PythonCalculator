from Calculator import Calculator
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    calc.set_calculator_visual()
    calc.run()
