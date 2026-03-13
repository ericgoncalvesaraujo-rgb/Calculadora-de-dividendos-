import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd
import plotly.express as px

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

#organizando as variáveis de sessão

if "calcular" not in st.session_state:
  st.session_state.calcular = False                      

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
 df_ano_mes. reset_index(inplace=True)

 saldo = valor_inicial % df_ano_mes["Close"].iloc[0]
 saldo_sem_divi = valor_inicial % df_ano_mes["Close"].iloc[0]

 quanti_acao = valor_inicial // df_ano_mes["Close"].iloc[0]
 quanti_acao_sem_divi = valor_inicial // df_ano_mes["Close"].iloc[0]

 aporte_somado = 0

 divi_somado = 0

 df_final = []  

 for row in df_ano_mes.itertuples():
  saldo += (row.Dividends * quanti_acao ) + aporte_mensal
  acao_comprada = saldo // row.Close
  quanti_acao += acao_comprada
  saldo = saldo % row.Close
  patrimonio = quanti_acao * row.Close + saldo
  dividendo_recebido = row.Dividends * quanti_acao



  saldo_sem_divi += aporte_mensal
  acao_comprada_sem_divi = saldo_sem_divi // row.Close
  quanti_acao_sem_divi += acao_comprada_sem_divi
  saldo_sem_divi = saldo_sem_divi % row.Close
  patrimonio_sem_divi = quanti_acao_sem_divi * row.Close + saldo_sem_divi
  dividendos_recebidos_sem_divi = row.Dividends * quanti_acao_sem_divi
   
  aporte_somado += aporte_mensal
  divi_somado += row.Dividends * quanti_acao
  
  
  
  df_final.append({
    "Data" : row.Date,
    "Saldo" : saldo,
    "Saldo_sem_reinvestir" : saldo_sem_divi,
    "Preço da ação" : row.Close,
    "Ações_compradas" : acao_comprada,
    "Ações_compradas_sem_reinvestir" : acao_comprada_sem_divi,
    "Dividendos_recebidos" : dividendo_recebido,
    "Dividendos_recebidos_sem_reinvestir" : dividendos_recebidos_sem_divi,
    "Total de ações" : quanti_acao,
    "Total de ações sem reinvestir" : quanti_acao_sem_divi,
    "Patrimônio" : patrimonio,
    "Patrimônio sem reinvestir" : patrimonio_sem_divi
  })
 
 df_final = pd.DataFrame(df_final)
 
 
 fig  =  px.line(df_ano_mes, x=df_final["Date"], y=(["Patrimônio", "Patrimônio sem reinvestir"]), title="Evoloção reinvestindo ou não os dividendos")
 
 
 st.plotly_chart(fig, use_container_width=True)
 st.bar_chart(df_final[["Data", "Dividendos_recebidos", "Dividendos_recebidos_sem_reinvestir"]].set_index("Data"))




