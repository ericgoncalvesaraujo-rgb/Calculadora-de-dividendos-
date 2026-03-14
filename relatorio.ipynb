# %% [markdown]
# 📊 Calculadora de Dividendos

# %% [markdown]
# *Detalhamento do projeto*
# 

# %% [markdown]
# Esse projeto tem o objetivo de mostrar as pessoas a diferença entre reenvestir ou não os dividendos recebidos quando se tem uma ação, mostrando o efeito bola de neve que causa atravez de um codigo em python

# %% [markdown]
# O projeto foi feito tanto em streamlit quanto sem para mostrar a diferença entre os dois, e o codigo sem streamlit tem a vantagem de ser mais leve e mais facil de rodar, enquanto o codigo com streamlit tem a vantagem de ser mais interativo e mais facil de entender para pessoas que não tem conhecimento em programação, mas os dois seguem mais ou menos o mesmo passo a passo ent explicarei mais o passo a passo do codigo sem streamlit.

# %% [markdown]
# -1 passo: Importar as bibliotecas necessárias para o projeto

# %%
#importar bibliotecas
import pandas as pd
import plotly.express as px
import yfinance as yf
from datetime import datetime


# %% [markdown]
# Isso fara a importação das bibliotecas necessarias para o projeto, como o projeto foi feito para evolução do meu aprendizado em python, optei por aquelas que ja domino, mas futuramente pretentendo aprender outras e evoluir cada vez o meu projeto

# %% [markdown]
# -2 passo: puxar os dados necessarios para o projeto

# %% [markdown]
# 2.1 passo: pegar a ação que quer se analisada e jogar no yfinance para pegar os dados, como preço, data, dividendos, etc

# %%

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

# %% [markdown]
# Nessas linhas de codigo pedem a ação que deseja ser analisada, garante que esteja da forma correta para ser mandada ao yfinance, e depois envia o ticket para o yfinance pegar os dados necessarios para o projeto, usando o while True garante que o usuario digite a ação da forma correta, e caso digite de forma errada, ele avisa e pede para digitar novamente, no final de tudo se a ação existir e estiver no yfinance ele reseta o index, fazendo a dat se tornar coluna, o que deixa mais facil de trabalhar com os dados depois

# %% [markdown]
# 2.2: pegar a data que a pessoa iniciou os aportes(no caso do streamlit, a pessoa pode escolher a data com dia, mes e ano especifico, no codigo normal para deixar mais pratico coloquei so para a pessoa colocar o ano)

# %%
hj = datetime.now().year
while True:

 data = int(input("Ano do começo dos aportes: "))
 #garante data possível 
 if data <= hj:

  break
 else:
  print("data impossível!!!")

# %% [markdown]
# Nessa parte o codigo pede o ano do começo dos aportes e garante que a pessoa não possa escolher um ano no futuro, tbm há o uso de while True para garantir uma resposta correta

# %% [markdown]
# 2.3 Pegar o valor do aporte inicial(que costuma ser um aporte mais alto)
# 

# %%
while True:
 valor_inicial = float(input("digite o valor do primeiro aporte: "))
 valor_inicial = round(valor_inicial, 2)
 if valor_inicial >= df["Close"].iloc[0]:
  break
 else:
  print("Seu aporte é insuficiente para comprar a ação nesse ano")

# %% [markdown]
# Nessa parte pede o valor do aporte inicial e vê se da para comprar a ação escolhida com o valor digitado, tbm usa o while True para garantir

# %% [markdown]
# 2.4: pedir o valor dos aportes mensais

# %%
aporte_mensal = float(input("digite o valor do aporte mensal (caso não for usar coloque 0): "))
aporte_mensal = round(aporte_mensal, 2)
if aporte_mensal == 0:
  print("Não tera aportes mensais")

# %% [markdown]
# Pega o valor dos aportes mensais e informa se a pessoa escolher 0 não tera aportes, tbm usa o while True nessa parte

# %% [markdown]
# -3 passo: arrumar o DataFrame
# 

# %% [markdown]
# 3.1: organizando a data do DataFrame

# %%
df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"].dt.year >= data]

# %% [markdown]
# Essa parte transforma as datas do DataFrame em "datetime" que deixa mais facil de lidar, depois limita o DataFrame a ter somente os dados após a data escolhida

# %% [markdown]
# 3.2: Montar o DataFrame apartir de meses para condizer com os dividendos recebidos e diminuir a quantidade de dados

# %%
df_ano_mes = df.copy()
df_ano_mes["Date"] = pd.to_datetime(df["Date"]).dt.to_period("M")

# %% [markdown]
# Nessa parte é feito uma copia do DataFrame original e faz um novo DataFrame organizado por meses, transformando a data tbm em "datetime" e mudando o periodo para mensal

# %% [markdown]
# 3.3: Organizando o novo DataFrame

# %%

df_ano_mes = df_ano_mes.groupby("Date").agg({
 "Dividends" : "sum", "Close" : "last"
})
df_ano_mes.reset_index(inplace=True)
dividendos_mes = df_ano_mes[df_ano_mes["Dividends"] > 0]

