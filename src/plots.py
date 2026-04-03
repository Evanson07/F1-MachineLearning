import matplotlib.pyplot as plt
from fastf1 import plotting

# Configurar colores oficiales de F1
plotting.setup_mpl()

# Obtener telemetría de la vuelta más rápida
telemetry = fastest_ver.get_telemetry()

plt.figure(figsize=(10, 6))
plt.plot(telemetry['Distance'], telemetry['Speed'], label='VER - Speed')
plt.xlabel('Distancia (m)')
plt.ylabel('Velocidad (km/h)')
plt.title('Perfil de Velocidad - Verstappen en Mónaco')
plt.legend()
plt.show()