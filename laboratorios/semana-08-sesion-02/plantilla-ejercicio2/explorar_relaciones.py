from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DIRECTORIO_SCRIPT = Path(__file__).resolve().parent
DIRECTORIO_FIGURAS = DIRECTORIO_SCRIPT / "figuras"
RUTA_DATOS = DIRECTORIO_SCRIPT.parent / "starter" / "viajes_taxi.csv"

DIRECTORIO_FIGURAS.mkdir(exist_ok=True)
viajes = pd.read_csv(RUTA_DATOS)

errores_confirmados = (viajes["tarifa"] == 999.99) | (viajes["duracion_min"] < 0)
limpios = viajes.loc[~errores_confirmados]
print(f"Filas restantes: {len(limpios)}")

fig, ax = plt.subplots()
ax.scatter(limpios["distancia_km"], limpios["tarifa"])
ax.set_xlabel("Distancia (km)")
ax.set_ylabel("Tarifa")
fig.tight_layout()
fig.savefig(DIRECTORIO_FIGURAS / "distancia_vs_tarifa.png")
plt.close(fig)

viajes_con_tarifa_fija = limpios.loc[limpios["tarifa"] == 70.0]
print(f"Viajes con tarifa fija de 70: {len(viajes_con_tarifa_fija)}")

propinas_por_pago = limpios.groupby("metodo_pago")["propina"].agg(
    propina_promedio="mean",
    viajes_sin_propina=lambda propinas: propinas.eq(0).sum(),
)
print(propinas_por_pago)

columnas = ["distancia_km", "duracion_min", "pasajeros", "propina"]
correlaciones_con_tarifa = limpios[columnas].corrwith(limpios["tarifa"])
print(correlaciones_con_tarifa)

pasajeros = limpios["pasajeros"]
print(f"Viajes con pasajeros vacío: {pasajeros.isna().sum()}")
print(f"Viajes con pasajeros en 0: {pasajeros.eq(0).sum()}")
