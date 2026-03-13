import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Calculadora de Dividendos")

#markdown
st.markdown("""
<style>
.stApp { background-color: white; color: #0E1117; }
            
button { background-color: #grey !important; color: #0E1117  !important; }
            
label, p, h1, h2, h3, h4 { color: #0E1117; }
            
</style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora de Dividendos")

#organizando

if "calcular" not in st.session_state:
  st.session_state.calcular = False                      # variavel para controlar o fluxo do código

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
  hj = dt.datetime.now()
  data = st.date_input("Digite a data inicial: ", max_value=hj.date())
  valor_inicial = st.number_input("Digite o valor inicial: ", min_value = 0.00, step= 100.00)
  aporte_mensal = st.number_input("Digite o valor do aporte mensal (caso não for usar coloque 0): ", min_value=0.00, step=10.00)
  botao_formulario = st.form_submit_button("Calcular")

  if botao_formulario:
   st.spinner("Calculando dividendos...")
   st.success("Cálculo concluído!")
   st.write(f"Data inicial: {data}")
   st.write(f"Valor inicial: R$ {valor_inicial:,.2f}")
   st.write(f"Aporte mensal: R$ {aporte_mensal:,.2f}")
  
   st.session_state.calcular = True

if st.session_state.calcular:
 
 df = st.session_state.df.copy()

 df["Date"] = df["Date"].dt.tz_localize(None)
 df = df[df["Date"] >= pd.to_datetime(data)]
 df["Date"] = pd.to_datetime(df['Date'])

 df_ano_mes = df.copy()

 df_ano_mes["Date"] = pd.to_datetime(df_ano_mes["Date"]).dt.to_period("M")

 df_ano_mes = df_ano_mes.groupby("Date").agg({
    "Dividends" : "sum", "Close" : "last"
 })

 
 st.plotly_chart(df_ano_mes[["Dividends", "Close"]])




