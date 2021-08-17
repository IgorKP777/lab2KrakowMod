from datetime import datetime
import tkinter as tk


def update():
    clock.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('+900+850')
    clock = tk.Label(root, font=('caviar dreams', 130), bg='black', fg='white')
    clock.pack()
    update()
    root.mainloop(0)
