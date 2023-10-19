import os

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import statsmodels.api as sm
from statsmodels.tools.tools import add_constant

import streamlit as st

chart_type_map = {    
    'Bar': 'bar',
    'Histogram': 'histogram',
    'Line': 'line',
    'Scatter Plot': 'scatter'

}

def get_dummies(input_df, column_names, drop_first=True):
    new_columns_list = []
    for column_name in column_names:        
        new_columns_df = pd.get_dummies(input_df[column_name], prefix=column_name, drop_first=drop_first)
        new_columns_list.append(new_columns_df)
        
    new_df = pd.concat(new_columns_list, axis=1)
    return new_df

def create_chart(data_df, chart_type, title=None):
    
    if chart_type == 'Bar':
        fig = make_subplots(rows=1, cols=1)
        for column in data_df.columns:
            fig.add_bar(
                y=data_df[column],
                x=data_df.index,
                name=column
            )        
    elif chart_type == 'Histogram':
        fig = px.histogram(
            data_df,            
            x=data_df.iloc[:, 0],
            labels={'x': data_df.columns[0]}
        )
    elif chart_type == 'Line':
        fig = make_subplots(rows=1, cols=1)
        for column in data_df.columns:
            fig.add_trace(
                go.Scatter(
                    x=data_df.index,
                    y=data_df[column],
                    mode='lines',                    
                    name=column
                )
            )
    elif chart_type == 'Scatter Plot':
        if len(data_df.columns) > 1:
            fig = px.scatter(
                data_df,
                x=data_df.iloc[:, 0],
                y=data_df.iloc[:, 1]                
            )
        else:
            fig = None
    
    return fig

if __name__ == '__main__':
    # setup streamlit
    st.set_page_config(
        page_title='Regression Analysis',
        page_icon=':bar_chart:',
        layout='wide'
    )

    st.title(':bar_chart: Regression Analysis')

    df = None

    ############# 1) SIDE BAR #############
    st.sidebar.header('Upload Data:')    
    
    uploaded_file = st.sidebar.file_uploader('Choose a file')
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except:
            st.subheader('Unable to load data. Please try again.')
            uploaded_file = None

        if uploaded_file is not None:
            st.sidebar.header('Data Exploration')

            chart_type = st.sidebar.selectbox(
                'Select a chart type',
                options=chart_type_map.keys()
            )

            if chart_type == 'Scatter Plot':
                max_selections = 2
            elif chart_type == 'Histogram':
                max_selections = 1
            else:
                max_selections = 5
            
            variables = st.sidebar.multiselect(
                'Select Variable(s)',
                options=df.columns,
                max_selections=max_selections
            )

    ############# 2) DATA EXPLORATION #############
    if df is not None:
        st.subheader('Data Exploration')

        if variables != []:
            filtered_df = df[variables]
        else:
            filtered_df = df
        
        fig = create_chart(filtered_df, chart_type, 'my title')
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader('Select data to view')

    ############# 3) MODEL SPECIFICATION #############

    if df is not None:
        run_regression = True
        st.sidebar.subheader('Model Specification')

        dependent_variable = st.sidebar.selectbox(
            'Select the dependent variable',
            options = df.columns
        )

        explanatory_variables = st.sidebar.multiselect(
            'Select explanatory variable(s)',
            options = [column for column in df.columns if column != dependent_variable]
        )

        if (dependent_variable != '') and (explanatory_variables != []):
            st.markdown('---')
            st.subheader('Model Output')            

            X = pd.DataFrame(np.ones(df[dependent_variable].shape[0]), columns=['Constant'])
            for variable in explanatory_variables:
                if df[variable].dtype == 'O':
                    # get dummies for categorical variable
                    if df[variable].nunique() <= 5:
                        X = pd.concat([X, get_dummies(df, [variable])], axis=1)
                    else:
                        run_regression = False
                        st.subheader(f'Variable "{variable}" has too many unique values ({df[variable].nunique()}).')
                        break
                else:
                    X = pd.concat([X, df[variable]], axis=1)

            if df[dependent_variable].dtype == 'O':
                st.subheader(f'Dependent Variable "{dependent_variable}" is categorical. Please use a numeric variable.')
                run_regression = False
                
            else:
                y = df[dependent_variable]

            
            if run_regression:
                

                model = sm.OLS(y, X).fit()
                st.markdown(model.summary()._repr_html_(), unsafe_allow_html=True)

                st.subheader('Actual Vs. Predicted')

                predicted = model.predict(X)

                avp_df = pd.DataFrame(np.concatenate([y.values.reshape(-1, 1), predicted.values.reshape(-1, 1)], axis=1), columns=['actual', 'predicted'])
                fig = create_chart(avp_df, 'Line', 'Actual Vs. Predicted')
                st.plotly_chart(fig, use_container_width=True)

                st.subheader('Residual Plot')
                fig = create_chart(pd.DataFrame(model.resid), 'Line', 'Residual Plot')
                st.plotly_chart(fig, use_container_width=True)

                st.subheader('Residual Histogram')
                fig = create_chart(pd.DataFrame(model.resid, columns=['Residual']), 'Histogram', 'Residual Plot')
                st.plotly_chart(fig, use_container_width=True)

    
    ############# X) RAW DATA #############
    if df is not None:
        st.markdown('---')
        st.subheader('Raw Data')    
        st.dataframe(df)
    
    ############# XX) HIDE STREAMLIT INFO #############
    hide_st_style = '''
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    '''

    st.markdown(hide_st_style, unsafe_allow_html=True)