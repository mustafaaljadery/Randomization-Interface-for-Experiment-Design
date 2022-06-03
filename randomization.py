# Implementation of Exact Test

import scipy.stats as stats
import scipy
import scipy.special
import numpy as np
import pandas as pd

ar = np.array([[9, 4], [2, 20]])
df = pd.DataFrame(ar, columns=["Responded", "No Response"])
df.index = ["value1", "value2"]
df.loc['col'] = df.sum(numeric_only=True, axis=0)
df.loc[:, 'row'] = df.sum(numeric_only=True, axis=1)

n = df.at["col", "row"]

exp = df.copy()
for x in exp.index[0:-1]:
    for y in exp.columns[0:-1]:
        v = (((df.at[x, "row"]) *
             (df.at["col", y])) / n).round(2)
        exp.at[x, y] = float(v)

p_observed = (scipy.special.binom(int(df.iloc[0, 2]), 9) * scipy.special.binom(int(
    df.iloc[1, 2]), (int(df.iloc[2, 0])-9)))/scipy.special.binom(n, int(df.iloc[2, 0]))

p_list = []

for i in range(int(df.iloc[0, 2]) + 1):
    value = (scipy.special.binom(int(df.iloc[0, 2]), i) * scipy.special.binom(int(
        df.iloc[1, 2]), (int(df.iloc[2, 0])-i)))/scipy.special.binom(n, int(df.iloc[2, 0]))
    if value <= p_observed:
        p_list.append(value)

p_val = np.sum(p_list)
oddsratio, pvalue = stats.fisher_exact([[9, 4], [2, 20]])

print(pvalue)
