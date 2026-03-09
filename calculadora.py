#importar bibliotecas
import pandas as pd
import plotly.express as px
import yfinance as yf
from datetime import datetime

hj = datetime.now().year
#coleta de dados da ação escolhida

while True:
 #pega uma ação do yahoo finance e adiciona a sigla ".SA" por ser br
 Ticket = str(input("Digite o código: ")).upper().strip()
 nome = yf.Ticker(f"{Ticket}.SA")
 df = nome.history(interval="1d", period="max")
 #garante que passe somente a ação correta
 if not df.empty:
  break
 else:
  print("acao incorreta ou não existente")

#reseta o index para que a data se torne uma coluna
df.reset_index(inplace = True)

#pegando as datas e garantindo serem possíveis
while True:
 #pega a informação da data do inicio dos aportes
 data = int(input("Ano do começo dos aportes: "))
 #garante data possível 
 if data <= hj:

  break
 else:
  print("data impossível!!!")

 
#pega o valor inicial do aporte
while True:
 valor_inicial = float(input("digite o valor do aporte: "))
 valor_inicial = round(valor_inicial, 2)
 if valor_inicial >= df["Close"].iloc[0]:
  break
 else:
  print("Seu aporte é insuficiente para comprar a ação nesse ano")

#pegar valor do aporte mensal

aporte_mensal = float(input("digite o valor do aporte mensal:"))
aporte_mensal = round(aporte_mensal, 2)
if aporte_mensal == 0:
  print("Não tera aportes mensais")
#organização de dados


#organizando arquivos a partir da data escolhida
df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.year >= data]

#organizando dados pelo mês 
df_ano_mes = df.copy()
df_ano_mes["Date"] = pd.to_datetime(df["Date"]).dt.to_period("M")

#organizando dividendos

#agrupando os dividendos por mês 

df_ano_mes = df_ano_mes.groupby("Date").agg({
 "Dividends" : "sum", "Close" : "last"
})
df_ano_mes.reset_index(inplace=True)
dividendos_mes = df_ano_mes[df_ano_mes["Dividends"] > 0]

#organizando algumas variaveis para saber a rentabilidade 

#calcula o numero exato de acoes que podem ser compradas com o valor inicial 
quantidade = int(valor_inicial // df_ano_mes["Close"].iloc[0])
quantidade_sem_divi = int(valor_inicial // df_ano_mes["Close"].iloc[0])

#criando o df final

#variaveis auxiliares
saldo = (valor_inicial % df_ano_mes["Close"].iloc[0])
aporte_somado = 0
dividendos_somados = 0
saldo_sem_divi = (valor_inicial % df_ano_mes["Close"].iloc[0])
df_final = []
#laço para percorrer o df inteiro e saber a evolução do patrimônio 
for linha in df_ano_mes.itertuples():
 dividendos_somados += linha.Dividends * quantidade_sem_divi
 acao_sem_divi = int(saldo_sem_divi // linha.Close)
 acao_dividendo = int((linha.Dividends * quantidade + saldo) //  linha.Close)
 saldo = ((linha.Dividends * quantidade) + saldo) % linha.Close
 saldo_sem_divi = saldo_sem_divi % linha.Close
 saldo += aporte_mensal
 saldo_sem_divi += aporte_mensal
 aporte_somado += aporte_mensal
 quantidade_sem_divi += acao_sem_divi
 quantidade_divi = quantidade
 quantidade += acao_dividendo
 patrimonio = round(quantidade * linha.Close, 2)
 patrimonio_sem_divi = round(quantidade_sem_divi * linha.Close, 2)

 df_final.append({
   "Data" : linha.Date,
   "Saldo" : saldo,
   "Saldo_sem_reinvestir" : saldo_sem_divi,
   "valor no fechamento" : linha.Close,
   "ações compradas" : acao_dividendo,
   "ações compradas sem reinvestir" : acao_sem_divi,
   "Dividendos" : linha.Dividends * quantidade_divi,
   "Dividendos sem reinvestir" : dividendos_somados,
   "total de ações" : quantidade,
   "total de ações sem reinvestir" : quantidade_sem_divi,
   "Patrimonio" : patrimonio,
   "Patrimonio sem reinvestir" : patrimonio_sem_divi
 })



#transformando o df_final em DataFrame e voltando ao tempo normal
df_final = pd.DataFrame(df_final)
df_final["Data"] = df_final["Data"].dt.to_timestamp()

#valores 
gastos = valor_inicial + aporte_somado
valor_final = round(df_final["Patrimonio"].iloc[-1], 2)
valor_final_sem_divi = round(df_final["Patrimonio sem reinvestir"].iloc[-1] + dividendos_somados, 2)

#porcentagem de lucro desse investimento 
porcentagem_sem_reinvestir = round(((valor_final_sem_divi - gastos)/ gastos)* 100, 2)
porcentagem_reinvestindo = round(((valor_final - gastos)/ gastos) * 100, 2)

#mostrar os resultados 
print(f"seu patrimônio seria R$:{valor_final_sem_divi} se não tivesse reenvestido os dividendos com lucro de {porcentagem_sem_reinvestir}% e\nR$:{valor_final} seria seu patrimônio se tivesse reenvestido,\num lucro de {porcentagem_reinvestindo}%")
print("Se tivesse investido vamos te mostrar a mudança\n\n")

print("Essa é a tabela da sua evolução patrimonial\n")
print(df_final, "\n\n")
print("Aqui está o gráfico da sua evolução patrimônial investimento os dividendos\n")
fig = px.line(df_final, x = "Data", y = ["Patrimonio", "Patrimonio sem reinvestir"])
fig.show()