# %% [markdown]
# Nessas linhas pega o DataFrame é juntado somente no necessario, pegando somente o ultimo preço da ação no mes e juntando os dividendos recebidos no mes

# %% [markdown]
# -4 passo: Fazer algumas variáveis necessarias
# 

# %% [markdown]
# 4.1: quantidade de ações que podem ser compradar com o preimeiro aporte

# %%
quantidade = int(valor_inicial // df_ano_mes["Close"].iloc[0])
quantidade_sem_divi = int(valor_inicial // df_ano_mes["Close"].iloc[0])

# %% [markdown]
# Pega o valor inicial divide pelo primeiro valor que tem no DataFrame que é o primeiro preço do ano que a pessoa escolheu, para isso chama o DataFrame pega a coluna "Close", e passa um .iloc[0], que pega o primeiro valor de uma tabela, dps faz novamente em uma outra variável para ser usada em outra parte

# %% [markdown]
# 4.2: mais variáveis auxiliares 

# %%
saldo = (valor_inicial % df_ano_mes["Close"].iloc[0])
aporte_somado = 0
dividendos_somados = 0
saldo_sem_divi = (valor_inicial % df_ano_mes["Close"].iloc[0])
df_final = []

# %% [markdown]
# Nessa parte cria mais algumas variáveis que serão usada num laço do proximo passo, o saldo é o que sobra do valor do aporte inicial, após a ver a quantidade de ações que podem ser compradas, o aporte_somado é os aportes mensais sendo somados para ver o valor dps, os dividendos_somados é a soma dos dividendos recebidos, o saldo_sem_divi é igual o saldo por enquanto também, mas depois do laço muda e o df_final por enquanto é só uma lista vazia

# %% [markdown]
# -5 passo: Criar um laço de repetição

# %% [markdown]
# 5.1: fazer as repetições

# %%
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


# %% [markdown]
# Esse laço usa o itertuples que passa em cada linha da coluna escolhida (quando coloca linha.Close vai passar em cada linha da coluna Close), e cada variavel ai é repetida e se atualizando até a ultima linha, as variáveis com "+=" pegam o valor delas e soma com o da proxima liha que é passada se atualizando e os com só "=" não que atualizam, nessas variáveis criadas algumas tem a versão sem_divi para ser compara com a versão normal(que seria reinvestindo os dividendos)

# %% [markdown]
# 5.2: Adicionando todos os dados a tabela df_final

# %%
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


# %% [markdown]
# Nessa parte adiciona tudo ao df_final, tudo antes dos ":" vira o titulo de uma coluna e tudo dps vira dados da coluna 

# %% [markdown]
# -6 passo: resolvendo os ultimos detalhes

# %% [markdown]
# 6.1: transformando o df_final em um DataFrame e voltando transformando a data de volta ao normal

# %%
df_final = pd.DataFrame(df_final)
df_final["Data"] = df_final["Data"].dt.to_timestamp()

# %% [markdown]
# Essa parte transforma o df_final em um DataFrame e tira o timzezone da coluna data que coloca a hora dependendo do lugar em que está

# %% [markdown]
# 6.2: contruindo as variaveis que mostram os lucros

# %%
gastos = valor_inicial + aporte_somado
valor_final = round(df_final["Patrimonio"].iloc[-1], 2)
valor_final_sem_divi = round(df_final["Patrimonio sem reinvestir"].iloc[-1] + dividendos_somados, 2)


porcentagem_sem_reinvestir = round(((valor_final_sem_divi - gastos)/ gastos)* 100, 2)
porcentagem_reinvestindo = round(((valor_final - gastos)/ gastos) * 100, 2)

# %% [markdown]
# Nessa parte cria uma variavel que mostra o quanto foi gasto nesse tempo, cria um valor final tanto de investisse quanto se não investisse os dividendos, depois cria as variaveis que mostram o lucro se investisse ou não os dividendos

# %% [markdown]
# -7 passo: mostrar os resultados

# %% [markdown]
# 7.1: mostra os textos

# %%
print(f"seu patrimônio seria R$:{valor_final_sem_divi} se não tivesse reenvestido os dividendos com lucro de {porcentagem_sem_reinvestir}% e\nR$:{valor_final} seria seu patrimônio se tivesse reenvestido,\num lucro de {porcentagem_reinvestindo}%")
print("Se tivesse investido vamos te mostrar a mudança\n\n")

#mostrar a tabela e os gráficos da evolução patrimonial com e sem reinvestimento dos dividendos
print("Essa é a tabela da sua evolução patrimonial\n")
print(df_final, "\n\n")

# %% [markdown]
# nessa parte cria textos mostrando toda a evolução de patrimônio se investisse ou não os dividendos e depois mostra como ficou o DataFrame que detalha cada evoluçao

# %% [markdown]
# 7.2: mostra o gráfico fa diferença se investir ou não

# %%
fig = px.line(df_final, x = "Data", y = ["Patrimonio", "Patrimonio sem reinvestir"])
fig.show()

# %% [markdown]
# Nessa parte cria um gráfico com plotly e apresenta como ficou o gráfico



