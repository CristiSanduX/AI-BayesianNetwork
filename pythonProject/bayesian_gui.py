import tkinter as tk
from tkinter import messagebox
from main import infer, model

def calculate():
    selected_variable = variable_to_query.get()
    if selected_variable == "Selectează variabila":
        messagebox.showwarning("Avertizare", "Te rog să selectezi o variabilă pentru a calcula probabilitatea.")
        return
    try:
        prob_result = infer.query(variables=[selected_variable], evidence={'Gripă': 1, 'Abces': 1, 'Anorexie': 1})
        prob_values = prob_result.values
        prob_text = f"Probabilitatea pentru '{selected_variable}':\n"
        prob_text += "\n".join([f"{state}: {prob:.2f}" for state, prob in enumerate(prob_values)])
        messagebox.showinfo("Rezultatul Interogării", prob_text)
    except Exception as e:
        messagebox.showerror("Eroare", str(e))

# Inițializarea interfeței grafice
root = tk.Tk()
root.title("Interfață pentru Rețea Bayesiană")

# Dropdown pentru a selecta variabila pentru care se face interogarea
variable_to_query = tk.StringVar(root)
variable_to_query.set("Selectează variabila")  # opțiunea implicită
query_dropdown = tk.OptionMenu(root, variable_to_query, *model.nodes())
query_dropdown.pack(pady=20)

# Butonul pentru a efectua interogarea
calculate_button = tk.Button(root, text="Calculează Probabilitatea", command=calculate)
calculate_button.pack(pady=20)

root.mainloop()
