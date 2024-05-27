# Walmart - Store Sales Forecasting

Este repositório contém o código para o projeto "Walmart - Store Sales Forecasting", uma competição do Kaggle que visa prever as vendas semanais para diferentes departamentos em várias lojas da Walmart utilizando dados históricos.

## Descrição do Projeto

### Objetivo

Prever as vendas semanais para cada departamento em cada loja da Walmart, considerando eventos de markdown durante feriados que impactam as vendas de forma significativa.

### Desafios

- Tomar decisões com base em um histórico de dados limitado.
- Prever o impacto de markdowns de feriados em diferentes departamentos.

## Estrutura do Repositório

- `store_sales.py`: Código principal do projeto, que inclui a interface do usuário construída com Streamlit.
- `random_forest_model.pkl`: Modelo pré-treinado de Random Forest Regressor usado para fazer previsões.
- `data/`: Pasta contendo dados utilizados para treinar o modelo (não incluída no repositório por questões de tamanho e confidencialidade).

## Requisitos

- Python 3.7+
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Joblib

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/yourusername/walmart-store-sales-forecasting.git
