import tkinter as tk
from tkinter import messagebox, ttk

# Tkinterアプリのウィンドウ作成
root = tk.Tk()
root.geometry("600x500")


# ラジオボタン
var = tk.IntVar()
tk.Label(root, text="好きな選択肢を選んで下さい").pack()
radiobutton1 = tk.Radiobutton(root, text="選択肢１", variable=var, value=1)
radiobutton2 = tk.Radiobutton(root, text="選択肢２", variable=var, value=2)
radiobutton1.pack()
radiobutton2.pack()


def show_radio_selection():
    messagebox.showinfo("選択結果", f"選ばれた値: {var.get()}")


ttk.Button(root, text="ラジオボタン確認", command=show_radio_selection).pack(pady=10)

# リストボックス
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

options = ["選択肢1", "選択肢2", "選択肢3"]
for i, option in enumerate(options, 1):
    listbox.insert(i, option)


def show_list_selection():
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_indices]
    messagebox.showinfo("選択結果", f"選ばれた項目: {', '.join(selected_values)}")


ttk.Button(root, text="リストボックス確認", command=show_list_selection).pack(pady=10)

# コンボボックス
ttk.Label(root, text="選択肢を選ぶか入力してください").pack()
combobox = ttk.Combobox(root, values=options)
combobox.pack()


def show_combo_selection():
    messagebox.showinfo("選択結果", f"選ばれた値: {combobox.get()}")


ttk.Button(root, text="コンボボックス確認", command=show_combo_selection).pack()

# メインループ開始
root.mainloop()
