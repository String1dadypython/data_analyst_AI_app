import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_visuals(df):
    st.subheader("📊 Visualizations")

    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) >= 2:
        col1 = st.selectbox("X-axis", numeric_cols)
        col2 = st.selectbox("Y-axis", numeric_cols, index=1)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=col1, y=col2, ax=ax)
        st.pyplot(fig)
    else:
        st.info("Need at least 2 numeric columns for scatterplot.")
