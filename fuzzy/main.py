# logica difusa -> fuzzy

# Ex: custo baixo, benefício alto -> custo-benefício = alto
#     custo alto, benefício alto  -> custo-benefício = médio
#     custo baixo, beneficio baixo -> custo-benefício = médio
#     custo alto, benefício baixo -> custo-benefício = baixo
# A lógica fuzzy é responsável por dar respostas mais humanas, não tão booleanas.


"""
Regras:
    Em um restaurante, classificar a comida como: ruim, boa, saborosa
    o serviço como: ruim, aceitável, ótimo

    - A gorjeta, entre 0% a 20% -> baixa, média, alta
    - Se a comida ou o serviço forem ruins, então, a gorjeta é baixa
    - Se o serviço for médio, então, a gorjeta será média
    - Se o serviço for bom e a qualidade da comida for saborosa, então, a gorjeta é alta.
"""
import time

import skfuzzy as fz
import numpy as np
from skfuzzy import control as ctrl


# antecedentes (se)
quality = ctrl.Antecedent(np.arange(0, 11, 1), "quality")
service = ctrl.Antecedent(np.arange(0, 11, 1), "service")

# consequentes (então)
tip = ctrl.Consequent(np.arange(0, 21, 1), "tip")  # 0% a 20%

# funções membros
quality.automf(number=3, names=["ruim", "boa", "saborosa"])  # comida
service.automf(number=3, names=["ruim", "aceitável", "ótimo"])  # serviço

# visualização
try:
    quality.view()
    service.view()
    quality["saborosa"].view()
except Exception:
    ...


# definição da gorjeta (consequente)
tip["baixa"] = fz.trimf(tip.universe, [0, 0, 10])  # pico em 0
tip["media"] = fz.trimf(tip.universe, [0, 10, 20])  # pico em 10
tip["alta"] = fz.trimf(tip.universe, [10, 20, 20])  # pico em 20

# definição das regras
rule_1 = ctrl.Rule(quality["ruim"] | service["ruim"], tip["baixa"])
rule_2 = ctrl.Rule(service["aceitável"], tip["media"])
rule_3 = ctrl.Rule(quality["saborosa"] | service["ótimo"], tip["alta"])


control_system = ctrl.ControlSystem([rule_1, rule_2, rule_3])
# teste
system = ctrl.ControlSystemSimulation(control_system)
system.input["quality"] = 8.5
system.input["service"] = 6
system.compute()

print(f"Recomenda-se uma gorjeta de {system.output['tip']:.2f} %")
tip.view(sim=system)
