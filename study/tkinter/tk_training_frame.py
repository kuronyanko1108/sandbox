import tkinter as tk
from tkinter import Scale, HORIZONTAL, Frame, Button, Label, messagebox

# メインウィンドウの設定
root = tk.Tk()
root.geometry("500x300")

# メインフレーム
main_frame = Frame(root, bg="lightgray")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# スケール
scale = Scale(main_frame, from_=0, to=100, orient=HORIZONTAL)
scale.pack(pady=10)

# ラベル（スケールの値を表示）
value_label = Label(main_frame, text="スケールの値: 0", bg="lightgray")
value_label.pack()

# ボタンフレーム
button_frame = Frame(main_frame, bg="white", width=200, height=100)
button_frame.pack(pady=10, fill="both", expand=True)


# フレーム内にボタン配置
def on_button_click():
    messagebox.showinfo("スケールの値", f"現在の値: {scale.get()}")


button = Button(button_frame, text="クリック", command=on_button_click)
button.pack(pady=20)


# スケールの値をラベルに反映する関数
def update_label(value):
    value_label.config(text=f"スケールの値 :{value}")


scale.config(command=update_label)

# メインループの開始
root.mainloop()
