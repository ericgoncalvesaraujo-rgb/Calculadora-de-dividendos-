#importar bibliotecas
import pandas as pd
import plotly.express as px
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

#organizando dados pelo mês 
df_ano_mes = df
df_ano_mes["Date"] = pd.to_datetime(df["Date"]).dt.to_period("M")

#organizando dividendos

#agrupando os dividendos por mês 

df_ano_mes.groupby("Date")["Dividends"]
df_ano_mes.reset_index(drop=True)
dividendos_mes = df_ano_mes[df_ano_mes["Dividends"] > 0]
#soma os dividendos que foram recebidos
dividendos_somados = dividendos_mes["Dividends"].sum()

#organizando algumas variaveis para saber a rentabilidade 

#calcula o numero exato de acoes que pode ser comprado com o valor inicial 
quantidade = valor_inicial // df["Close"].iloc[0]

#calcula quanto que rende sem os dividendos sendo reenvestidos, mas considerando-os na soma
lucro = round(((df["Close"].iloc[-1] - df["Close"].iloc[0]) * quantidade) + dividendos_somados, 2)


#criando o df final

#variaveis auxiliares
saldo = valor_inicial % df["Close"].iloc[0]
df_final = []
#laço para percorrer o df inteiro e saber a evolução do patrimônio 
for linha in df.itertuples:
 acao_dividendo = ((df.Dividends * quantidade) + saldo) //  df.Close
 saldo = ((df.Dividends * quantidade) + saldo) % df.Close
 quantidade += acao_dividendo
 patrimonio = quantidade * df.Close

 df_final.append({
   "Data" : df.Date,
   "Saldo" : saldo,
   "valor no fechamento" : df.Close,
   "ações compradas" : acao_dividendo,
   "Dividendos" : df.Dividends * quantidade,
   "total de ações" : quantidade,
   "patrimônio" : patrimonio
 })
df_final = pd.DataFrame(df_final)
print(df_final)









