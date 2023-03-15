import tkinter as tk
import platform
import cpuinfo
import psutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Meu PC")
        self.geometry("500x300")

        # Obter informações da CPU
        self.cpu_info = cpuinfo.get_cpu_info()
        self.cpu_percent = psutil.cpu_percent()
        self.mem_info = psutil.virtual_memory()

        # Adicionar widgets
        self.add_labels()
        self.update_cpu_usage()

    def add_labels(self):
        # Labels com as informações da CPU
        tk.Label(self, text="Informações da CPU", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Nome:").grid(row=1, column=0, padx=10)
        tk.Label(self, text=self.cpu_info["brand_raw"]).grid(row=1, column=1)

        tk.Label(self, text="Cores:").grid(row=2, column=0, padx=10)
        tk.Label(self, text=self.cpu_info["count"]).grid(row=2, column=1)

        tk.Label(self, text="Frequência da CPU:").grid(row=3, column=0, padx=10)
        tk.Label(self, text=f"{self.cpu_info['hz_advertised_friendly']} ({self.cpu_info['hz_actual_friendly']})").grid(row=3, column=1)

        self.cpu_usage_label = tk.Label(self, text=f"Uso da CPU: {self.cpu_percent}%", font=("Helvetica", 12))
        self.cpu_usage_label.grid(row=4, column=0, padx=10)

        # Labels com as informações da memória
        tk.Label(self, text="Informações da Memória", font=("Helvetica", 16, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Total de Memória:").grid(row=6, column=0, padx=10)
        tk.Label(self, text=f"{self.mem_info.total / (1024 ** 2):.2f} MB").grid(row=6, column=1)

        tk.Label(self, text="Memoria Disponível:").grid(row=7, column=0, padx=10)
        tk.Label(self, text=f"{self.mem_info.available / (1024 ** 2):.2f} MB").grid(row=7, column=1)

    def update_cpu_usage(self):
        # Obter o valor do uso da CPU
        self.cpu_percent = psutil.cpu_percent()

        # Atualizar o texto do Label correspondente
        self.cpu_usage_label.config(text=f"Uso da CPU: {self.cpu_percent}%", font=("Helvetica", 12))

        # Chamar novamente a função após 1000ms (1 segundo)
        self.after(1000, self.update_cpu_usage)


if __name__ == "__main__":
    app = App()
    app.mainloop()
