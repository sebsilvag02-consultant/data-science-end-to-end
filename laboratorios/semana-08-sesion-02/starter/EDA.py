import pandas as pd
import os
import matplotlib.pyplot as plt

ruta_base = os.path.dirname(os.path.abspath(__file__))
carpeta_figuras = os.path.join(ruta_base, "figuras")
os.makedirs(carpeta_figuras, exist_ok=True)

data =pd.read_csv(os.path.join(ruta_base, "viajes_taxi.csv"))
print("Análisis exploratorio descriptivo")

data.info()
print(data.dtypes)
print(data.isna().sum())
print(data.duplicated().sum())

print(data.describe())

plt.figure()
plt.hist(data["tarifa"], bins=50)
plt.title("Distribución de la tarifa")
plt.xlabel("USD")
plt.ylabel("Cantidad de viajes")
plt.savefig(os.path.join(carpeta_figuras, "hist_tarifa.png"))
plt.close()

plt.figure()
plt.boxplot(data["tarifa"])
plt.title("Distribución de la tarifa")
plt.savefig(os.path.join(carpeta_figuras, "boxplot_tarifa.png"))
plt.close()

q1=data["tarifa"].quantile(0.25)
q3=data["tarifa"].quantile(0.75)

iqr=q3-q1

limite_superior=q3+1.5*iqr
limite_inferior=q1-1.5*iqr

atipicos=data.query(f'tarifa<{limite_inferior} or tarifa>{limite_superior}')
print(atipicos)

plt.figure()
plt.scatter(data["tarifa"], data["distancia_km"])
plt.title("Relación entre distancia y tarifa")
plt.savefig(os.path.join(carpeta_figuras, "scatter_distancia_tarifa.png"))
plt.close()
#tosolve
#print(data.corr())
