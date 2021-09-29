import streamlit as st
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  # Display dataset within beta_expander.
  with st.beta_expander("View Dataset"):
    st.table(census_df)
  # Show dataset summary on click of a checkbox.
  if st.checkbox("Show Summary"):
    st.table(census_df.describe())