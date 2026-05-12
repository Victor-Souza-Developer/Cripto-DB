import streamlit as st
import plotly.express as px

from src.use_cases.streamlit.crypto_dashboard import GetCryptoDashboardData


st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide"
)


use_case = GetCryptoDashboardData()

df, latest_df = use_case.execute()


st.title("Crypto Market Dashboard")


cards = st.columns(len(latest_df))


for index, (_, crypto) in enumerate(latest_df.iterrows()):

    cards[index].metric(
        label=crypto["symbol"].upper(),
        value=f"${crypto['current_price']}",
        delta=f"{float(crypto['price_change_percentage_24h']):.2f}%"
    )


st.divider()


selected_symbol = st.selectbox(
    "Selecione a criptomoeda",
    latest_df["symbol"]
)


filtered_df = (
    df[
        df["symbol"] == selected_symbol
    ]
    .sort_values(
        by="last_updated"
    )
)


fig = px.line(
    filtered_df,
    x="last_updated",
    y="current_price",
    markers=True,
    title=f"Histórico de preço - {selected_symbol.upper()}"
)


fig.update_layout(
    xaxis_title="Data",
    yaxis_title="Preço",
    height=550
)


st.plotly_chart(
    fig,
    use_container_width=True
)