"""
Gera a figura boxplot-ablacao.pdf usada no Capítulo 5 do modelo científico.

Os dados são FICTÍCIOS e servem apenas para ilustrar como produzir um gráfico
vetorial (PDF) em Python para inclusão no LaTeX.

Uso:
    python3 gerar_boxplot_ablacao.py

Requer: numpy e matplotlib.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

SAIDA = Path(__file__).with_name("boxplot-ablacao.pdf")

# Dados fictícios: gap (%) de 10 execuções em cada grupo de instâncias com
# n = 500 itens, para as versões com perturbação fixa e adaptativa.
rng = np.random.default_rng(2026)
grupos = ["m = 5", "m = 10", "m = 30"]
fixa = [rng.normal(mu, 0.08, 10) for mu in (0.42, 0.71, 1.12)]
adaptativa = [rng.normal(mu, 0.06, 10) for mu in (0.31, 0.52, 0.85)]

# Aparência próxima à do texto: fonte com serifa e tamanho de legenda.
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

fig, ax = plt.subplots(figsize=(6.0, 3.0))
posicoes = np.arange(len(grupos))
largura = 0.32

bp1 = ax.boxplot(fixa, positions=posicoes - largura / 2 - 0.02, widths=largura,
                 patch_artist=True, medianprops={"color": "black"})
bp2 = ax.boxplot(adaptativa, positions=posicoes + largura / 2 + 0.02,
                 widths=largura, patch_artist=True,
                 medianprops={"color": "black"})

# Cinza claro liso e cinza escuro hachurado: distinguíveis mesmo impressos em
# preto e branco e por pessoas com daltonismo.
for caixa in bp1["boxes"]:
    caixa.set(facecolor="0.85", edgecolor="black")
for caixa in bp2["boxes"]:
    caixa.set(facecolor="0.55", edgecolor="black", hatch="///")

ax.set_xticks(posicoes)
ax.set_xticklabels(grupos)
ax.set_xlabel("Grupo de instâncias (n = 500)")
ax.set_ylabel("Gap (%)")

# Vírgula como separador decimal nos rótulos do eixo.
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", ",")))

ax.legend(handles=[
    Patch(facecolor="0.85", edgecolor="black", label="Perturbação fixa (k = 5)"),
    Patch(facecolor="0.55", edgecolor="black", hatch="///",
          label="Perturbação adaptativa"),
], frameon=False, loc="upper left")

fig.tight_layout()
fig.savefig(SAIDA, bbox_inches="tight")
print(f"Figura salva em {SAIDA}")
