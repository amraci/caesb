{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5bbade26-b0c2-4a55-8eab-5a4cd65326e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Carregar o arquivo Excel\n",
    "df = pd.read_excel('consumo_caesb.xlsx')\n",
    "\n",
    "# Título do dashboard\n",
    "st.title(\"Dashboard de Consumo de Água\")\n",
    "\n",
    "# Dropdown para selecionar o tipo de consumo (total ou médio)\n",
    "tipo_consumo = st.selectbox(\n",
    "    'Selecione o tipo de consumo',\n",
    "    options=['Consumo Médio']  # Removemos o 'total' pois o seu cálculo está comentado\n",
    ")\n",
    "\n",
    "# Dropdown para filtrar pela unidade\n",
    "unidade_selecionada = st.selectbox(\n",
    "    'Selecione a unidade',\n",
    "    options=df['Sigla'].unique()\n",
    ")\n",
    "\n",
    "# Filtrar o dataframe pela unidade selecionada\n",
    "df_filtrado = df[df['Sigla'] == unidade_selecionada]\n",
    "\n",
    "# Calcular a mediana para o tipo de consumo 'Consumo Médio'\n",
    "media = df_filtrado['Metro'].median()\n",
    "\n",
    "# Criar o gráfico de barras\n",
    "fig = px.bar(\n",
    "    df_filtrado, \n",
    "    x='Comp', \n",
    "    y='Metro', \n",
    "    title=f'Consumo Médio de Água - {unidade_selecionada}',\n",
    "    text=df_filtrado['Metro'].apply(lambda x: f'{x/media:.2%}')\n",
    ")\n",
    "\n",
    "# Adicionar a linha da média\n",
    "fig.add_hline(y=media, line_dash=\"dash\", line_color=\"red\", \n",
    "              annotation_text=\"Mediana\", annotation_position=\"bottom right\")\n",
    "\n",
    "# Exibir o gráfico no Streamlit\n",
    "st.plotly_chart(fig)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d40a55f-260a-400c-a8c8-32607bb95d9d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
