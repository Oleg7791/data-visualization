import matplotlib.pyplot as plt

from random_walk import RandomWalk

# построение случайного блуждания
rw = RandomWalk()
rw.fill_walk()

# нанесение точек на диаграмму
plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()