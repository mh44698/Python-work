# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Create a dataset (fake)
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])

# sns.heatmap(df, annot=True, annot_kws={"size": 7})

# sns.heatmap(df, linewidths=2, linecolor='yellow')

# sns.heatmap(df, yticklabels=False)

# sns.heatmap(df, cbar=False)

sns.heatmap(df, xticklabels=4)


plt.show()

