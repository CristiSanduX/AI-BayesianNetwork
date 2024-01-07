import json
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Funcția pentru încărcarea unui model bayesian dintr-un fișier JSON.
def load_model_from_json(json_file_path):
    # Deschidem fișierul JSON pentru citire.
    with open(json_file_path, 'r') as file:
        data = json.load(file)  # Încărcăm datele din fișierul JSON.

        # Creăm un model Bayesian folosind arcele definite în JSON.
        model = BayesianModel(data["edges"])

        # Iterăm prin fiecare CPD definit în JSON și le adăugăm la model.
        for node, cpd_data in data["cpds"].items():
            cpd = TabularCPD(
                node,
                cpd_data["variable_card"],
                cpd_data["values"],
                evidence=cpd_data.get("evidence"),  # None dacă nu există
                evidence_card=cpd_data.get("evidence_card")  # None dacă nu există
            )
            model.add_cpds(cpd)  # Adăugăm CPD-ul la model.

        # Verificăm dacă modelul este valid.
        if not model.check_model():
            raise ValueError("Modelul încărcat nu este valid.")

        return model  # Returnăm modelul bayesian încărcat.

# Calea către fișierul JSON ce conține structura modelului bayesian și CPD-urile.
model_path = 'values.json'
model = load_model_from_json(model_path)  # Încărcăm modelul.

# Inițializăm motorul de inferență bayesiană folosind modelul încărcat.
infer = VariableElimination(model)
