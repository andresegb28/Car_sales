<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('data/vehicles_us.csv')  

# Load and clean data
df = df.dropna(subset=['model_year', 'odometer', 'cylinders', 'paint_color'])
df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)

# Add a header
st.header('Car Advertisement Data Dashboard')

# Days listed distribution
st.subheader("Distribution of Days Listed")
fig = px.histogram(
    df, x='days_listed', nbins=30,
    title="Distribution of Days Listed"
)
st.plotly_chart(fig)

# Price vs Odometer scatter plot
st.subheader("Price vs Odometer")
fig = px.scatter(
    df, x='odometer', y='price',
    title="Price vs Odometer", opacity=0.5
)
st.plotly_chart(fig)

# Boxplot: Price by condition
st.subheader("Price by Vehicle Condition")
fig = px.box(
    df, x='condition', y='price',
    title="Price by Vehicle Condition"
)
st.plotly_chart(fig)

# Top 10 models
top_models = df['model'].value_counts().head(10).reset_index()
top_models.columns = ['model', 'count'] 

fig_1 = px.bar(
    top_models,
    x='model',
    y='count',
    title="Top 10 Most Common Models"
)
st.plotly_chart(fig_1)

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Compare manuifacturers with select boxes
st.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox('Select manufacturer 1',
                              manufac_list, index=manufac_list.index('chevrolet'))

manufacturer_2 = st.selectbox(
    'Select manufacturer 2',
    manufac_list,
    index=manufac_list.index('hyundai') if 'hyundai' in manufac_list else 0
)
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay'))
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('vehicles_us.csv')  

# Load and clean data
df = df.dropna(subset=['model_year', 'odometer', 'cylinders', 'paint_color'])
df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)

# Add a header
st.header('Car Advertisement Data Dashboard')

# Days listed distribution
st.subheader("Distribution of Days Listed")
fig = px.histogram(
    df, x='days_listed', nbins=30,
    title="Distribution of Days Listed"
)
st.plotly_chart(fig)

# Price vs Odometer scatter plot
st.subheader("Price vs Odometer")
fig = px.scatter(
    df, x='odometer', y='price',
    title="Price vs Odometer", opacity=0.5
)
st.plotly_chart(fig)

# Boxplot: Price by condition
st.subheader("Price by Vehicle Condition")
fig = px.box(
    df, x='condition', y='price',
    title="Price by Vehicle Condition"
)
st.plotly_chart(fig)

# Top 10 models
top_models = df['model'].value_counts().head(10).reset_index()
top_models.columns = ['model', 'count'] 

fig_1 = px.bar(
    top_models,
    x='model',
    y='count',
    title="Top 10 Most Common Models"
)
st.plotly_chart(fig_1)

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Compare manuifacturers with select boxes
st.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox('Select manufacturer 1',
                              manufac_list, index=manufac_list.index('chevrolet'))

manufacturer_2 = st.selectbox(
    'Select manufacturer 2',
    manufac_list,
    index=manufac_list.index('hyundai') if 'hyundai' in manufac_list else 0
)
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay'))
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
