import pandas as pd
import streamlit as st
from .scheduler import LATEST_DATA, LATEST_NEWS


st.set_page_config(page_title="Hospitality Market Intelligence", layout="wide")
st.title("Hospitality Market Intelligence")


def load_data() -> pd.DataFrame:
    if not LATEST_DATA:
        return pd.DataFrame()
    return pd.DataFrame(LATEST_DATA)

def load_news() -> pd.DataFrame:
    if not LATEST_NEWS:
        return pd.DataFrame()
    return pd.DataFrame(LATEST_NEWS)


def render():
    page = st.sidebar.selectbox("Página", ["Visão Geral", "Últimas do Mercado"])
    if page == "Visão Geral":
        render_overview()
    else:
        render_news_feed()


def render_overview() -> None:
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


def render_news_feed() -> None:
    df = load_news()
    if df.empty:
        st.info("Sem notícias disponíveis.")
        return

    search = st.text_input("Buscar empresa")
    date_range = st.date_input(
        "Período",
        [])
    if search:
        df = df[df["company"].str.contains(search, case=False, na=False)]
    if date_range:
        if isinstance(date_range, list) and len(date_range) == 2:
            start, end = date_range
            df = df[(df["date"] >= str(start)) & (df["date"] <= str(end))]

    st.subheader("Últimas do Mercado")
    for _, row in df.iterrows():
        badge = " 🆕" if row['date'][:10] == pd.Timestamp.today().strftime("%Y-%m-%d") else ""
        st.markdown(
            f"### {row['title']}{badge} \n {row['summary']} \n _{row['date'][:10]}_"
        )
        st.markdown(
            f"[Ver matéria original]({row['source']})"
        )
