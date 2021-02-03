import pandas as pd
import numpy as np


investments = [round(np.random.rand())*500 for i in range(10)]
prices = [10]
for i in range(9):
    prices.append(prices[-1] * ((-1)**(2*round(np.random.random())))*(1 + np.random.rand()/50))
df = {'market' : prices}
df = pd.DataFrame(df)

leftover = 0
print(sum(investments))
for i in range(len(investments)):
        if investments[i]>0:
            shares = (investments[i] + leftover)/df['market'][i]
            to_buy = np.floor(shares)
            leftover = (investments[i] + leftover)*(shares-to_buy)/shares
            investments[i] = df['market'][i]*to_buy

print(sum(investments))

print(investments)
