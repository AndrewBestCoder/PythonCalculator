from tkinter import *

class Calculator:
    def __init__(self): #Что означает __init__ нижние подчеркивания?
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("485x510")
        self.bg = "#999"
        self.root["bg"] = self.bg
        self.root.resizable(False, False)

        self.formula = "0"
        self.errormessage = ""

        self.lbl = Label(self.root, text = self.formula, font = ("Times New Roman", 21, "bold"), bg = self.bg, fg = "#FFF")
        self.lbl.place(x = 11, y = 30)

        self.erlbl = Label(self.root, text = self.errormessage, font = ("Times New Roman", 12, "normal"), bg = self.bg, fg = "#FFF")
        self.erlbl.place(x = 11, y = 70)

        buttons = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x, y = 10, 100
        for bt in buttons:
            com = lambda x = bt: self.Calculate(x)
            Button(self.root, text=bt, bg="#FFF", font=("Times New Roman", 15),
                   command=com).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81


    def Calculate(self, operation):
        try:
            self.errormessage = ""
            match operation:
                case "C":
                    self.formula = "0"
                case "DEL":
                    self.formula = self.formula[:-1]
                case "X^2":
                    value = eval(self.formula)
                    if abs(value) > 1e10:
                        self.errormessage = "Too large"
                    else:
                        self.formula = str((eval(self.formula)) ** 2)
                case "=":
                    value = eval(self.formula)
                    if abs(value) > 1e10:
                        self.errormessage = "Too large"
                    else:
                        self.formula = str(eval(self.formula))
                case "+":
                    if self.formula[-1] != "+":
                        if self.formula == "0":
                            self.formula = ""
                        self.formula += operation
                case "-":
                    if self.formula[-1] != "-":
                        if self.formula == "0":
                            self.formula = ""
                        self.formula += operation
                case "*":
                    if self.formula[-1] != "*":
                        if self.formula == "0":
                            self.formula = ""
                        self.formula += operation
                case "/":
                    if self.formula[-1] != "/":
                        if self.formula == "0":
                            self.formula = ""
                        self.formula += operation
                case _:
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation
        except (SyntaxError, TypeError):
            self.errormessage = "Syntax Error"
        except ZeroDivisionError:
            self.errormessage = "Zero Division Error"
        self.Update()

    def Update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.config(text = self.formula)
        self.erlbl.config(text = self.errormessage)

    def Run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.Run()