import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# Завдання 2: Обчислення визначеного інтеграла методом Монте-Карло
# Визначення функції

def f(x):
    return x ** 2

a, b = 0, 2  # Межі інтегрування

# Метод Монте-Карло
num_samples = 10000
x_rand = np.random.uniform(a, b, num_samples)
y_rand = np.random.uniform(0, f(b), num_samples)

under_curve = y_rand <= f(x_rand)
integral_mc = (b - a) * f(b) * np.sum(under_curve) / num_samples

# Аналітичний розрахунок інтеграла
result_quad, error = spi.quad(f, a, b)

# Графік
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Monte Carlo Integral: {integral_mc:.4f}, Quad Integral: {result_quad:.4f}')
plt.grid()
plt.show()
