import matplotlib.pyplot as plt

slices_hours = [4, 8, 2]
activities = ["Sleep", "Work", "walk"]
colors = ["r", "g", "b"]

plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct="%.1f%%")

plt.show()
