import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events


#configurações da página
st.set_page_config(page_title="Calculadora de dividendos")

#mudar as cores e fazer textos 
st.markdown("""
<style>

.stApp{
 background-color: #0E1117;
 color: white;
}
label{
 color: white !important;
 }
            
p{
 color: white;}
            
h1 h2 h3 h4 h5 h6{
 color: white;}   

.stButton > button {
  background-color: darkblue;
  color: white;}      
</style>

""", unsafe_allow_html=True)

st.markdown("""
            
# Calculadora de dividentos

## Essa calculadora tem como objetivo mostrar o poder dos dividendos e a importância de investir em ações que pagam bons dividendos.
""")

#caixa de ações
if "acoes" not in st.session_state:
 st.session_state.acoes = []

#criando um dataframe vazio para receber os dados da ação
if "df" not in st.session_state:
 st.session_state.df = pd.DataFrame()

#pega uma ação do yahoo finance e adiciona a sigla ".SA" por ser br
ticket = str(st.text_input("Digite o código: ")).upper().strip()
if ticket and ticket not in st.session_state.acoes:
      st.success("Ação adicionada!!!")
      st.session_state.acoes.append(ticket)
      if st.session_state.acoes:
        escolha_acao =  st.selectbox("Adicione ações:" , st.session_state.acoes)
        acao = yf.Ticker(f"{escolha_acao}.SA")
        st.session_state.df = acao.history(interval="1d", period="max")
        if st.button("Confirmar ação"):
  #garante que passe somente a ação correta
          if st.session_state.df.empty:
            st.error("acao incorreta ou não existente")
          #reseta o index para que a data se torne uma coluna
            st.session_state.df.reset_index(inplace=True)
          else:
            st.success("Ação encontrada!!!")

        #formulario para pegar o ano do começo dos aportes, o valor do primeiro aporte e o valor do aporte mensal
          with st.form("Escolha"):
           hj = dt.datetime.now().year
           data = st.number_input("Ano do começo dos aportes: ", min_value=1, max_value=hj, step=1)
           
           valor_inicial = st.number_input("Digite o valor do primeiro aporte: ", min_value=1, step=10)

           aporte_mensal = st.number_input("Digite o valor do aporte mensal (caso não for usar coloque 0): ", min_value=0, step=10)

         #pegando as datas e garantindo serem possíveis    
          if data:
            if data <= hj:
             st.success("Data aceita!!!")
            else:
              st.error("data impossivel!!!")
            
          #pega o valor inicial do aporte
          if valor_inicial and not st.session_state.df.empty:
            valor_inicial = round(valor_inicial, 2)
            if valor_inicial >= st.session_state.df['Close'].iloc[0]:
              st.success("Valor do aporte aceito!!!")
            else:
              st.error("Seu aporte é insuficiente para comprar a ação nesse ano")

            #pegar valor do aporte mensal
            if aporte_mensal:
              aporte_mensal = round(aporte_mensal, 2)
              st.success("Aportes mensais aceitos!!!")
              if aporte_mensal == 0:
               st.info('Não tera aportes mensais')
            botao_formulario = st.form_submit_button("Confirmar")


          #organizando arquivos a partir da data 
            if botao_formulario:
                  st.session_state.df["Date"] = pd.to_datetime(st.session_state.df["Date"])
                  df = st.session_state.df[st.session_state.df["Date"].dt.year >= data]
                  st.text("Em fase de testes")


  






        


