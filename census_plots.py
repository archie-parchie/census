import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  st.header("Visualise Data")
  st.set_option("Deprecation.showpyplotglobaluse",False)
  plot_list=st.sidebar.multiselect("Select the Charts/Plots.",("Pie Chart","Box Plot","Count Plot"))
  # Display pie plot using matplotlib module and 'st.pyplot()'
  if "Pie Chart" in plot_list:
    feat=st.sidebar.selectbox("Select Which Column to make a Pie Chart for.",("Income Group","Gender"))
    if "Income Group" in feat:
      st.subheader("Pie Chart for Income Groups")
      data=df["income"].value_counts()
      plt.figure(figsize=(20,8))
      plt.pie(data,labels=data.index,autopct="%1.2d%%")
      st.pyplot()
    elif "Gender" in feat:
      st.subheader("Pie Chart for Gender Distribution")
      data=df["gender"].value_counts()
      plt.figure(figsize=(20,8))
      plt.pie(data,labels=data.index,autopct="%1.2d%%",startangle=30)
      st.pyplot()
  # Display box plot using matplotlib module and 'st.pyplot()'
  elif "Box Plot" in plot_list:
    feat=st.sidebar.selectbox("Select Which Column to make a Box Plot for.",("Hours Per Week vs Income Group","Hours Per Week vs Gender"))
    if "Hours Per Week vs Income Group" in feat:
      st.subheader("Boxplot for Hours Per Week vs Income Group")
      plt.figure(figsize=(20,8))
      sns.boxplot(x="hours-per-week",y="income",data=df)
      st.pyplot()
    elif "Hours Per Week vs Gender" in feat:
      st.subheader("Boxplot for Hours Per Week vs Gender")
      plt.figure(figsize=(20,8))
      sns.boxplot(x="hours-per-week",y="gender",data=df)
      st.pyplot()
  # Display count plot using seaborn module and 'st.pyplot()' 
  elif "Count Plot" in plot_list:
    st.subheader("Count Plot for the Distribution of Records for the Unique Workclass Groups")
    plt.figure(figsize=(20,8))
    sns.countplot(x="workclass",data=df)
    st.pyplot()