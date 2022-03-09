import numpy as np
import pandas as pd
from apriori_python import apriori

df = pd.read_csv('titanic.csv',encoding="UTF-8",sep=",")


grupo1 = df.groupby('PassengerId')['Sex'].apply(list)
grupo2 = df.groupby('PassengerId')['Age'].apply(list)
grupo3 = df.groupby('PassengerId')['Survived'].apply(list)
grupo4 = grupo1 + grupo2 + grupo3


freqItemSet, rules = apriori(grupo4, minSup=0.5, minConf=0.8)
print(len(grupo4))
print(rules) 

print('\n')
print('#######################################################')
print('\n')


grupo1 = df.groupby('PassengerId')['Survived'].apply(list)
grupo2 = df.groupby('PassengerId')['Pclass'].apply(list)
grupo3 = df.groupby('PassengerId')['Cabin'].apply(list)
grupo4 = grupo1 + grupo2 + grupo3


freqItemSet, rules = apriori(grupo4, minSup=0.5, minConf=0.8)
print(len(grupo4))
print(rules) 



