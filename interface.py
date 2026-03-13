import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Calculadora de Dividendos")

#markdown
st.markdown("""
<style>
.stApp { background-color: #0E1117; color: white; }
label, p, h1, h2, h3, h4 { color: white !important; }
button { background-color: blue !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora de Dividendos")

#organizando
if "acoes" not in st.session_state:
    st.session_state.acoes = []

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

if "df_ano_mes" not in st.session_state:
  st.session_state.df_ano_mes = pd.DataFrame()


#pedindo a ação
ticket_input = st.text_input("Digite o código da ação (ex: PETR4):").upper().strip()

if ticket_input and ticket_input not in st.session_state.acoes:
 st.session_state.acoes.append(ticket_input)

# Seleção de ações
if st.session_state.acoes:
 escolha_acao = st.selectbox("Escolha a ação da sua lista:", st.session_state.acoes)

if st.button("Buscar Dados"):
 with st.spinner("Buscando dados no Yahoo Finance..."):
  acao = yf.Ticker(f"{escolha_acao}.SA")
  df_temporario = acao.history(period="max")
  if df_temporario.empty:
    st.error("Não foi possível encontrar dados para a ação selecionada.")
  else:
    df_temporario.reset_index(inplace=True)
    st.session_state.df = df_temporario
    st.success("Dados carregados com sucesso!")
  
#fazendo o formulario
if not st.session_state.df.empty:
  with st.form("formulario"):
    hj = dt.now()
    data = st.number_input("Digite a data inicial: ", min_value=1900, max_value=hj, step=1)
    valor_inicial = st.number_input("Digite o valor inicial: ", min_value = 0.0, step= 100)
    aporte_mensal = st.number_input("Digite o valor do aporte mensal (caso não for usar coloque 0): ", min_value=0.0, step=10)
    botao_formulario = st.form_submit_button("Calcular")

if botao_formulario:
 st.spinner("Calculando dividendos...")
 st.success("Cálculo concluído!")

 df = st.session_state.df.copy()

 df = df[df["Date"].year >= hj.year]
 df["Date"] = pd.to_datetime(df['Date'])

df_ano_mes = df.copy()

df_ano_mes["Date"] = pd.to_datetime(["Date"]).dt.to_period("M")

df_ano_mes = df_ano_mes.groupby("Date").agg({
  "Dividends" : "sum", "Close" : "last"
})

if not df_ano_mes.empty:
 st.line_chart(df_ano_mes[["Dividends", "Close"]])




