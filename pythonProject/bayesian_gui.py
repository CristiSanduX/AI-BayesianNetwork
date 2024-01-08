import tkinter as tk
from tkinter import messagebox
from main import infer, model

# Inițializarea interfeței grafice
root = tk.Tk()
root.title("Interfață pentru Rețea Bayesiană")
root.geometry('500x400')  # Setează dimensiunea ferestrei

# Frame pentru evidențe
evidence_frame = tk.Frame(root)
evidence_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Dicționar pentru variabilele de evidență
evidence_vars = {}

# Adaugă etichete și dropdown-uri pentru fiecare nod în frame-ul de evidențe
for i, node in enumerate(model.nodes()):
    # Etichetă pentru nod, cu text roșu
    label = tk.Label(evidence_frame, text=node, fg='red', font=('Helvetica', 10, 'bold'))
    label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

    # Dropdown pentru alegerea stării nodului
    var = tk.StringVar(value="Nedefinit")  # Opțiunea implicită
    evidence_vars[node] = var
    dropdown = tk.OptionMenu(evidence_frame, var, "Da", "Nu", "Nedefinit")
    dropdown.grid(row=i, column=1, padx=5, pady=5, sticky='ew')

# Dropdown pentru selectarea variabilei de interogat
variable_frame = tk.Frame(root)
variable_frame.pack(fill='x', expand=True, padx=10, pady=10)

variable_to_query = tk.StringVar(value="Selectează variabila")
query_label = tk.Label(variable_frame, text="Variabila de interogat:")
query_label.pack(side='left', padx=5, pady=5)

query_dropdown = tk.OptionMenu(variable_frame, variable_to_query, *model.nodes())
query_dropdown.pack(side='right', padx=5, pady=5)



def calculate():
    selected_variable = variable_to_query.get()
    if selected_variable == "Selectează variabila":
        messagebox.showwarning("Avertizare", "Te rog să selectezi o variabilă pentru a calcula probabilitatea.")
        return

    evidence = {node: (1 if var.get() == "Da" else 0 if var.get() == "Nu" else None)
                for node, var in evidence_vars.items() if var.get() != "Nedefinit"}

    try:
        prob_result = infer.query(variables=[selected_variable], evidence=evidence)
        prob_values = prob_result.values
        prob_text = f"Probabilitatea pentru '{selected_variable}':\n"
        prob_text += "\n".join([f"{state}: {prob:.2f}" for state, prob in enumerate(prob_values)])
        messagebox.showinfo("Rezultatul Interogării", prob_text)
    except Exception as e:
        messagebox.showerror("Eroare", str(e))

# Butonul pentru a efectua interogarea
calculate_button = tk.Button(root, text="Calculează Probabilitatea", command=calculate)
calculate_button.pack(pady=20)

root.mainloop()
