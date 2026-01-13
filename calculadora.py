#importar bibliotecas
import pandas as pd
import matplotlib as plt
import yfinance as yf
from datetime import datetime
from decimal import Decimal

#coleta de dados


Ticket = str(input("Digite o codigo da ação")).strip().upper()
Ticker = yf.Ticker(f"{Ticket}.SA")
acao = Ticker.history(interval="1d", period="max")

print(acao)




