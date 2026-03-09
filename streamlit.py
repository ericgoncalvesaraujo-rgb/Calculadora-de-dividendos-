import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

st.set_page_config(page_title="Calculadora de dividendos")

st.markdown("""
<style>

.stApp{
 backgorund-color: black;
 color: white;
 
</style>

            }


""")


st.markdown("""
            
# Calculadora de dividentos

## Essa calculadora tem como objetivo mostrar o poder dos dividendos e a importância de investir em ações que pagam bons dividendos.
""")

#caixa de ações

st.session_state.acoes = []

#pega uma ação do yahoo finance e adiciona a sigla ".SA" por ser br
ticket = str(st.text_input("Digite o código: ")).upper().strip()
if ticket:
 if ticket not in st.session_state:
  st.session_state.acoes.append(ticket)
acao = yf.Ticker(f"{ticket}.SA")
df = acao.history(interval="1d", period="max")
#garante que passe somente a ação correta
if not df.empty:
   st.success("Ação encontrada!!!")
else:
   st.error("acao incorreta ou não existente")

#reseta o index para que a data se torne uma coluna
df.reset_index(inplace=True)

#pegando as datas e garantindo serem possíveis

hj = dt.datetime.now().year

data = st.number_input("Ano do começo dos aportes: ", min_value=1, max_value=hj, step=1)
if data:
  if data <= hj:
   st.success("Data aceita!!!")
  else:
   st.error("data impossivel!!!")

#pega o valor inicial do aporte
valor_inicial = st.number_input("Digite o valor do primeiro aporte: ", min_value=1, step=10)
if valor_inicial:
 valor_inicial = round(valor_inicial, 2)
 if valor_inicial >= df['Close'].iloc[0]:
  st.success("Valor do aporte aceito!!!")
 else:
  st.error("Seu aporte é insuficiente para comprar a ação nesse ano")

#pegar valor do aporte mensal
aporte_mensal = st.number_input("Digite o valor do aporte mensal (caso não for usar coloque 0): ", min_value=0, step=10)
if aporte_mensal:
 aporte_mensal = round(aporte_mensal, 2)
 if aporte_mensal == 0:
  st.info('Não tera aportes mensais')


#organizando arquivos a partir da data 

df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.datetime.year >= data]



  


