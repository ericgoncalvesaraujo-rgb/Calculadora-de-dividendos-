import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

st.set_page_config(page_title="Calculadora de dividendos")
st.title("Calculadora de dividentos")

#coleta de dados da ação escolhida
while True:
 #pega uma ação do yahoo finance e adiciona a sigla ".SA" por ser br
 Ticket = str(st.text_input("Digite o código: ")).upper().strip()
 nome = yf.Ticker(f"{Ticket}.SA")
 df = nome.history(interval="1d", period="max")
 #garante que passe somente a ação correta
 if not df.empty:
  break
 else:
  st.error("acao incorreta ou não existente")

#reseta o index para que a data se torne uma coluna
df.reset_index(inplace=True)

#pegando as datas e garantindo serem possíveis

hj = dt.datetime.now().year
while True:
 data = st.number_input("Ano do começo dos aportes: ")
 if data <= hj:
  break
 else:
  st.error("data impossivel!!!")

#pega o valor inicial do aporte
while True:
 valor_inicial = st.number_input("Digite o valor do primeiro aporte: ")
 valor_inicial = round(valor_inicial, 2)
 if valor_inicial >= df['Close'].iloc[0]:
  break
 else:
  st.error("Seu aporte é insuficiente para comprar a ação nesse ano")

#pegar valor do aporte mensal
aporte_mensal = st.number_input("Digite o valor do aporte mensal (caso não for usar coloque 0): ")
aporte_mensal = round(aporte_mensal, 2)
if aporte_mensal == 0:
 st.info('Não tera aportes mensais')


#organizando arquivos a partir da data 

df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.datetime.year >= data]



  


