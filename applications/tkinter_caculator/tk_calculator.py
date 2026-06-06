import tkinter as tk
from decimal import Decimal

FOUR_ARITHMETIC_OPERATIONS = {"+", "-", "*", "/"}
ZERO = "0"
LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"
DECIMAL_POINT = "."
MINUS = "-"


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(
            master=root, bg="White", width=500, height=300, border=2, relief="raised"
        )
        self.pack()
        self.pack_propagate(0)
        self.root = root
        self.input_values = [ZERO]
        self.output = ""
        self.result_var = tk.StringVar(value=ZERO)

        self.create_widgets()

    # ウィジェット作成
    def create_widgets(self):
        self.create_calc_key_btn()
        self.create_result_var()

    # 計算結果表示作成
    def create_result_var(self):
        self.result_label = tk.Label(
            self,
            textvariable=self.result_var,
            bg="White",
        )
        self.result_label.grid(row=0, column=0, columnspan=4, pady=10)

    # 計算機のボタン作成
    def create_calc_key_btn(self):
        calc_keys = [
            "AC",
            "+/-",
            "%",
            "/",
            "7",
            "8",
            "9",
            "*",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "+",
            "0",
            ".",
            "=",
        ]

        row_idx = 4
        col_idx = 0

        for key in calc_keys:
            self.num_btn = tk.Button(self)
            self.num_btn["command"] = lambda k=key: self.on_click(k)
            self.num_btn["text"] = key

            if key == "0":
                self.num_btn.grid(
                    row=row_idx,
                    column=col_idx,
                    padx=1,
                    pady=1,
                    columnspan=2,
                    sticky="nsew",
                )
                col_idx += 2

            else:
                self.num_btn.grid(
                    row=row_idx, column=col_idx, padx=1, pady=1, sticky="nsew"
                )
                col_idx += 1

            if col_idx >= 4:
                row_idx += 1
                col_idx = 0

    # ボタン押下時の処理
    def on_click(self, key):
        prev_value = self.input_values[-1]

        if key == "=":
            self.output_value = self.trim_trailing_zeros(self.calculation())
            self.input_values.clear()
            self.input_values.append(self.output_value)

        elif key == "AC":
            self.input_values.clear()
            self.input_values.append(ZERO)
            self.output_value = "".join(self.input_values)

        # 入力キーが数字
        elif key.isdigit():
            if prev_value == ZERO and len(self.input_values) == 1:
                self.input_values.pop()

            elif RIGHT_PARENTHESIS in prev_value and LEFT_PARENTHESIS in prev_value:
                prev_num = self.input_values.pop()
                key = (
                    LEFT_PARENTHESIS
                    + self.strip_parentheses(prev_num)
                    + key
                    + RIGHT_PARENTHESIS
                )

            elif prev_value.isdigit() or DECIMAL_POINT in prev_value:
                prev_num = self.input_values.pop()
                key = prev_num + key

            self.input_values.append(key)
            self.output_value = "".join(self.input_values)

        # 入力キーが四則演算子
        elif key in FOUR_ARITHMETIC_OPERATIONS:
            if prev_value in FOUR_ARITHMETIC_OPERATIONS:
                self.input_values.pop()
            elif prev_value[-1] == DECIMAL_POINT:
                self.input_values.pop()
                self.input_values.append(prev_value.rstrip(DECIMAL_POINT))
            self.input_values.append(key)
            self.output_value = "".join(self.input_values)

        # 入力キーが小数点
        elif key == DECIMAL_POINT:
            if DECIMAL_POINT in prev_value:
                return

            if prev_value in FOUR_ARITHMETIC_OPERATIONS:
                key = ZERO + key
            elif prev_value.isdigit():
                prev_num = self.input_values.pop()
                key = prev_num + key
            elif RIGHT_PARENTHESIS in prev_value and LEFT_PARENTHESIS in prev_value:
                prev_num = self.input_values.pop()
                key = (
                    LEFT_PARENTHESIS
                    + self.strip_parentheses(prev_num)
                    + key
                    + RIGHT_PARENTHESIS
                )
            self.input_values.append(key)
            self.output_value = "".join(self.input_values)

        # 入力キーが +/-
        elif key == "+/-":
            if prev_value in FOUR_ARITHMETIC_OPERATIONS:
                return
            else:
                self.input_values.pop()
                self.input_values.append(self.convert_sign_format(prev_value))
                self.output_value = "".join(self.input_values)

        print(self.input_values)
        self.result_var.set(self.output_value)

    # 正負入れ替え処理
    def convert_sign_format(self, number):
        if MINUS in number:
            return self.strip_parentheses(number).strip(MINUS)
        else:
            return LEFT_PARENTHESIS + MINUS + number + RIGHT_PARENTHESIS

    # 括弧の処理を外す処理
    def strip_parentheses(self, value):
        return value.strip(RIGHT_PARENTHESIS).strip(LEFT_PARENTHESIS)

    # 小数点.0のときの小数点以下の０を削除
    def trim_trailing_zeros(self, val):
        if val == val.to_integral_value():
            return str(val.to_integral_value())
        return str(val)

    # 計算処理
    def calculation(self):
        # 入力値を逆ポーランド記法に変換する
        expression = self.convert_infix_to_postfix(self.input_values)

        numbers = []

        for val in expression:
            if val.isdigit() or any(v.isdigit() for v in val):
                numbers.append(Decimal(val))
            else:
                num2 = numbers.pop()
                num1 = numbers.pop()

                if val == "+":
                    n = num1 + num2
                elif val == "-":
                    n = num1 - num2
                elif val == "*":
                    n = num1 * num2
                elif val == "/":
                    n = num1 / num2
                numbers.append(n)

        ans = numbers.pop()
        return ans

    # 中置記法を逆ポーランド記法に変換
    def convert_infix_to_postfix(self, expression):
        postfix = []
        operators = []

        for e in expression:
            if RIGHT_PARENTHESIS in e and LEFT_PARENTHESIS in e:
                e = self.strip_parentheses(e)

            if e.isdigit() or any(v.isdigit() for v in e):
                postfix.append(e)

            elif not operators:
                operators.append(e)

            else:
                for o in reversed(operators):
                    if e in ("*", "/") and o in ("+", "-"):
                        break
                    else:
                        ope = operators.pop()
                        postfix.append(ope)

                operators.append(e)

        while operators:
            ope = operators.pop()
            postfix.append(ope)

        return postfix


root = tk.Tk()
root.title("tkinter-calculator")
root.geometry("200x230")

app = Application(root=root)

app.mainloop()
