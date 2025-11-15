import tkinter as tk
from enum import Enum
from typing import Callable


class ButtonsLabels(Enum):
    C = "C"
    DEL = "DEL"
    MULTIPLY = "*"
    EQUAL = "="
    ONE = "1"
    TWO = "2"
    THREE = "3"
    DIVIDE = "/"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    PLUS = "+"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    MINUS = "-"
    OPEN_BRACKET = "("
    ZERO = "0"
    CLOSE_BRACKET = ")"
    POWER = "X^2"


class Calculator:
    def __init__(self, root_tk: tk.Tk, background_color: str = "#000") -> None:
        self.calc_visual = CalculatorVisual(root_tk, controller=self)
        self.root = root_tk
        self.formula = "0"
        self.error_message = ""

    def set_calculator_visual(self) -> None:
        self.calc_visual.set_calculator_frame()

    def button_pressed(self, operation: ButtonsLabels) -> None:
        self.error_message = ""
        match operation:
            case ButtonsLabels.C:
                self.formula = "0"
            case ButtonsLabels.DEL:
                self.formula = self.formula[:-1]
            case ButtonsLabels.POWER:
                result, error = CalculatorCalculation.calculate_power_string(
                    self.formula
                )
                if error != "":
                    self.error_message = error
                else:
                    self.formula = result
            case ButtonsLabels.EQUAL:
                result, error = CalculatorCalculation.calculate_string(self.formula)
                if error != "":
                    self.error_message = error
                else:
                    self.formula = result
            case ButtonsLabels.PLUS:
                if self.formula[-1] != "+":
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation.value
            case ButtonsLabels.MINUS:
                if self.formula[-1] != "-":
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation.value
            case ButtonsLabels.MULTIPLY:
                if self.formula[-1] != "*":
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation.value
            case ButtonsLabels.DIVIDE:
                if self.formula[-1] != "/":
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation.value
            case _:
                if self.formula == "0":
                    self.formula = ""
                self.formula += operation.value

        self.calc_visual.update(self.formula, self.error_message)

    def run(self) -> None:
        self.root.mainloop()


class CalculatorVisual:
    def __init__(
        self, root_tk: tk.Tk, controller: Calculator, background_color: str = "#000"
    ) -> None:
        self.root = root_tk
        self.controller = controller
        self.bg = background_color

        self.formula = "0"
        self.error_message = ""

        self.formula_label: tk.Label
        self.error_label: tk.Label

        self.buttons_labels = ButtonsLabels

    def set_calculator_frame(self) -> None:
        self.root.title("Calculator")
        self.root.geometry("485x510")
        self.root.resizable(False, False)
        self.root["bg"] = self.bg

        self.formula_label = tk.Label(
            self.root,
            text=self.formula,
            font=("Times New Roman", 21, "bold"),
            bg=self.bg,
            fg="#FFF",
        )
        self.formula_label.place(x=11, y=30)

        self.error_label = tk.Label(
            self.root,
            text=self.error_message,
            font=("Times New Roman", 12, "normal"),
            bg=self.bg,
            fg="#FFF",
        )
        self.error_label.place(x=11, y=70)

        x, y = 10, 100
        for bt in self.buttons_labels:
            # com = lambda x=bt: self.button_press(x)
            tk.Button(
                self.root,
                text=bt.value,
                bg="#FFF",
                font=("Times New Roman", 15),
                command=self.make_handler(bt),
            ).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def make_handler(self, value: ButtonsLabels) -> Callable[[], None]:
        return lambda: self.controller.button_pressed(value)

    def update(self, formula: str, error_message: str = "") -> None:
        if formula == "":
            self.formula = "0"
            self.formula_label.config(text=self.formula)
        else:
            self.formula_label.config(text=formula)
        self.error_label.config(text=error_message)


class CalculatorCalculation:
    @staticmethod
    def calculate_string(formula: str) -> tuple[str, str]:
        try:
            value = eval(formula)
            if abs(value) > 1e10:
                return "", "Too large"
        except (SyntaxError, TypeError):
            return "", "Syntax error"
        except ZeroDivisionError:
            return "", "Zero division error"

        return str(eval(formula)), ""

    @staticmethod
    def calculate_power_string(formula: str) -> tuple[str, str]:
        try:
            value = eval(formula)
            if abs(value) > 1e10:
                return "", "Too large"
        except (SyntaxError, TypeError):
            return "", "Syntax error"
        except ZeroDivisionError:
            return "", "Zero division error"

        return str(eval(formula) ** 2), ""


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    calc.set_calculator_visual()
    calc.run()
