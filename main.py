import platform
import psutil
import tkinter as tk


class MeuPC:
    def __init__(self, root):
        self.root = root
        root.title("CPU-Z")

        self.lbl_system = tk.Label(root, text="Sistema:")
        self.lbl_system.grid(row=0, column=0, sticky="w")
        self.txt_system = tk.Entry(root, state="readonly", disabledbackground="white", disabledforeground="black")
        self.txt_system.grid(row=0, column=1)

        self.lbl_processor = tk.Label(root, text="Processor:")
        self.lbl_processor.grid(row=2, column=0, sticky="w")
        self.txt_processor = tk.Entry(root, state="readonly", disabledbackground="white", disabledforeground="black")
        self.txt_processor.grid(row=2, column=1)

        self.lbl_memory = tk.Label(root, text="Memory:")
        self.lbl_memory.grid(row=3, column=0, sticky="w")
        self.txt_memory = tk.Entry(root, state="readonly", disabledbackground="white", disabledforeground="black")
        self.txt_memory.grid(row=3, column=1)

        self.lbl_python = tk.Label(root, text="Python Version:")
        self.lbl_python.grid(row=4, column=0, sticky="w")
        self.txt_python = tk.Entry(root, state="readonly", disabledbackground="white", disabledforeground="black")
        self.txt_python.grid(row=4, column=1)

        self.update_info()

    def update_info(self):
        system = platform.system()
        processor = platform.processor()
        memory = psutil.virtual_memory().total / (1024 ** 3)
        python_version = platform.python_version()

        self.txt_system.config(state="normal")
        self.txt_system.delete(0, tk.END)
        self.txt_system.insert(0, system)
        self.txt_system.config(state="readonly")


        self.txt_processor.config(state="normal")
        self.txt_processor.delete(0, tk.END)
        self.txt_processor.insert(0, processor)
        self.txt_processor.config(state="readonly")

        self.txt_memory.config(state="normal")
        self.txt_memory.delete(0, tk.END)
        self.txt_memory.insert(0, f"{memory:.2f} GB")
        self.txt_memory.config(state="readonly")

        self.txt_python.config(state="normal")
        self.txt_python.delete(0, tk.END)
        self.txt_python.insert(0, python_version)
        self.txt_python.config(state="readonly")

        self.root.after(1000, self.update_info)


root = tk.Tk()
app = MeuPC(root)
root.mainloop()
