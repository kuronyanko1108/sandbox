import tkinter as tk
from tkinter import Scale, HORIZONTAL, Button, Label, messagebox

# 　メインウィンドウの設定
root = tk.Tk()
root.title("Scale and frame Example")
root.geometry("400x300")

# スケール
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale.pack(pady=10)

# ラベル（スケールの値を表示）
value_label = Label(root, text="スケールの値: 0")
value_label.pack(pady=5)


# フレーム内にボタン配置
def on_button_click():
    messagebox.showinfo("スケールの値", f"現在の値: {scale.get()}")


button = Button(root, text="クリック", command=on_button_click)
button.pack(pady=20)


# スケールの値をラベルに反映する関数
def update_label(value):
    value_label.config(text=f"スケールの値: {value}")


scale.config(command=update_label)

# メインループの開始
root.mainloop()
