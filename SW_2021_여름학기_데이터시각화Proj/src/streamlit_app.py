import openpyxl
import streamlit as st
import pandas as pd
from load_data import LoadData
from data_preprocessing import Preprocessing

#반환된 DataFrame을 univ_data에 저장 및 확인
univ_data = LoadData().load_data()
#데이터프레임 복사본
raw_data = univ_data.copy()
print(univ_data.tail(2))

#결측치 확인 및 결측치 제거 및 확인
univ_data = LoadData().missing_value(univ_data)
print(univ_data.tail(2))

#필요없는 특성 삭제 및 확인
univ_data = LoadData().drop_feature(univ_data)
print(univ_data.columns)

#2008 ~ 2011년 데이터 삭제 및 확인
univ_data = LoadData().drop_year(univ_data)
print(univ_data.tail(2))

#1) 설립유형 인코딩
univ_data = Preprocessing().encoding_type_1(univ_data)
print(univ_data['설립유형'])

#2) 소재지유형 인코딩
univ_data = Preprocessing().encoding_type_2(univ_data)
print(univ_data['소재지유형'])

#3) 지역별 인코딩
univ_data = Preprocessing().encoding_region(univ_data)
print(univ_data['지역명'])

#사이드바 메뉴 선택
st.sidebar.header("Menu")
menu = st.sidebar.selectbox('Want', ['home','RawData','Preprocessing & EDA','Graph'])
# option 1) home 선택
# option 2) 원자료 조회
# option 3) 데이터 전처리 조회
# option 4) 데이터 시각화 조회
if menu == "home":
    st.markdown("""
    # Home
    ***project***
    """)
elif menu == "RawData":
    st.title('RawData')
    user_option = st.sidebar.radio("조건검색 Yes or No",["Yes","No"])
    LoadData().display_raw_data(raw_data, user_option)
elif menu == "Graph":
    # option 1)설립유형별 그래프 시각화 확인
    # option 2)소재지별 그래프 시각화 확인
    option = st.sidebar.radio("User Want",["Type of Establishment","Type of Location","By Region"])
    if option == "Type of Establishment":
        chart = st.sidebar.selectbox("Want",["barchart", "lineplot"])
        if chart == "barchart":
            Preprocessing().eda_typeOfEstb(univ_data,'설립유형')
            Preprocessing().bar_chart_founding(univ_data,'재학생수(학부)')
            Preprocessing().bar_chart_founding(univ_data,'졸업생수(학부)')
            Preprocessing().bar_chart_founding(univ_data,'전임교원수(학부+대학원)')
            Preprocessing().bar_chart_founding(univ_data,'정원내입학자')
            Preprocessing().bar_chart_founding(univ_data,'정원내신입생충원율(%)')
            Preprocessing().bar_chart_founding(univ_data,'경쟁률')
        elif chart == "lineplot":
            Preprocessing().plot_chart_founding(univ_data,'재학생수(학부)')
            Preprocessing().plot_chart_founding(univ_data,'졸업생수(학부)')
            Preprocessing().plot_chart_founding(univ_data,'전임교원수(학부+대학원)')
            Preprocessing().plot_chart_founding(univ_data,'정원내입학자')
            Preprocessing().plot_chart_founding(univ_data,'정원내신입생충원율(%)')
            Preprocessing().plot_chart_founding(univ_data,'경쟁률')
    elif option == "Type of Location":
        chart = st.sidebar.selectbox("Want",["barchart", "lineplot"])
        if chart == "barchart":
            Preprocessing().eda_typeOfEstb(univ_data,'소재지유형')
            Preprocessing().bar_chart_city(univ_data,'재학생수(학부)')
            Preprocessing().bar_chart_city(univ_data,'졸업생수(학부)')
            Preprocessing().bar_chart_city(univ_data,'전임교원수(학부+대학원)')
            Preprocessing().bar_chart_city(univ_data,'정원내입학자')
            Preprocessing().bar_chart_city(univ_data,'정원내신입생충원율(%)')
            Preprocessing().bar_chart_city(univ_data,'경쟁률')
        elif chart == "lineplot":
            Preprocessing().plot_chart_city(univ_data,'재학생수(학부)')
            Preprocessing().plot_chart_city(univ_data,'졸업생수(학부)')
            Preprocessing().plot_chart_city(univ_data,'전임교원수(학부+대학원)')
            Preprocessing().plot_chart_city(univ_data,'정원내입학자')
            Preprocessing().plot_chart_city(univ_data,'정원내신입생충원율(%)')
            Preprocessing().plot_chart_city(univ_data,'경쟁률')
