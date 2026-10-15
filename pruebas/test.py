import sys
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# 1. Configurar las dimensiones y colores del campo (Estilo césped oscuro)
pitch = Pitch(pitch_color="#3d6957", line_color="#cf30ad", pitch_type='statsbomb')
fig, ax = pitch.draw(figsize=(10, 7))

# 2. Dibujar un pase de prueba ficticio (X_inicio, Y_inicio, X_fin, Y_fin)
# En StatsBomb, el campo mide 120x80 de forma estándar
pitch.arrows(40, 20, 80, 60, width=2, color='#ad993c', ax=ax, label='Pase de prueba')

# 3. Mostrar el resultado
plt.legend(loc='upper left')
plt.title("Mi primer campo de fútbol con mplsoccer", color='green', fontsize=20)

fig.savefig("figures/first_Pitch.png", dpi=150, bbox_inches="tight")
print("OK: figures/first_Pitch.png")

plt.show()

print(sys.version)
print("¡Todo listo VAMOOOOOOOS!")