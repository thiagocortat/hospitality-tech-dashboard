import pandas as pd
import streamlit as st
from .scheduler import LATEST_DATA


st.set_page_config(page_title="Hospitality Market Intelligence", layout="wide")
st.title("Hospitality Market Intelligence")


def load_data() -> pd.DataFrame:
    if not LATEST_DATA:
        return pd.DataFrame()
    return pd.DataFrame(LATEST_DATA)


def render():
    df = load_data()
    if df.empty:
        st.info("Nenhum dado disponível. Aguarde a próxima atualização.")
        return
    companies = df["content"].str.extractall(r"(\\b[A-Z][A-Za-z0-9_]+\\b)")[0]
    company_counts = companies.value_counts().head(10)

    st.subheader("Menções por Empresa")
    st.bar_chart(company_counts)

    st.subheader("Tópicos por Categoria")
    st.write(df.groupby("category").size())

    st.subheader("Dados Brutos")
    st.dataframe(df[["date", "title", "category", "source"]])
