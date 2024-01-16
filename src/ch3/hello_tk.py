import tkinter as tk

# ボタンを押した時に実行する処理 --- (*1)
def show_message():
    txt.insert('1.0','穏やかな舌は命の木であり\n')
    txt.insert('end','悪意ある言葉は人を落胆させる')

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.geometry('300x200')

# ボタンを作成 --- (*3)
btn = tk.Button(win, text='格言表示', command=show_message)
btn.pack() # ウィンドウに配置

# テキストボックスを作成 --- (*4)
txt = tk.Text(win)
txt.pack()

# メインループを開始 --- (*5)
win.mainloop()

