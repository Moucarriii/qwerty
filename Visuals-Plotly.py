import streamlit as st
import pandas as pd
import plotly.express as px 
st.title("Plotly Visualizations!!!")

#### Data For Charts

co2=pd.read_csv(r"C:\Users\abdal\Desktop\co2_emission_data.csv")
sb= pd.read_csv(r"C:\Users\abdal\Desktop\5visuals\Starbucks satisfactory survey_DATA.csv")
fig1= px.scatter(co2,x="Year",y="Co2 Emission",color="Country",hover_name="Country",title="Yearly Co2 Emission by Country")
fig2=px.histogram(co2,x="Year",y="Co2 Emission",color="Country",title="Co2 Emission per Year",hover_name="Country")
fig3=fig=px.bar(co2,x="Country",y="Co2 Emission",color="Country",animation_frame="Year",animation_group="Country",range_y=[0,9000000000])
fig4=px.pie(sb, values="How would you rate the price range at Starbucks?", names="Gender",title="Rating Starbucks Prices Based on Gender")


df = pd.DataFrame({
    'first column': ['1','2','3','4','5'],
   
    })
print(df)
option = st.selectbox(
    'Which Visualizations would you like to see?',
     df['first column'])

'You selected: ', option

if '1' in option :
    st.plotly_chart(fig1) 
    info= st.checkbox("More info")
    if info: 
        st.write("The above VISUAL is a SCATTER PLOT showing the  emission of CO2 of several Countries since 1940")
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
    
    

     
    


