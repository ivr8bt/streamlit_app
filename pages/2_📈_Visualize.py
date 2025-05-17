import streamlit as st
import pandas as pd 
import plotly.express as px 

st.markdown(
    """
    <style>
        .stApp {
            background-color: #fff9b0;
        }

        .fade-in {
        animation: fadeIn 2s;
        -webkit-animation: fadeIn 2s;
        -moz-animation: fadeIn 2s;
        -o-animation: fadeIn 2s;
        -ms-animation: fadeIn 2s;
        }

        @keyframes fadeIn {
        0% {opacity:0;}
        100% {opacity:1;}
        }

        @keyframes bounceIn {
        0% {
            transform: scale(0.3);
            opacity: 0;
        }
        50% {
            transform: scale(1.05);
            opacity: 1;
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            transform: scale(1);
        }
    }

    .bounce-in {
        animation: bounceIn 0.8s ease-out;
    }
    </style>

    <div style='text-align: center;'>
        <h1 class='bounce-in'>Plotting Page</h1>
    </div>
    """,
    unsafe_allow_html=True
)


if "uploaded_df" in st.session_state:
    df = st.session_state["uploaded_df"]
    
    # Show column selection
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[selected_columns])


    # Select chart type
    graph_type = st.selectbox("Select type of graph", ["Bar","Line"])

    if graph_type=='Line':
        g = st.selectbox("Would like to group by different categories?", ["Yes","No"])
        if g=='Yes':
            group = st.selectbox("Select categories to group by", df.columns)
            
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
        if g=='Yes':
            data = pd.DataFrame({
                x_values : df[x_values],
                y_values : df[y_values],
                group : df[group]
            })
            fig = px.line(data, x=x_values, y=y_values, color=group, markers=True, title=f'Line Graph of {y_values} by {x_values} grouped by {group}')
        else:
            fig = px.line(data, x=x_values, y=y_values, title=f'Line Graph of {y_values} by {x_values}')  

    # Display in Streamlit
    fig.update_layout(title={'x': 0.5, 'xanchor': 'center'})
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please upload a file first on the Upload page.")
