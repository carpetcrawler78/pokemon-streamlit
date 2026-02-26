import streamlit as st
import pandas as pd
import functions as f
import plotly.express as px
import plotly.graph_objects as go
import random
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="EDA Visualization",
    page_icon="🔴")

f.navigation()

auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh", value=False)

if auto_refresh:
    count = st_autorefresh(interval=5000, key="auto")
else:
    count = st.session_state.get("_last_count", 0)

st.title("📊 EDA Visualization")
st.subheader("Let's explore the Pokémon dataset.")
st.write("")


# Scatter plot

fig = px.scatter(
    st.session_state.df,
    x='height_m',
    y='weight_kg',
    color='type',
    size='speed',
    title='Height vs Weight (Plotly)',
    hover_data=['name']
)

fig.update_traces(
    hovertemplate=
    '<b>Name:</b> %{customdata[0]}<br>' +
    '<b>Height (m):</b> %{x}<br>' +
    '<b>Weight (kg):</b> %{y}<br>' +
    '<b>Type:</b> %{customdata[1]}<br>' +
    '<b>Speed:</b> %{customdata[2]}<br>' +
    '<extra></extra>',
    customdata=st.session_state.df[['name', 'type', 'speed']].values)

st.plotly_chart(fig, key=f"scatter_{count}")


# Radar chart

st.subheader(f'Pokémon Stats Radar Chart')

options = st.session_state.df.name.to_list()

# Nach Refresh: nur zurücksetzen wenn count sich erhöht hat (echter Autorefresh)
if count != st.session_state.get("_last_count", 0):
    st.session_state["_last_count"] = count
    st.session_state["pokemon"] = options[0]

pokemon_name = st.selectbox(
    'Select Pokemon',
    options,
    key="pokemon"
)

pokemon_row = st.session_state.df[st.session_state.df['name']==pokemon_name].iloc[0]

fig = go.Figure()

r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

vals = list(pokemon_row[st.session_state.stats_cols].values)
cols = list(st.session_state.stats_cols)

fig.add_trace(go.Scatterpolar(
              r=vals + [vals[0]],
              theta=cols + [cols[0]],
              fillcolor=f'rgba({r},{g},{b},0.3)',
              line=dict(color=f'rgb({r},{g},{b})'),
              fill='toself',
              name=pokemon_name)
)

st.plotly_chart(fig)