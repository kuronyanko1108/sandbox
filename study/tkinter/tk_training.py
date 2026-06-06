import tkinter as tk
from tkinter import messagebox, filedialog


def show_info():
    messagebox.showinfo("情報", "これはメッセージボックスです！")


def ask_confirm():
    result = messagebox.askyesno("確認", "保存しますか？")
    if result:
        messagebox.showinfo("結果", "ユーザーは「はい」を選択しました")
    else:
        messagebox.showinfo("結果", "ユーザーは「いいえ」を選択しました")


def open_file():
    file_path = filedialog.askopenfilename(title="ファイルを選択")
    if file_path:
        messagebox.showinfo("選択されたファイル", f"選択されたファイル: {file_path}")


def save_file():
    save_path = filedialog.askdirectory(title="保存先を選択")
    if save_path:
        messagebox.showinfo("保存先", f"保存先ディレクトリ: {save_path}")


# ステータス更新処理（１秒ごとに実行）
def update_status():
    global counter
    counter += 1
    status_label.config(text=f"ステータス: {counter}秒経過")
    root.after(1000, update_status)  # 1秒後に再実行


# Tkinterアプリのウィンドウ作成
root = tk.Tk()
root.geometry("400x300")

# ステータスバーの作成
status_bar = tk.Frame(root, relief=tk.RAISED, bd=1)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# ステータス更新用のカウンタ
counter = 0

# ステータスラベルの作成
status_label = tk.Label(status_bar, text="ステータス: 初期状態", anchor="w")
status_label.pack(side=tk.LEFT, padx=20)

root.after(1000, update_status)

# ボタン配置
btn_info = tk.Button(root, text="情報メッセージ", command=show_info)
btn_info.pack(pady=5)

btn_ask_info = tk.Button(root, text="確認ダイアログ", command=ask_confirm)
btn_ask_info.pack(pady=5)

btn_open = tk.Button(root, text="ファイルを開く", command=open_file)
btn_open.pack(pady=5)

btn_save = tk.Button(root, text="保存先を指定する", command=save_file)
btn_save.pack(pady=5)

# 閉じるボタンの作成
close_button = tk.Button(root, text="閉じる", command=root.destroy)
close_button.pack(pady=20)

# メインループ開始
root.mainloop()
