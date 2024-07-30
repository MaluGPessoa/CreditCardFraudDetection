import pandas as pd 
import numpy as np 
import zipfile
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_absolute_error, r2_score
from sklearn.datasets import load_iris

df_credit = pd.read_csv(r"C:\\data\\creditcard.zip")

zip_file_path = 'C:\\data\\creditcard.zip'

csv_file_name = 'creditcard.csv'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    with zip_ref.open(csv_file_name) as file:
        df_credit = pd.read_csv(file)


df_credit.head() #verifica dataframe

df_credit.isnull().sum() #verifica se há valores nulos 

df_credit.dtypes #verifica os tipos

df_nao_fraude = df_credit.Amount[df_credit.Class == 0]

df_fraude = df_credit.Amount[df_credit.Class == 1]
                
                #Treinar o modelo 
df_fraude = df_credit[df_credit.Class == 1] #Verifica os dados de fraude

df_nao_fraude = df_credit[df_credit.Class == 0] #Verifica os dados não fraude

#Dataset igualando a quantidade de fraude com a não fraude
df_nao_fraudes = df_nao_fraude.sample(n=492)

#Concat os dataframes fraude e não fraude 
df = pd.concat([df_nao_fraudes, df_fraude], axis=0)

#Arrumando o index
df.reset_index(inplace=True)

#VALIDAR DADOS
df_val_nao_fraude = df.head(5) 

df_val_fraude = df.tail(5)

#retirar as validaçoes
df = df.iloc[5:]

df = df[:-5]

#Concat o dataframe de validação

df_val_total = pd.concat([df_val_nao_fraude, df_val_fraude])
df_val_total.reset_index(inplace=True)
df_val_total_real = df_val_total.Class
df_val_total = df_val_total.drop(['level_0','index','Time','Class'], axis=1)

#Separando labels e features 

X = df.drop(['index','Time','Class'], axis=1)
Y = df['Class']

#Treinamento 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 12, stratify=Y)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, Y_train)
pred = lr.predict(X_test)
acc = accuracy_score(Y_test, pred)

#Precisão dos dados 

f'Acurácia:{acc * 100: .2f}'

#Validar

pred = lr.predict(df_val_total)
df = pd.DataFrame({'real':df_val_total_real, 'previsao':pred})


print(df)


