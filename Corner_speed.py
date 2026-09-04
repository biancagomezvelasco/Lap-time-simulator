import numpy as np
mu = 0.50
g = 9.81
r = 80
vmax_m_per_second = np.sqrt(mu * g * r)
vmax_km_per_hour = (vmax_m_per_second / 1000) * 60**2
print (vmax_m_per_second, "m/s")
print (vmax_km_per_hour, "km/h")
