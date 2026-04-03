import fastf1
import os

# Configuración de la carpeta de caché
CACHE_DIR = 'data/f1_cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

fastf1.Cache.enable_cache(CACHE_DIR)

print("Caché de F1 configurado y listo.")

# Cargar la sesión del GP de Mónaco 2024 (Carrera)
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()

# Ver la tabla de resultados (Data Analyst)
print(session.results[['Abbreviation', 'ClassifiedPosition', 'GridPosition', 'Status']].head())

# Obtener la vuelta más rápida de un piloto (ej. Verstappen)
fastest_ver = session.laps.pick_driver('VER').pick_fastest()
print(f"Vuelta más rápida de Verstappen: {fastest_ver['LapTime']}")