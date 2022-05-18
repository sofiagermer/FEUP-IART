import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpt
import sklearn as sk
import seaborn as sb


if __name__ == '__main__':
    dataset = pd.read_csv('data.csv', na_values=['NA'], delimiter=";")

    dataset_corr = dataset.corr()
    plt.figure(figsize=(20,20))
    mask = np.zeros_like(dataset_corr)
    mask[np.triu_indices_from(mask, k=1)] = True
    sb.heatmap(dataset_corr, linewidths=0.1,cmap="YlGnBu", annot=True, square=True, mask=mask, fmt='.2f', annot_kws={"size": 6});
    plt.show()
