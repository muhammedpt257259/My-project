import matplotlib.pyplot as plt
import pandas as pd


x = ['A','B','C','D','E']
Y = [10, 15, 7, 12, 20]
plt.bar(x, Y)
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()