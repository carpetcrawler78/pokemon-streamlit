import streamlit as st
import pandas as pd
import functions as f

# Set configuration and sidebar navigation
st.set_page_config(
    page_title='Pokemon',
    page_icon='🔴'
)

f.navigation()


# Write title/headers/text
st.title('🔴⚪️ Welcome to my :rainbow[Pokémon] - Streamlit Demo!')

# Also with markdown and HTML formatting
# st.markdown("<h1 style='font-size: 33px;'><p style='color:red;'>🔴⚪️ Welcome to my Pokémon - Streamlit Demo!</h1></p>", 
#                   unsafe_allow_html=True)

# st.markdown("Hi!!")
# st.write('I am writing')

# st.header("Header 1")


# Insert image
st.image('images/pokemon.png')

st.subheader('What are we going to do?')
st.write("")
st.markdown('- EDA Visualizations / Dataset exploration \n - __Prediction:__ Is my Pokémon legendary? \n - Find our Pokémon in the map')

# Save variables in the session state
st.session_state.df = pd.read_csv('data/pokemon.csv')
st.session_state.stats_cols = ['hit_points','attack','defense','sp_attack','sp_defense','speed']