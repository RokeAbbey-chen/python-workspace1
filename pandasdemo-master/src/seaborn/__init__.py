import pandas as pd
from matplotlib.pyplot import plot, show
import seaborn as sns
import numpy as np
sns.set(style="white", palette="muted", color_codes=True)     #set( )设置主题，调色板更常用
plot(np.arange(10))
show()

print(sum(range(10)))


def sinplot(flip = 1):
    x = np.linespace(0,14,100)