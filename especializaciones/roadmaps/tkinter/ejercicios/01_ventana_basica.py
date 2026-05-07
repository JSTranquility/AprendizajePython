import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Ejercicio 01")
    root.geometry("320x180")
    root.minsize(260, 140)

    tk.Label(root, text="Mi primera ventana Tkinter", font=("Segoe UI", 14)).pack(
        pady=20
    )
    tk.Button(root, text="Cerrar", command=root.destroy).pack()

    root.mainloop()


if __name__ == "__main__":
    main()

