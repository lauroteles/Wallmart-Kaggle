import pandas as pd
import numpy as np
import streamlit as st
import joblib
class Wallmart_st_sales():
    def __init__(self):
        print('hello world')

    def juntando_dados(self,store_input,dept_input,date_input,holiday_input,temperature_input,fuel_input):

        test_file = pd.DataFrame({
            'Store': [store_input],
            'Dept': [dept_input],
            'Date': [date_input],
            'Weekly_Sales': [0],
            'IsHoliday_x': [holiday_input],
            'Temperature': [temperature_input],
            'Fuel_Price': [fuel_input]
        })
        return test_file

    def feature_engeneering(self,test_file2):
        test_file2['Date'] = pd.to_datetime(test_file2['Date'])


        test_file2['IsHoliday_x'] = np.where(test_file2['IsHoliday_x']==False,0,1)
        test_file2['Year'] = test_file2['Date'].dt.year
        test_file2['Weekday'] = test_file2['Date'].dt.weekday
        test_file2['Month'] = test_file2['Date'].dt.month
        test_file2['leap_year'] = test_file2['Date'].dt.is_leap_year
        test_file2['Year_Start_End']= test_file2['Date'].dt.is_year_start

        test_file2['leap_year'] = np.where(test_file2['leap_year']==False,0,1)
        test_file2['Year_Start_End'] = np.where(test_file2['Year_Start_End']==False,0,1)

        test_file2['Month sin'] =  test_file2['Month'].apply(lambda x: np.sin(x *(2 *np.pi/12)))
        test_file2['Month con'] =  test_file2['Month'].apply(lambda x: np.cos(x *(2 *np.pi/12)))

        return test_file2
    
    def final_preparation(self,test_file4):

        X = test_file4.drop(columns=['Date','Weekly_Sales'])
        return X



        


if __name__=="__main__":

    st.sidebar.text('Bem vindo ao meu portfolio \nde projetos \nde ML(Machine Learning e \nDeep Learning)')
    seletor_de_projetos = st.sidebar.radio('Projetos',options=['Home','Walmart - Store Sales Forecasting(Kaggle Competition)'])
    if seletor_de_projetos == 'Home':
        st.text('')
    if seletor_de_projetos == 'Walmart - Store Sales Forecasting(Kaggle Competition)':
        

        st.markdown(
              "Walmart - Store Sales Forecasting\n"
                "\nEste projeto é uma competição do Kaggle chamada Walmart Recruiting - Store Sales Forecasting. O objetivo é prever as vendas semanais para diferentes departamentos em várias lojas da Walmart, utilizando dados históricos.\n"

                "\nDescrição do Projeto\n"
               " \nUma das principais dificuldades ao modelar dados de varejo é a necessidade de tomar decisões com base em um histórico limitado. Este desafio é intensificado por eventos de markdown em feriados específicos, que afetam as vendas de maneira imprevisível. A tarefa é prever as vendas para cada departamento em cada loja da Walmart, levando em consideração esses markdowns.\n"

                "\nO projeto utiliza um modelo de Machine Learning (Random Forest Regressor) treinado com dados históricos de vendas, temperaturas, preços de combustível, feriados e outras variáveis sazonais. O objetivo final é fornecer previsões precisas para ajudar na tomada de decisões estratégicas.\n"

                "\nComo Utilizar"
                "\nInsira os dados da loja, departamento, data, se é feriado, temperatura e preço do combustível nos campos fornecidos.\n"
                "\nClique no botão Prever Valor das vendas para obter a previsão das vendas semanais.\n"
                "\nA previsão será exibida na página junto com os dados inseridos.\n"
                "\nExperimente e veja como as previsões podem ajudar a melhorar a precisão nas decisões de negócios!\n\n")

        store_input = st.number_input("Escolhe o store(Valores entre 1 e 45) :",key="st",min_value=1, max_value=45)
        dept_input = st.number_input("Escolha o departamento (Valores entre 1 e 98) :",key="dpt",min_value=1, max_value=98)
        date_input = st.date_input("Insira data da predição semanal de vendas :",key="date")
        holiday_input = st.number_input("Se a data escolhida for feriado coloque 1 caso contrário coloque 0 :",min_value=0, max_value=1,key="hol")
        temperature_input = st.number_input("Insira a temperatura do dia(Formato 38.42) :",key="temp")
        fuel_input = st.number_input("Insira o valor da Gasolina no dia escolhido (Formato 3.255) :",key="fuel")

        wp = Wallmart_st_sales()
        pipeline = wp.juntando_dados(store_input,dept_input,date_input,holiday_input,temperature_input,fuel_input)
        pipeline_2 = wp.feature_engeneering(pipeline)
        pipeline_3 = wp.final_preparation(pipeline_2)

        if st.button('Prever Valor das vendas :'):
            model = joblib.load('random_forest_model.pkl')

            prediction = model.predict(pipeline_3)

            pipeline_2['Weekly_Sales'] = prediction
            st.metric("Weekly Sales Prediction", f"{pipeline_2['Weekly_Sales'].iloc[0]:,.2f}")

   

