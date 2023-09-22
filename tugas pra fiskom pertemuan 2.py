import numpy as np

# Fungsi untuk persamaan diferensial Bernoulli
def bernoulli_eq(t, y):
    rho = 1.0  # Massa jenis fluida
    P0 = 100000.0  # Tekanan awal
    v0 = 10.0  # Kecepatan awal
    g = 9.81  # Percepatan gravitasi

    # Persamaan diferensial Bernoulli
    dydt = [
        y[1],  # Persamaan pertama: dv/dt = ...
        -(1 / rho) * ((y[1] ** 2) / 2 + P0) + g  # Persamaan kedua: dp/dt = ...
    ]
    return dydt

# Kondisi awal
t_span = (0, 10)  # Rentang waktu
y0 = [v0, P0]  # Kecepatan awal dan tekanan awal

# Menyelesaikan persamaan diferensial
sol = solve_ivp(bernoulli_eq, t_span, y0, t_eval=np.linspace(0, 10, 100))

# Hasilnya
t = sol.t
v = sol.y[0]
P = sol.y[1]

# Anda dapat memplot hasilnya menggunakan Matplotlib jika diperlukan
import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, v, label='Kecepatan')
plt.plot(t, P, label='Tekanan')
plt.xlabel('Waktu')
plt.ylabel('Nilai')
plt.legend()
plt.show()
