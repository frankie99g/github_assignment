import streamlit as st
import pandas as pd


st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

# Part 1: Setup and Connected to Dataset

df_kart = pd.read_csv('data/kart_stats.csv')
# st.dataframe(df_kart)


# Part 2: Create Visualizations

# Visualization 1
# Limit Columns and sort by Weight
df_kart = df_kart[['Body','Weight','Acceleration','Ground Speed','Ground Handling','On-Road traction']].sort_values('Weight',ascending=False)
# Highlight min/max
st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0,subset=['Body','Weight','Acceleration','Ground Speed','Ground Handling','On-Road traction'])
             .highlight_min(color='pink', axis=0,subset=['Body','Weight','Acceleration','Ground Speed','Ground Handling','On-Road traction']),
             width=704
            )

# Visualization 2 - line chart
st.line_chart(df_kart, x='Ground Speed', y=['Acceleration'])
#Visualization 3 - scatter chart
st.header('Acceleration increases as Weight decreases')
st.scatter_chart(df_kart, x='Acceleration', y='Weight', color='Ground Speed', size='Ground Handling')

# Part 3: Dynamic Bar Chart
# Dropdown selection
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
# Dataframe for selected kart
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
#Unpivot the data
df_unp_kart = df_single_kart.unstack().rename_axis(['Category','row number']).reset_index().drop(columns='row number').rename({0:'Strength'}, axis=1)
# Display bar chart for single kart
st.bar_chart(df_unp_kart, x='Category', y='Strength')