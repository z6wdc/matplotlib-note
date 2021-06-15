import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [10, 20, 30, 40]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
