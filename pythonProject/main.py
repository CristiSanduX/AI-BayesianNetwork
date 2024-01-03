from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crearea structurii rețelei bayesiene (arcele)
model = BayesianModel([
    ('Gripă', 'Febra'),
    ('Abces', 'Febra'),
    ('Febra', 'Oboseală'),
    ('Febra', 'Anorexie')
])

###
#   Tabelele de probabilități pentru rețeaua bayesiană
###

# Definirea CPD-urilor pentru fiecare variabilă
cpd_gripa = TabularCPD(variable='Gripă', variable_card=2, values=[[0.1], [0.9]])
cpd_abces = TabularCPD(variable='Abces', variable_card=2, values=[[0.05], [0.95]])
cpd_febra = TabularCPD(variable='Febra', variable_card=2,
                       values=[[0.8, 0.7, 0.25, 0.05],
                               [0.2, 0.3, 0.75, 0.95]],
                       evidence=['Gripă', 'Abces'],
                       evidence_card=[2, 2])
cpd_oboseala = TabularCPD(variable='Oboseală', variable_card=2,
                          values=[[0.6, 0.2],
                                  [0.4, 0.8]],
                          evidence=['Febra'],
                          evidence_card=[2])
cpd_anorexie = TabularCPD(variable='Anorexie', variable_card=2,
                          values=[[0.5, 0.1],
                                  [0.5, 0.9]],
                          evidence=['Febra'],
                          evidence_card=[2])

# Asocierea CPD-urilor cu modelul
model.add_cpds(cpd_gripa, cpd_abces, cpd_febra, cpd_oboseala, cpd_anorexie)

# Verificarea corectitudinii modelului
assert model.check_model()

# Inițializarea motorului de inferență
infer = VariableElimination(model)

# Exercițiul 1, Laboratorul 11
# Probabilitatea ca o persoană să fie obosită dacă nu are gripă, nu are abces și nu are anorexie
prob_oboseala = infer.query(variables=['Oboseală'], evidence={'Gripă': 1, 'Abces': 1, 'Anorexie': 1})
print(prob_oboseala)
