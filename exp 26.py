import matplotlib.pyplot as plt
import numpy as np
y = np.array([351, 140, 240, 115])
mylabels =["Apples", "Bananas", "Cherries", "Dates"]
plt.title("pie chart with labels")
plt.pie(y, labels=mylabels,autopct='%d')
plt.show()