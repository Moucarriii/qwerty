import streamlit as st
import pandas as pd
import plotly.express as px 
st.title("Plotly Visualizations!!!")

#### Data For Charts
covid= pd.read_csv(r"Covid_death_DATA.csv")
co2=pd.read_csv(r"co2_emission_data.csv")
sb= pd.read_csv(r"Starbucks satisfactory survey_DATA.csv")
fig2=px.histogram(co2,x="Year",y="Co2 Emission",color="Country",title="Co2 Emission per Year",hover_name="Country")
fig3=fig=px.bar(co2,x="Country",y="Co2 Emission",color="Country",animation_frame="Year",animation_group="Country",range_y=[0,9000000000])
fig4=px.pie(sb, values="How would you rate the price range at Starbucks?", names="Gender",title="Rating Starbucks Prices Based on Gender")
fig5=px.treemap(covid,path=['country'],values="covid_deaths",title="Total Covid Deaths (2020-2022)")

df = pd.DataFrame({
    'first column': ['1','2','3','4','5'],
   
    })
print(df)
option = st.selectbox(
    'Which Visualizations would you like to see?',
     df['first column'])

'You selected: ', option

if '1' in option :
    slider_year = st.slider("Choose Year Range", max_value = 2020, min_value = 1940, value = [1940, 2020], step=10)
    co2_2 = co2.loc[(co2["Year"] >= slider_year[0]) & (co2["Year"] <= slider_year[1])]
    fig1= px.scatter(co2_2,x="Year",y="Co2 Emission",color="Country",hover_name="Country",title="Yearly Co2 Emission by Country")

    st.plotly_chart(fig1) 
    info= st.checkbox("More info")
    if info: 
        st.write("The above VISUAL is a SCATTER PLOT showing the  emission of CO2 of several Countries since 1940. As observed, China and the United States are the top leading counrties in Co2 Emission")
    if info:
        st.balloons()
    
    
if '2' in option:
     st.plotly_chart(fig2)
     info= st.checkbox("More info")
     if info: 
         st.write("The above VISUAL is a HISTOGRAM showing the sum of emission of CO2 of several Countries since 1940")
     if info:
         st.balloons()

    
if '3' in option:
     st.plotly_chart(fig3)
     info= st.checkbox("More info")
     if info: 
         st.write("The above VISUAL is a BAR GRAPH showing the emission of CO2 of several Countries since 1940")
     if info:
         st.balloons()
    
    
if '4' in option:
     st.plotly_chart(fig4)
     info= st.checkbox("More info")
     if info: 
         st.write("The above VISUAL is a PIE CHART showing Strabucks prices rating")
     if info:
         st.balloons()
    
    
if '5' in option:
     st.plotly_chart(fig5)
     info= st.checkbox("More info")
     if info: 
         st.write("The above VISUAL is a TREEMAP showing covid deaths from 2020 to 2022")
     if info:
         st.balloons()
     
    


