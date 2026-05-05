import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Contador")
    root.geometry("300x180")

    contador = tk.IntVar(value=0)

    def cambiar(delta):
        contador.set(contador.get() + delta)

    tk.Label(root, textvariable=contador, font=("Segoe UI", 28)).pack(pady=20)

    botones = tk.Frame(root)
    botones.pack()

    tk.Button(botones, text="-", width=8, command=lambda: cambiar(-1)).grid(
        row=0, column=0, padx=4
    )
    tk.Button(botones, text="+", width=8, command=lambda: cambiar(1)).grid(
        row=0, column=1, padx=4
    )
    tk.Button(root, text="Reiniciar", command=lambda: contador.set(0)).pack(pady=10)

    root.bind("<Left>", lambda evento: cambiar(-1))
    root.bind("<Right>", lambda evento: cambiar(1))
    root.mainloop()


if __name__ == "__main__":
    main()

