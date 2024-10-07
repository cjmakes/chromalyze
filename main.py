import matplotlib.pyplot as plt
import analysis

bgrs = analysis.get_colors()
x = [p for p in range(len(bgrs))]
clrs = ['blue','green','red']
plt.stackplot(x, bgrs[:,0], bgrs[:,1], bgrs[:,2], colors=clrs)
plt.show()
