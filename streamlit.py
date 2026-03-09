import yfinance as yf
import datetime as dt
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

st.set.page_config(page_title="Calculadora de dividendos")
st.title("Calculadora de dividentos", color="blue")