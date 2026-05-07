import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Canvas")
    root.geometry("500x360")

    color = tk.StringVar(value="black")

    barra = tk.Frame(root, padx=8, pady=8)
    barra.pack(fill="x")

    for nombre, valor in [("Negro", "black"), ("Rojo", "red"), ("Azul", "blue")]:
        tk.Radiobutton(barra, text=nombre, value=valor, variable=color).pack(side="left")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True)

    def dibujar(evento):
        radio = 4
        canvas.create_oval(
            evento.x - radio,
            evento.y - radio,
            evento.x + radio,
            evento.y + radio,
            fill=color.get(),
            outline=color.get(),
        )

    canvas.bind("<B1-Motion>", dibujar)
    root.mainloop()


if __name__ == "__main__":
    main()

