import pandas as pd 
import seaborn as sns

## Análise 1
print("*****Análise 1*****")
titanic = sns.load_dataset('titanic')
survival_percent_by_class = titanic.groupby('class')['survived'].mean() * 100
for class_name, percent in survival_percent_by_class.items():
    if class_name == 'First':
        class_name = 'Primeira'
    elif class_name == 'Second':
        class_name = 'Segunda'
    elif class_name == 'Third':
        class_name = 'Terceira'
    print(f"{class_name} classe: {percent:.2f}%")

## Análise 2

print("*****Análise 2*****")

conditions = [
    (titanic['age'] < 18),
    (titanic['age'] >= 18) & (titanic['age'] < 30),
    (titanic['age'] >= 30) & (titanic['age'] < 50),
    (titanic['age'] >= 50)
]


labels = [0, 1, 2, 3]


titanic['idade_intervalo'] = pd.cut(titanic['age'], bins=[0, 18, 30, 50, float('inf')], labels=labels, include_lowest=True)

passageiros_por_classe = titanic['idade_intervalo'].value_counts().sort_index()

print(passageiros_por_classe)

## Análise 3
print("*****Análise 3*****")

conditions = [
    (titanic['age'] < 18),
    (titanic['age'] >= 18) & (titanic['age'] < 30),
    (titanic['age'] >= 30) & (titanic['age'] < 50),
    (titanic['age'] >= 50)
]

labels = [0, 1, 2, 3]

titanic['idade_intervalo'] = pd.cut(titanic['age'], bins=[0, 18, 30, 50, float('inf')], labels=labels, include_lowest=True)
sobreviventes_por_classe = (titanic.groupby('idade_intervalo')['survived'].mean() * 100).round(2).astype(str) + '%'

print(sobreviventes_por_classe)