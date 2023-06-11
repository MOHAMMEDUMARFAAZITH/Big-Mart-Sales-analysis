import pickle
import xgboost
import streamlit as st
from streamlit_option_menu import option_menu
Sales_model = pickle.load(open("Big_mart_sales_prediction.sav","rb"))
with st.sidebar:
	
	selected = option_menu("sales_prediction",["Big_mart_sales_prediction"],default_index=0)

if (selected == "Big_mart_sales_prediction"):
	st.title("Big_mart_sales_prediction using ML")
	col1, col2= st.columns(2)
	with col1:
		Item_Weight = int(st.number_input('Item_Weight'))
	with col2:
		Item_Fat_Content = int(st.number_input('Item_Fat_Content'))
	with col1:
		Item_Visibility = int(st.number_input('Item_Visibility'))
	with col2:
		Item_Type = int(st.number_input('Item_Type'))
	with col1:
		Item_MRP = int(st.number_input('Item_MRP'))
	with col2:
		Outlet_Identifier = int(st.number_input('Outlet_Identifier'))
	with col1:
		Outlet_Establishment_Year = int(st.number_input('Outlet_Establishment_Year'))
	with col2:
		Outlet_Size = int(st.number_input('Outlet_Size'))
	with col1:
		Outlet_Location_Type = int(st.number_input('Outlet_Location_Type'))
	with col2:
		Outlet_Type = int(st.number_input('Outlet_Type'))
	Item_Outlet_Sales = Sales_model.predict([[Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type]])
	print(jsonify({'Prediction': int(Item_Outlet_Sales)}))
	
