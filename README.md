# Streamlit em desenvolvimento, mas a logica do programa ja funciona!!!

# Calculadora de Dividendos com Reinvestimento Automático

Simulador de investimento em ações brasileiras com reinvestimento automático de dividendos, utilizando dados históricos do Yahoo Finance.

O projeto realiza um backtest completo com base em parâmetros definidos pelo usuário, considerando:

- Compra inicial de ações  
- Aportes mensais recorrentes  
- Recebimento periódico de dividendos  
- Reinvestimento automático dos proventos  
- Evolução patrimonial mês a mês  
- Comparação entre estratégia com e sem reinvestimento  

A proposta é analisar, de forma prática e quantitativa, o impacto do reinvestimento de dividendos na construção de patrimônio no longo prazo.

---

## Objetivo

Este projeto foi desenvolvido com foco na aplicação prática de conceitos de Ciência de Dados e Finanças, utilizando dados reais de mercado.

Competências exploradas:

- Manipulação e transformação de séries temporais com `pandas`
- Consumo de dados financeiros via `yfinance`
- Modelagem de fluxo de caixa aplicada a investimentos
- Estruturação de um backtest financeiro
- Simulação de reinvestimento com controle de saldo residual
- Visualização de dados com `plotly`
- Validação de entradas e controle de consistência

O objetivo não é apenas gerar um valor final, mas representar de forma clara a dinâmica de acumulação patrimonial ao longo do tempo.

---

## Bibliotecas Utilizadas

- Python 3.12  
- `pandas`  
- `yfinance`  
- `plotly`  
- `datetime`  

---

## Funcionalidades

### Coleta de Dados

- Busca automática de dados históricos via Yahoo Finance  
- Conversão e tratamento de datas  
- Filtragem por ano de início definido pelo usuário  
- Agrupamento mensal para simulação  

### Simulação de Investimento

- Compra inicial com validação de capital mínimo  
- Aportes mensais configuráveis  
- Cálculo da quantidade de ações adquiridas  
- Reinvestimento automático de dividendos  
- Controle de saldo residual  
- Evolução patrimonial ao longo do tempo  

### Comparação de Estratégias

O sistema calcula:

- Patrimônio final sem reinvestimento  
- Patrimônio final com reinvestimento  
- Lucro absoluto  
- Percentual de retorno  

---

## Lógica de Funcionamento

### Entrada

O usuário informa:

- Código da ação  
- Ano de início dos aportes  
- Valor inicial investido  
- Valor do aporte mensal  

### Processamento

O sistema:

- Filtra os dados históricos a partir do ano informado  
- Agrupa dividendos por mês  
- Calcula compras de ações utilizando:
  - Dividendos recebidos  
  - Aportes mensais  
  - Saldo acumulado  

### Saída

- DataFrame com a evolução patrimonial detalhada  
- Comparação de rentabilidade entre estratégias  
- Gráfico interativo de crescimento do patrimônio  

---

## Conceitos Financeiros Aplicados

- Juros compostos  
- Reinvestimento de dividendos  
- Acumulação patrimonial  
- Backtesting  
- Simulação de fluxo de caixa  
- Compra fracionada via saldo acumulado  

---

## Estrutura do Código

Fluxo principal:

1. Coleta e validação de entradas  
2. Tratamento e organização dos dados históricos  
3. Agrupamento mensal  
4. Simulação iterativa com controle de saldo  
5. Cálculo de métricas finais  
6. Visualização gráfica  

---

## Possíveis Melhorias

- Cálculo de CAGR  
- Cálculo de TIR (IRR)  
- Cálculo de drawdown  
- Comparação com CDI ou IBOV  
- Inclusão de múltiplos ativos  
- Interface Web (Streamlit ou Flask)  
- Transformação em API  

---

## Como Executar

Instale as dependências:

```bash
pip install pandas plotly yfinance
```
 Mande o comando após a instalação:

 ```bash
python calculadora.py
```

## Motivos
Projeto desenvolvido como parte do processo de evolução em Ciência de Dados com foco em aplicações financeiras e mercado quantitativo.

##Observação
Este projeto demonstra:
Capacidade de transformar dados brutos em análise estruturada
Entendimento de fluxo financeiro aplicado
Raciocínio quantitativo
Organização lógica
Modelagem de problemas financeiros por meio de código

