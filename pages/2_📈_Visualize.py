import streamlit as st
import pandas as pd 
import plotly.express as px 

st.markdown(
    """
    <style>
        .stApp {
            background-color: #fff9b0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Plotting Page")

if "uploaded_df" in st.session_state:
    df = st.session_state["uploaded_df"]
    
    # Optional: Show column selection
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[selected_columns])


    # Select chart type
    graph = ["Bar","Line"]
    graph_type = st.selectbox("Select type of graph", graph)

    x_values = st.selectbox("Select x axis value to plot", df.columns)
    y_values = st.selectbox("Select y axis value to plot", df.columns)

    data = pd.DataFrame({
    x_values : df[x_values],
    y_values : df[y_values]
    })
    # Example: simple plot
    if graph_type=="Bar":
        # Create Plotly bar chart
        fig = px.bar(data, x=x_values, y=y_values, title=f'Bar Graph of {y_values} by {x_values}')
    else:
        fig = px.line(data, x=x_values, y=y_values, title=f'Line Graph of {y_values} by {x_values}')  

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please upload a file first on the Upload page.")
