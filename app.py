import streamlit as st
from prediction import main
from visualization import show_explore_page

page = st.sidebar.selectbox("Visualization Or Prediction", ("Prediction", "Visulizations"))

if page == "Prediction":
    main()
else:
    show_explore_page()
