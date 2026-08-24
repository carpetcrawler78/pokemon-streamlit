import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def navigation():
    """
    Function to customize navigation sidebar panel
    """
    
    st.sidebar.page_link("app.py", label='👋 Welcome')
    st.sidebar.page_link("pages/01_eda.py", label="📊 EDA")
    st.sidebar.page_link("pages/02_prediction.py", label="🔮 Prediction")
    st.sidebar.page_link("pages/03_map.py", label="🌍 Map viz")


def show_pairplot(df, columns, hue=None):
    fig = sns.pairplot(df[columns], hue=hue)
    st.pyplot(fig)

def load_data():
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_csv('data/pokemon.csv')
        st.session_state.stats_cols = ['hit_points','attack','defense','sp_attack','sp_defense','speed']