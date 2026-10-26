import pandas as pd

viajes = pd.read_csv("../starter/viajes_taxi.csv")
viajes = viajes[(viajes["tarifa"] != 999.99) & (viajes["duracion_min"] >= 0)].copy()

ZONAS_MANHATTAN = ["Midtown", "Upper East Side", "Upper West Side", "Lower Manhattan", "Harlem"]

# TODO 1: crea la columna es_tarifa_fija (1 o 0): vale 1 cuando el viaje
# va de JFK Airport a una zona de Manhattan, o de una zona de Manhattan a
# JFK Airport. Imprime cuantos viajes la tienen en 1, y la tarifa minima
# y maxima de esos viajes.

es_jfk_a_manhattan = viajes["zona_origen"].eq("JFK Airport") & viajes["zona_destino"].isin(ZONAS_MANHATTAN)
es_manhattan_a_jfk = viajes["zona_origen"].isin(ZONAS_MANHATTAN) & viajes["zona_destino"].eq("JFK Airport")
viajes["es_tarifa_fija"] = (es_jfk_a_manhattan | es_manhattan_a_jfk).astype("int8")

tarifas_fijas = viajes.loc[viajes["es_tarifa_fija"].eq(1), "tarifa"]
print(f"Viajes con tarifa fija: {tarifas_fijas.size}")
print(f"Tarifa mínima: {tarifas_fijas.min()}")
print(f"Tarifa máxima: {tarifas_fijas.max()}")

# TODO 2: codifica zona_origen con one-hot (pd.get_dummies), con el
# prefijo "origen" y dtype=int. Imprime los nombres de las columnas
# nuevas.
columnas_origen = pd.get_dummies(viajes["zona_origen"], prefix="origen", dtype=int)
viajes = pd.concat([viajes, columnas_origen], axis=1)
print(f"Columnas one-hot de origen: {columnas_origen.columns.tolist()}")

# TODO 3: codifica zona_origen de forma ordinal: un numero entero por
# zona, en orden alfabetico, en una columna origen_ordinal.
viajes["origen_ordinal"] = pd.factorize(viajes["zona_origen"], sort=True)[0]

# TODO 4: para cada columna original del dataset, decide si existe en el
# momento en que alguien pide el taxi (antes del viaje) e imprime la
# decision.
disponible_al_pedir = {
    "id_viaje": True,
    "fecha_hora_inicio": True,
    "zona_origen": True,
    "zona_destino": True,
    "distancia_km": False,
    "duracion_min": False,
    "pasajeros": True,
    "metodo_pago": False,
    "tarifa": False,
    "propina": False,
}

for columna, disponible in disponible_al_pedir.items():
    print(f"{columna}: {'si' if disponible else 'no'}")
