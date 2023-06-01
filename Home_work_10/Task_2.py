import pandas as pd
import seaborn as sns

# Постройте диаграмму с данными о численности студентов дневной формы обучения южного федерального округа за 2017 год.

df = pd.read_csv('/content/data20152019.csv', sep=';', encoding='cp1251')
df = pd.DataFrame(
    df, columns=['Субъект РФ', 'Численность студентов, очная форма, человек, 2017'])
df = df.iloc[33:41]
plot = sns.barplot(df, x='Субъект РФ',
                   y='Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(labels=df['Субъект РФ'], rotation=90)
