## 📊 Calculadora de Dividendos com Reinvestimento Automático
Simulador de investimento em ações brasileiras com reinvestimento automático de dividendos, utilizando dados históricos reais do Yahoo Finance.
Este projeto realiza um backtest completo considerando:
✔ Compra inicial de ações
✔ Aportes mensais
✔ Recebimento de dividendos
✔ Reinvestimento automático
✔ Evolução patrimonial mês a mês
✔ Comparação com estratégia sem reinvestimento
# 🎯 Objetivo do Projeto
Demonstrar habilidades em:
Manipulação avançada de dados com Pandas
Consumo de API financeira (yfinance)
Modelagem de fluxo de caixa
Simulação financeira
Backtesting de estratégia de dividendos
Visualização interativa com Plotly
Estruturação lógica e validação de entradas
O projeto foi desenvolvido com foco em aprendizado prático de análise de dados aplicada ao mercado financeiro.
# 🛠 Tecnologias Utilizadas
Python 3.12
Pandas
YFinance
Plotly
Datetime
# 📈 Funcionalidades
🔹 1. Coleta de Dados
Busca automática de dados históricos de ações brasileiras via Yahoo Finance.
Conversão e tratamento de datas.
Agrupamento mensal para simulação.
🔹 2. Simulação de Investimento
Compra inicial com validação de capital mínimo.
Aportes mensais configuráveis.
Cálculo da quantidade de ações adquiridas.
Reinvestimento automático de dividendos.
Controle de saldo residual.
Evolução patrimonial ao longo do tempo.
🔹 3. Comparação de Estratégias
O sistema calcula:
📌 Patrimônio final sem reinvestimento
📌 Patrimônio final com reinvestimento
📌 Lucro absoluto
📌 Percentual de retorno
# 🧠 Lógica de Funcionamento
O usuário informa:
Código da ação
Ano de início
Valor inicial
Valor de aporte mensal
O sistema:
Filtra os dados históricos a partir do ano informado
Agrupa dividendos por mês
Calcula compras de ações com:
Dividendos recebidos
Aportes mensais
Saldo acumulado
Ao final, é gerado:
DataFrame com evolução patrimonial
Gráfico interativo
Comparação de rentabilidade
# 📊 Exemplo de Saída
Tabela com:
Data
Saldo acumulado
Preço de fechamento
Ações compradas no mês
Dividendos recebidos
Total de ações
Patrimônio total
Gráfico de evolução patrimonial ao longo do tempo.
# 📌 Conceitos Financeiros Aplicados
Juros compostos
Reinvestimento de dividendos
Acumulação patrimonial
Backtesting
Simulação de fluxo de caixa
Compra fracionada via saldo acumulado
# 🔍 Estrutura do Código
O projeto segue a seguinte lógica:
Coleta e validação de inputs
Tratamento e organização dos dados históricos
Agrupamento mensal
Simulação iterativa com controle de saldo
Cálculo de métricas finais
Visualização gráfica
#:🚀 Possíveis Melhorias Futuras
Cálculo de CAGR
Cálculo de TIR (IRR)
Cálculo de Drawdown
Comparação com CDI / IBOV
Inclusão de múltiplos ativos
Interface Web (Streamlit ou Flask)
Transformação em API
# 📌 Diferenciais Técnicos
Uso de dados históricos reais
Tratamento correto de datas e períodos
Modelagem própria de reinvestimento
Simulação dinâmica mês a mês
Visualização interativa
# 🧪 Como Executar
Bash
Copiar código
pip install pandas plotly yfinance
python calculadora.py
# 📚 Aprendizados Técnicos
Durante o desenvolvimento deste projeto foram praticados:
Manipulação avançada de DataFrames
Agrupamentos e agregações
Iteração eficiente com itertuples()
Modelagem financeira aplicada
Estruturação de lógica condicional
Visualização de dados financeiros
# 👨‍💻 Autor
Desenvolvido como parte do processo de evolução em Ciência de Dados com foco em aplicações financeiras e mercado quantitativo.
# 💎 Observação para Recrutadores
Este projeto demonstra:
Capacidade de transformar dados brutos em análise aplicada
Entendimento de fluxo financeiro real
Raciocínio quantitativo
Organização lógica
Capacidade de modelar problemas financeiros via código
