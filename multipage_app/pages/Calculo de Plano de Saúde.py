import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st

#IMPORTANTE : RODAR O CODIGO :  streamlit run Streamlit_Regressao_Linear_simples_Plano_Saude.py

#titulo
st.write('Plano de Saúde')
#cabeçalho
st.subheader('Projeto de Regressão linear.\n O objetivo desse Projeto é descobrir o custo de um plano de saude mediante a idade do cliente')
#Mostrar o grafico da planilha original
base_plano_saude = pd.read_csv(r"C:\Users\luis.bezerra.ext\Desktop\Machine Learning\Projetos de Machine Learning\multipage_app\plano_saude.csv")



#separando as categorias dos atributos
x_plano_saude = base_plano_saude.iloc[:,0].values
y_plano_saude = base_plano_saude.iloc[:,1].values




#vamos agora calcular o coeficiente de relação (beta).
percentural_de_relacao = np.corrcoef(x_plano_saude,y_plano_saude)*100
#com isso entendemos que a correlação entre as duas variaveis é de 93%.
#Ou seja, 93% do custo dos planos de saúde são explicados pela idade dos clientes

x_plano_saude = x_plano_saude.reshape(-1,1)


#hora de usar o modelo

regressor_plano_saude = LinearRegression()
regressor_plano_saude.fit(x_plano_saude,y_plano_saude)

previsao = regressor_plano_saude.predict(x_plano_saude)

@st.cache_data
def graf():
    grafico = px.scatter(x = x_plano_saude.ravel(), y= y_plano_saude)
    grafico.add_scatter(x = x_plano_saude.ravel(), y = previsao,name='Regressão')
    grafico.update_layout(title= "Valor do Plano de Saúde",xaxis_title = 'IDADE',yaxis_title='VALOR')
    st.plotly_chart(grafico,theme=None)

graf()
idade = st.number_input('Insira a sua idade',format='%i',max_value=115,min_value=0)

def valor_previsto (idade):

    A = regressor_plano_saude.intercept_
    B = regressor_plano_saude.coef_
    Y = A + B * idade
    Y = float(Y)
    Y = (f'R$ {Y:.2f}')
    return Y

valor = st.write('o valor do plano do cliente é de: ', valor_previsto(idade))

