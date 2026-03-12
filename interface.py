import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Calculadora de Dividendos")

# CSS para interface
st.markdown("""
<style>
.stApp { background-color: #0E1117; color: white; }
label, p, h1, h2, h3, h4 { color: white !important; }
button { background-color: blue !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora de Dividendos")

# Inicialização de estados
if "acoes" not in st.session_state:
    st.session_state.acoes = []

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

# Entrada de Ticker
ticket_input = st.text_input(
    "Digite o código da ação (ex: PETR4):"
).upper().strip()

if ticket_input and ticket_input not in st.session_state.acoes:
    st.session_state.acoes.append(ticket_input)

# Seleção de ações
if st.session_state.acoes:

    escolha_acao = st.selectbox(
        "Escolha a ação da sua lista:",
        st.session_state.acoes
    )

    if st.button("Buscar Dados"):

        with st.spinner("Buscando dados no Yahoo Finance..."):

            acao = yf.Ticker(f"{escolha_acao}.SA")
            aux_df = acao.history(period="max")

            if aux_df.empty:
                st.error("Ação incorreta ou sem dados disponíveis.")

            else:
                aux_df.reset_index(inplace=True)

                # Garantir que a coluna Date não tenha timezone
                aux_df["Date"] = aux_df["Date"].dt.tz_localize(None)

                st.session_state.df = aux_df
                st.success(f"Dados de {escolha_acao} carregados!")

# Só mostra o formulário se houver dados
if not st.session_state.df.empty:

    with st.form("config_investimento"):

        hj = dt.datetime.now().year

        ano_inicio = st.number_input(
            "Ano do começo dos aportes:",
            min_value=2000,
            max_value=hj,
            value=2015
        )

        valor_inicial = st.number_input(
            "Valor do primeiro aporte (R$):",
            min_value=0.0,
            step=100.0
        )

        aporte_mensal = st.number_input(
            "Valor do aporte mensal (R$):",
            min_value=0.0,
            step=50.0
        )

        submit = st.form_submit_button(
            "Gerar Gráfico e Simulação"
        )

    if submit:

        df = st.session_state.df.copy()

        # Filtrar por data
        df = df[df["Date"].dt.year >= ano_inicio]

        if df.empty:
            st.warning("Não há dados para o período selecionado.")

        else:

            # Agrupamento mensal
            df["Mes"] = df["Date"].dt.to_period("M").dt.to_timestamp()

            df_mensal = df.groupby("Mes").agg({
                "Close": "last",
                "Dividends": "sum"
            }).reset_index()

            # Gráfico de preço
            st.subheader(
                f"Evolução do Preço de Fechamento - {escolha_acao}"
            )

            st.line_chart(
                df_mensal.set_index("Mes")["Close"]
            )

            # Gráfico de dividendos
            st.subheader("Dividendos Totais por Mês")

            st.bar_chart(
                df_mensal.set_index("Mes")["Dividends"]
            )
    

      






            


