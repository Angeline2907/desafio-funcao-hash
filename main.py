import matplotlib.pyplot as plt
import numpy as np

# --- 1. CONFIGURAÇÃO DO ESTILO FOFO ---
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#4A4A4A'

# --- 2. DADOS DAS PALAVRAS ---
# Valores simulados para as letras: A=1, M=13, O=15, R=18
valores_amor = [1, 13, 15, 18]
valores_roma = [18, 15, 13, 1]

letras_amor = ['A', 'M', 'O', 'R']
letras_roma = ['R', 'O', 'M', 'A']

# Calcula a soma acumulada passo a passo
soma_amor = np.cumsum(valores_amor)
soma_roma = np.cumsum(valores_roma)

# --- 3. CRIANDO O GRÁFICO ---
fig, ax = plt.subplots(figsize=(9, 5.5), facecolor='#FFFDF9')
ax.set_facecolor('#FFFDF9')

# Linhas em tons pastel (Rosa e Azul)
ax.plot(range(1, 5), soma_amor, marker='o', markersize=10, linewidth=3, color='#FF8DA1', label='Palavra: AMOR 🌸')
ax.plot(range(1, 5), soma_roma, marker='s', markersize=10, linewidth=3, color='#8DCAFF', label='Palavra: ROMA 🐳')

# Letras da palavra AMOR
for i, (txt, val) in enumerate(zip(letras_amor, soma_amor)):
    ax.annotate(f"{txt}\n({val})", (i+1, val), textcoords="offset points", 
                xytext=(0, 12), ha='center', fontsize=10, weight='bold', color='#D84B6B')

# Letras da palavra ROMA
for i, (txt, val) in enumerate(zip(letras_roma, soma_roma)):
    ax.annotate(f"{txt}\n({val})", (i+1, val), textcoords="offset points", 
                xytext=(0, -22), ha='center', fontsize=10, weight='bold', color='#3B82C4')

# Estrela dourada no ponto de colisão final
ax.plot(4, soma_amor[-1], marker='*', markersize=22, color='#FFD700', mec='#E6B800', mew=2, label='Colisão de Hash! 🌟')

# --- 4. CUSTOMIZAÇÃO VISUAL ---
ax.set_title("Caminhos Diferentes, Mesmo Hash Final! ✨", fontsize=15, weight='bold', pad=20, color='#5C5C5C')
ax.set_xlabel("Passo a Passo da Soma das Letras", fontsize=11, labelpad=10)
ax.set_ylabel("Valor do Hash Acumulado", fontsize=11, labelpad=10)

ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Letra 1', 'Letra 2', 'Letra 3', 'Letra 4'], fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6, color='#E0E0E0')

ax.legend(loc='upper left', frameon=True, facecolor='#FFFFFF', edgecolor='#EAEAEA', fontsize=10)
ax.set_ylim(0, 60)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# --- 5. SALVAR A IMAGEM AUTOMATICAMENTE ---
plt.tight_layout()
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
print("✨ Sucesso! O arquivo 'grafico.png' foi gerado na sua pasta.")
