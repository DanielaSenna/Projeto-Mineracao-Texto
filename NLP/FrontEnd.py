import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

df = pd.read_csv('reviews_positivas.csv')
df2 = pd.read_csv('reviews_negativas.csv')
df3 = pd.read_csv('reviews_kindle_limpo_final.csv')

st.title('Projeto de Mineração de Texto')

x1 = np.array(df["Data"])
x2 = np.array(df2["Data"])
y1 = np.array(df["Review"])
y2 = np.array(df2["Review"])
#y = np.array(list(zip(y1,y2)))




source = pd.DataFrame({
  'date': x1,
  'count_ratings': y1
})

source2 = pd.DataFrame({
  'date': x2,
  'count_ratings': y2
})

graphic1 = alt.Chart(source).mark_line().encode(
    x='date',
    y='count_ratings'
)

graphic2 = alt.Chart(source2).mark_line().encode(
    x='date',
    y='count_ratings'
)


st.write("Reviews Positivas (por mês) ao Longo do Tempo")
st.altair_chart(graphic1 , use_container_width=False)
st.write("Reviews Negativas (por mês) ao Longo do Tempo")
st.altair_chart(graphic2 , use_container_width=False)

text = 'kindle, ler, bateria, leitura, livros, tela, produto, luz, pra, bem, livro, dura, leve, ter, ser, aparelho, iluminação, melhor, recomendo, pouco, comprar, iso, ainda, embutida, comprei, super, pois, ótimo, amazon, bastante, dias, excelente, dia, tempo, uso, qualidade, boa, compra, achei, qualquer, geração, chegou, antes, celular, fácil, tamanho, gostei, sempre, confortávell'


wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(str(text))
plt.figure(figsize=(20,8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
st.pyplot()

