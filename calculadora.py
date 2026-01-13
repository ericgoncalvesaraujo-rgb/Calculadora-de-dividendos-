#importar bibliotecas
import pandas as pd
import matplotlib as plt
import yfinance as yf
from datetime import datetime
from decimal import Decimal

hj = datetime.now().year
#coleta de dados da ação escolhida

#pega uma ação do yahoo finance e adiciona a sigla ".SA" por ser br
Ticket = str(input("Digite o código: ")).upper().strip()
nome = yf.Ticker(f"{Ticket}.SA")
df = nome.history(interval="1d", period="max")

#reseta o index para que a data se torne uma coluna
df.reset_index(inplace = True)
 
#pega a informação da data do inicio dos aportes
data = int(input("Data do começo dos aportes: "))

#garante data possível 
while data > hj:
 if data > hj:
  print("data impossível!!!")
  data = int(input("Data do começo dos aportes: "))


#pega o valor inicial do aporte
valor_inicial = float(input("digite o valor do aporte: "))
valor_inicial = round(valor_inicial, 2)



#organização de dados

#organizando arquivos a partir da data escolhida
df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.year >= data]
df_ano_mes = df
df_ano_mes["Date"] = pd.to_datetime(df["Date"]).dt.to_period("M")

print(df_ano_mes)



