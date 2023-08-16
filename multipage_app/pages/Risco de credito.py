import streamlit as st
import pickle
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,accuracy_score

st.set_page_config(page_title='Risco crédito')

#O objetivo dessa aplicação é classificar se um cliente apresenta um risco de crédito Alto, Moderado ou Baixo. Quis deixar que a ação tomada após a previsão ficasse a cargo do usuario.
st.write('Projeto : Risco de Emprestimo')
st.write('O objetivo dessa aplicação é classificar se um cliente apresenta um risco de crédito Alto, Moderado ou Baixo. Quis deixar que a ação tomada após a previsão ficasse a cargo do usuario.')
st.write('Algoritmo utilizado: NAIVE BAYES')
st.write('precisão e assertividade do modelo: 98,1%')

#titulo
st.write('Novos dados')
#cabeçalho
st.subheader('Informações dos dados')
#dataset

#nome usuario
user_input = st.sidebar.text_input('Digite seu nome')

base_risco_credito = pd.read_csv(r'multipage_app/risco_credito.csv')
x_risco_credito = base_risco_credito.iloc[:,0:4].values
y_risco_credito = base_risco_credito.iloc[:,4].values
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()
x_risco_credito[:, 0] = label_encoder_historia.fit_transform(x_risco_credito[:, 0])
x_risco_credito[:, 1] = label_encoder_divida.fit_transform(x_risco_credito[:, 1])
x_risco_credito[:, 2] = label_encoder_garantia.fit_transform(x_risco_credito[:, 2])
x_risco_credito[:, 3] = label_encoder_renda.fit_transform(x_risco_credito[:, 3])



def previsao_nb(lista):
    #df = pre_processing()
    naive_risco_credito = GaussianNB()
    naive_risco_credito.fit(x_risco_credito, y_risco_credito)
    previsao = naive_risco_credito.predict(lista)
    return previsao

def get_user_data():
    Historia = st.sidebar.selectbox('Historia de crédito',('Boa','Desconhecida','Ruim'))
    Divida = st.sidebar.selectbox('Divida',('Alta','Baixa'))
    Garantia = st.sidebar.selectbox('Garantia',('Nenhuma','Adequada'))
    Renda = st.sidebar.selectbox('Renda anual',('acima_35','0_15','15_35'))

    user_data = {
        'Historia': Historia,
        'Divida' : Divida,
        'Garantia' : Garantia,
        'Renda' : Renda
    }

    if user_data['Historia'] == "Boa":
        user_data['Historia']='0'
    elif user_data['Historia'] == "Descohecida":
        user_data['Historia'] = '1'
    else:
        user_data['Historia'] = '2'

    if user_data['Divida'] == 'Alta' :
        user_data['Divida'] = '0'
    elif user_data['Divida'] == 'Baixa':
        user_data['Divida'] = '1'

    if user_data['Garantia'] == 'Nenhuma':
        user_data['Garantia'] = '1'
    elif user_data['Garantia'] == 'Adequada':
        user_data['Garantia'] = '0'

    if user_data['Renda'] == 'acima_35':
        user_data['Renda'] = '2'

    elif user_data['Renda'] == '15_35':
        user_data['Renda'] = '1'
    else :
        user_data['Renda'] = '0'


    features = pd.DataFrame(user_data, index=[0])
    dados_usuario = features.to_excel('dados_usuario.xlsx',index=False)
    return features

user_input_variables = get_user_data()
def graf():
    graf = st.bar_chart(user_input_variables)
    return graf

graf()
st.subheader('Dados do usuario:')
st.write('Nome do Usuario:',user_input)

st.write(user_input_variables)

#novos dados submetidos
dado_novo = pd.read_excel(r'multipage_app/dados_usuario.xlsx')

dado_novo['Historia'] = dado_novo['Historia'].astype('object')
dado_novo['Divida'] = dado_novo['Divida'].astype('object')
dado_novo['Garantia'] = dado_novo['Garantia'].astype('object')
dado_novo['Renda'] = dado_novo['Renda'].astype('object')

lista = dado_novo.values.tolist()


previsoes = previsao_nb(lista)
previsoes ="".join(map(str,previsoes)).upper()

st.subheader('Nivel de Risco do Usuario')
st.write(f'O usuario apresenta um risco: {previsoes}')

