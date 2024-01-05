import tkinter as tk
from tkinter import messagebox
from pgmpy.inference import VariableElimination
from main import load_model_from_json, model_path

# Încărcăm modelul bayesian
model = load_model_from_json(model_path)
infer = VariableElimination(model)


def display_oboseala():
    # Exercițiul 1, Laboratorul 11
    # Probabilitatea ca o persoană să fie obosită dacă nu are gripă, nu are abces și nu are anorexie
    prob_oboseala = infer.query(variables=['Oboseală'], evidence={'Gripă': 1, 'Abces': 1, 'Anorexie': 1})
    # Accesarea valorilor
    oboseala_da = prob_oboseala.values[0]  # Probabilitatea de oboseală când valoarea este 'Da'
    oboseala_nu = prob_oboseala.values[1]  # Probabilitatea de oboseală când valoarea este 'Nu'
    # Conversia rezultatului la un string pentru afișare
    prob_text = f"Probabilitatea de Oboseală: Da = {oboseala_da:.2f}, Nu = {oboseala_nu:.2f}"
    # Afișarea rezultatului într-un messagebox
    messagebox.showinfo("Rezultatul Interogării", prob_text)


# Inițializarea interfeței grafice
root = tk.Tk()
root.title("Interfață pentru Rețea Bayesiană")

# Butonul care va afișa rezultatul interogării
show_result_button = tk.Button(root, text="Afișează Probabilitatea de Oboseală", command=display_oboseala)
show_result_button.pack(pady=20)

# Rularea interfeței grafice
root.mainloop()
