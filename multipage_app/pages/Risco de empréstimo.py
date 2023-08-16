import streamlit as st
import pickle
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

st.write('Projeto : Risco de Emprestimo')
st.write('Objetivo : Por caracteristicas do solicitante, descobrir se a taxa de risco de emprestimo é alta ou baixa.')
#ALGORITMO : NAIVE BAYES
#accuracy do modelo: 96,3%




#IMPORTANTE: PARA RODAR ESSE CODIGO, BASTA ABRIR O TERMINAL E RODAR streamlit run Streamlit_Risco_emprestimo_Naive_bayes.py

st.set_page_config(page_title='Risco Emprestimo')


with open(r'multipage_app/credit.pkl','rb') as f:
    x_credit_treinamento,y_credit_treinamento,x_credit_test,y_credit_test = pickle.load(f)


def previsao_nb(lista):

    naive_credit_data = GaussianNB()
    naive_credit_data.fit(x_credit_test, y_credit_test)
    previsao = naive_credit_data.predict(lista)
    match previsao:
        case 1:
            return('Alto risco de comprometimento')
        case 0:
            return ('Baixo risco de comprometimento')
    return previsao

#titulo
st.write('Projeto: Risco de emprestimo' /n
        Objetivo:)

def get_user_data():
    Idade = st.sidebar.text_input('Idade')
    Renda = st.sidebar.number_input('Renda Mensal')
    Emprestimo = st.sidebar.slider('Valor do Emprestimo',0,500000,0)

    user_data = {
        'Idade': int(Idade),
        'Renda' : float(Renda),
        'Valor Emprestimo' : int(Emprestimo),

    }


    features = pd.DataFrame(user_data, index=[0])


    dados_usuario = features.to_csv(r'multipage_app/dados_usuario.csv', index=False)


    return features

user_input = st.sidebar.text_input('Nome:')

try:
    user_input_variables = get_user_data()
    dado_novo = pd.read_csv(r'multipage_app/dados_usuario.csv')

    lista = dado_novo.values.tolist()

    previsoes = previsao_nb(lista)
    previsoes = "".join(map(str, previsoes)).upper()
    st.subheader('Nivel de Risco do Usuario')

    st.write(f'O usuario apresenta um risco: {previsoes}')
except:
    st.error('Primeiro adicione sua idade')


try:
    st.subheader('Dados do usuario:')
    st.write('Nome do Usuario:',user_input)
    st.write(user_input_variables)
except:
    st.error('Preencha as informações!')
