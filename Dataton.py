import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurações da página do Streamlit
st.set_page_config(page_title="Datathon Passos Mágicos", layout="wide")

# Título e Introdução
st.title("Datathon Passos Mágicos - Grupo 08")
st.write("""
A Passos Mágicos é uma organização educacional em Embu-Guaçu, SP, que oferece aulas de português, matemática e inglês, além de acompanhamento psicopedagógico e psicossocial para crianças e jovens em situação de vulnerabilidade social.
Seu objetivo é promover o desenvolvimento educacional, cognitivo, emocional e social dos alunos, complementando a educação formal e oferecendo oportunidades para que superem suas dificuldades.
""")

# Função para plotar gráficos de exemplo (substituir pelos dados reais)
def plot_bar_chart(data, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.bar(data.index, data.values)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    st.pyplot(fig)

def plot_line_chart(data, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data.index, data.values)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    st.pyplot(fig)

# Seção: Panorama Geral do Sucesso
st.header("Panorama Geral do Sucesso (INDE)")
st.write("""
O INDE (Índice de Desenvolvimento Educacional) mostrou uma evolução positiva ao longo dos anos, com uma tendência geral de crescimento.
Os principais indicadores como o IAN (Indicador de Adequação de Nível) sugerem que os alunos estão progredindo em direção à adequação escolar, enquanto o IEG (Indicador de Engajamento) apresenta uma leve queda.
""")
# Exemplo de gráfico de barras para evolução do INDE
inde_data = pd.Series([3.5, 4.0, 4.5, 5.0], index=[2020, 2021, 2022, 2023])
plot_bar_chart(inde_data, "Evolução do INDE", "Ano", "INDE Médio")

# Seção: Desempenho e Engajamento em 2020
st.header("Desempenho Acadêmico e Engajamento (2020)")
st.write("""
Em 2020, a maioria dos alunos da Passos Mágicos frequentava escolas públicas, com uma pequena parte em instituições privadas como Estácio e Rede Decisão.
O gráfico abaixo mostra as notas dos alunos nas atividades da Passos Mágicos (IDA - Indicador de Desempenho Acadêmico), enquanto o engajamento em atividades extracurriculares, como voluntariado, apresenta desafios.
""")
# Exemplo de gráfico de linhas para desempenho acadêmico em 2020
desempenho_data = pd.Series([60, 65, 70, 75], index=["Setembro", "Outubro", "Novembro", "Dezembro"])
plot_line_chart(desempenho_data, "Desempenho Acadêmico - IDA", "Mês", "Pontuação IDA")

# Seção: Avaliações por Raça e Sexo em 2021
st.header("Avaliações por Raça e Sexo (2021)")
st.write("""
Em 2021, os gráficos de avaliações por raça, sexo e idade mostraram a diversidade dos alunos atendidos pela Passos Mágicos.
Isso permitiu identificar possíveis disparidades e necessidades específicas entre os grupos, destacando a importância de intervenções personalizadas para cada aluno.
""")
# Exemplo de gráfico de barras para avaliações por raça
avaliacao_raca_data = pd.Series([50, 60, 55, 70], index=["Raça A", "Raça B", "Raça C", "Raça D"])
plot_bar_chart(avaliacao_raca_data, "Avaliações por Raça", "Raça", "Pontuação")

# Seção: Desempenho e Bolsas em 2022
st.header("Desempenho e Bolsas (2022)")
st.write("""
Em 2022, o desempenho acadêmico dos alunos foi detalhado em diferentes fases do programa, mostrando que os bolsistas tendem a ter melhores desempenhos em comparação com outros grupos.
O gráfico abaixo ilustra o desempenho acadêmico em diferentes fases do programa, com destaque para as notas nas atividades da Passos Mágicos.
""")
# Exemplo de gráfico de barras para desempenho por fase em 2022
fase_data = pd.Series([80, 85, 78, 90], index=["Fase 1", "Fase 2", "Fase 3", "Fase 4"])
plot_bar_chart(fase_data, "Desempenho por Fase", "Fase", "Pontuação IDA")

# Seção: Insights Gerais (2020-2022)
st.header("Insights Gerais (2020-2022)")
st.write("""
Entre 2020 e 2022, observou-se uma melhora geral no INDE, sugerindo que as ações da Associação Passos Mágicos têm impactado positivamente o desenvolvimento educacional dos alunos. No entanto, ainda há desafios relacionados ao engajamento (IEG), especialmente em atividades de voluntariado e entrega de tarefas.
""")
st.write("""
**Sugestões:**
1. **Gamificação e Incentivos**: Introduzir jogos e recompensas para aumentar o engajamento.
2. **Acompanhamento Individualizado**: Oferecer suporte personalizado aos alunos com dificuldades.
3. **Aulas de Apoio**: Criar programas de reforço escolar focados nas dificuldades dos alunos.
4. **Apoio Psicossocial**: Ampliar o suporte psicossocial para alunos vulneráveis e suas famílias.
""")

# Considerações Finais
st.header("Considerações Finais")
st.write("""
A Passos Mágicos usa estratégias de engajamento para aumentar o interesse e a participação dos alunos. Apesar dos avanços, é necessário um acompanhamento mais individualizado e estratégias como gamificação e comunicação clara para aumentar o engajamento e melhorar o desempenho acadêmico dos alunos.
""")

