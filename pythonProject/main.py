import json
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def load_model_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        model = BayesianModel(data["edges"])

        for node, cpd_data in data["cpds"].items():
            cpd = TabularCPD(node, cpd_data["variable_card"], cpd_data["values"],
                             evidence=cpd_data.get("evidence"),
                             evidence_card=cpd_data.get("evidence_card"))
            model.add_cpds(cpd)

        if not model.check_model():
            raise ValueError("Modelul încărcat nu este valid.")

        return model

# Încărcarea modelului
model_path = 'values.json'
model = load_model_from_json(model_path)

# Inițializarea motorului de inferență
infer = VariableElimination(model)



