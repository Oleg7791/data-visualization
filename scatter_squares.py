import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [i ** 2 for i in x_values]
plt.style.use('fast')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

# назначение заголовка диаграммы и меток осей
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
