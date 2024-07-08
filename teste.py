import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import pyautogui
import time
import threading
import keyboard
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Automação com PyAutoGUI")
        self.root.iconbitmap(self.get_relative_path('icon_1-removebg-preview.ico'))  # Adicionar o ícone à janela
        self.pause_event = threading.Event()
        self.pause_event.set()
        self.multiplier = 1.0

        self.csv_path = tk.StringVar()
        self.csv_path.set(self.get_relative_path('csv_abril_2.csv'))

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 12), padding=5)
        self.style.configure('TEntry', font=('Helvetica', 12), padding=5)

        container = ttk.Frame(root, padding="10 10 10 10")
        container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(container, text="Caminho do CSV:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(container, textvariable=self.csv_path, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E))
        ttk.Button(container, text="Selecionar CSV", command=self.select_csv).grid(row=0, column=2, padx=5)
        ttk.Button(container, text="Usar CSV Padrão", command=self.use_default_csv).grid(row=0, column=3, padx=5)

        ttk.Label(container, text="Multiplicador do Time Sleep:").grid(row=1, column=0, sticky=tk.W)
        self.multiplier_entry = ttk.Entry(container)
        self.multiplier_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Button(container, text="Executar Script", command=self.start_script).grid(row=2, column=0, columnspan=4, pady=10)
        
        ttk.Button(container, text="Editar CSV", command=self.edit_csv).grid(row=3, column=0, columnspan=4, pady=10)

        self.time_label = ttk.Label(container, text="Tempo: 0s, Loop: 0")
        self.time_label.grid(row=4, column=0, columnspan=4, pady=10)

        for child in container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        keyboard.on_press_key('esc', self.toggle_pause)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_relative_path(self, filename):
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, filename)

    def select_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            self.csv_path.set(filepath)

    def use_default_csv(self):
        self.csv_path.set(self.get_relative_path('csv_abril_2.csv'))

    def start_script(self):
        try:
            self.multiplier = float(self.multiplier_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "O multiplicador deve ser um número.")
            return

        self.pause_event.set()
        thread = threading.Thread(target=self.run_script)
        thread.start()

    def run_script(self):
        pyautogui.PAUSE = 0.3 * self.multiplier
        tabela = pd.read_csv(self.csv_path.get())
        print(tabela)

        self.perform_actions(tabela)

    def perform_actions(self, tabela):
        start_time = time.time()
        loop_count = 0
        for linha in tabela.index:
            self.pause_event.wait()
            time.sleep(1 * self.multiplier)
            pyautogui.press('3')
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('1')
            time.sleep(0.25 * self.multiplier)
            pyautogui.click(340, 273)
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('4')
            time.sleep(0.25 * self.multiplier)
            pyautogui.click(326, 289)
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('1')
            time.sleep(0.25 * self.multiplier)
            mat = tabela.loc[linha, "MATRICULA"]
            pyautogui.write(str(mat))
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('enter')
            time.sleep(0.25 * self.multiplier)
            valor = tabela.loc[linha, "VALOR"]
            pyautogui.write(str(valor))
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('enter')
            time.sleep(0.25 * self.multiplier)
            centavos = tabela.loc[linha, "CENTAVOS"]
            pyautogui.write(str(centavos))
            time.sleep(0.25 * self.multiplier)
            pyautogui.press('enter')
            time.sleep(0.25 * self.multiplier)
            loop_count += 1
            elapsed_time = time.time() - start_time
            self.time_label.config(text=f"Tempo: {elapsed_time:.2f}s, Loop: {loop_count}")
            self.root.update_idletasks()

    def toggle_pause(self, event):
        self.pause_event.clear() if self.pause_event.is_set() else self.pause_event.set()
        print("Script pausado" if not self.pause_event.is_set() else "Script retomado")

    def edit_csv(self):
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Editar CSV")
        self.edit_window.iconbitmap(self.get_relative_path('icon.ico'))

        self.tree = ttk.Treeview(self.edit_window, columns=("MATRICULA", "VALOR", "CENTAVOS"), show='headings')
        self.tree.heading("MATRICULA", text="MATRICULA")
        self.tree.heading("VALOR", text="VALOR")
        self.tree.heading("CENTAVOS", text="CENTAVOS")
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.load_csv_data()

        ttk.Button(self.edit_window, text="Salvar", command=self.save_csv_data).pack(pady=10)

    def load_csv_data(self):
        try:
            df = pd.read_csv(self.csv_path.get())
            for row in df.itertuples(index=False):
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o CSV: {e}")

    def save_csv_data(self):
        # Implementar a lógica para salvar os dados do CSV
        pass

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Você tem certeza que deseja sair?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()