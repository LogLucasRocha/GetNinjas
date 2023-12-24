import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')

# Análise 1
plt.figure(figsize=(7, 5))
sns.boxplot(x='survived', y='age', data=titanic, hue='survived', palette='Set2')
plt.xlabel('Sobreviveu')
plt.ylabel('Idade')
plt.title('Distribuição da Idade para Passageiros que Sobreviveram e Não Sobreviveram')
plt.show()

# Análise 2
plt.figure(figsize=(7, 5))
sns.countplot(x='class', hue='survived', data=titanic, palette='Set2')
plt.xlabel('Classe')
plt.ylabel('Número de Passageiros')
plt.title('Número de Passageiros que Sobreviveram e Não Sobreviveram por Classe')
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])
plt.show()

# Análise 3
plt.figure(figsize=(7, 5))
class_palette = {'First': 'red', 'Second': 'blue', 'Third': 'green'}  # Corrigido o mapeamento de cores
sns.scatterplot(x='fare', y='age', data=titanic, hue='class', palette=class_palette, s=100, alpha=0.7)
plt.xlabel('Tarifa (Fare)')
plt.ylabel('Idade (Age)')
plt.title('Relação entre Tarifa e Idade com Cores de Classe')
plt.legend(title='Classe', labels=['Terceiro', 'Primeiro', 'Segundo'])

plt.show()

