import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

plt.style.use('seaborn')

import warnings
warnings.filterwarnings(action='ignore')

st.set_option('deprecation.showPyplotGlobalUse', False)

class Preprocessing():
    #범주형 데이터를 수치형 데이터로 변환 ( 설립유형 인코딩 : 국공립 = 0, 사립 =1 )
    def encoding_type_1(self,data):
        univ_data = [data]
        found_mapping = {"국공립": 0, "사립": 1}
        for dataset in univ_data:
            dataset['설립유형'] = dataset['설립유형'].map(found_mapping)
        return data

    #범주형 데이터를 수치형 데이터로 변환 ( 설립유형 인코딩 : 수도권 = 0, 비수도권 =1 )
    def encoding_type_2(self,data):
        univ_data = [data]
        city_mapping = {"수도권": 0, "비수도권": 1}
        for dataset in univ_data:
            dataset['소재지유형'] = dataset['소재지유형'].map(city_mapping)
        return data

    #범주형 데이터를 수치형 데이터로 변환 (지역별 인코딩)
    def encoding_region(self,data):
        univ_data = [data]
        region_mapping = {"서울": 0, "경기": 1, "인천": 2, "경북": 3, "충남": 4, "부산": 5, "강원": 6, "충북": 7, "대전": 8, "전북": 9,
                          "전남": 10, "경남": 11, "광주": 12, "대구": 13, "세종": 14, "제주": 15, "울산": 16}
        for dataset in univ_data:
            dataset['지역명'] = dataset['지역명'].map(region_mapping)
        return data

    def eda_typeOfEstb(self,data,feature):
        st.markdown("""
                ### ❗**설립 유형 비율 확인(사립 & 공립)**
                """)

        f, ax = plt.subplots(1, 2, figsize=(20, 8))
        data[feature].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)

        ax[0].set_title(feature)
        ax[0].set_ylabel('')
        # print(ax[1])
        sns.countplot(feature, data=data, ax=ax[1])
        ax[1].set_title(feature)
        plt.show()
        st.pyplot()

    @staticmethod
    def bar_chart_founding(data,feature):
        national = data[data['설립유형'] == 0][feature].mean()
        private = data[data['설립유형'] == 1][feature].mean()

        x = ["국공립", "사립"]
        y = [national, private]

        plt.figure(figsize=(20, 10))
        colors = ['lightpink', 'cyan']
        plt.bar(x, y, color=colors)

        plt.title('설립유형별 ' + feature + ' 비교', fontsize=20)
        plt.xlabel('설립유형별')
        plt.ylabel(feature)

        for i, v in enumerate(x):
            plt.text(v, y[i], y[i], fontsize=15, color='blue', horizontalalignment='center',
                     verticalalignment='bottom')

        plt.show()
        st.pyplot()

    @staticmethod
    def plot_chart_founding(data,feature):
        national_feature = []
        private_feature = []
        for i in range(2011, 2021):
            national_i = data[(data["공시연도"] == i) & (data["설립유형"] == 0)][feature].mean()
            national_feature.append(national_i)
            private_i = data[(data["공시연도"] == i) & (data["설립유형"] == 1)][feature].mean()
            private_feature.append(private_i)

        year = []
        for i in range(2011, 2021):
            year.append(i)

        plt.figure(figsize=(20, 10))
        plt.plot(year, national_feature, color="lightpink", marker='o')
        plt.plot(year, private_feature, color="cyan", marker='o')
        plt.xlabel('년도')
        plt.ylabel(feature)
        plt.legend(['국공립', '사립'])
        plt.title('설립유형별 ' + feature + ' 변화', fontsize=15)
        plt.show()
        st.pyplot()

    @staticmethod
    def bar_chart_city(data,feature):
        city = data[data['소재지유형'] == 0][feature].mean()
        rural = data[data['소재지유형'] == 1][feature].mean()

        x = ["수도권", "비수도권"]
        y = [city, rural]

        plt.figure(figsize=(20, 10))
        colors = ['orange', 'green']
        plt.bar(x, y, color=colors)

        plt.title('소재지별 ' + feature + ' 비교', fontsize=20)
        plt.xlabel('소재지별')
        plt.ylabel(feature)

        for i, v in enumerate(x):
            plt.text(v, y[i], y[i], fontsize=15, color='blue', horizontalalignment='center', verticalalignment='bottom')

        plt.show()
        st.pyplot()

    @staticmethod
    def plot_chart_city(data,feature):
        city_feature = []
        rural_feature = []
        for i in range(2011, 2021):
            city_i = data[(data["공시연도"] == i) & (data["소재지유형"] == 0)][feature].mean()
            city_feature.append(city_i)
            rural_i = data[(data["공시연도"] == i) & (data["소재지유형"] == 1)][feature].mean()
            rural_feature.append(rural_i)

        year = []
        for i in range(2011, 2021):
            year.append(i)

        plt.figure(figsize=(20, 10))
        plt.plot(year, city_feature, color="orange", marker='o')
        plt.plot(year, rural_feature, color="green", marker='o')
        plt.xlabel('년도')
        plt.ylabel(feature)
        plt.legend(['city', 'rural'])
        plt.title('소재지별 ' + feature + ' 변화', fontsize=15)
        plt.show()
        st.pyplot()
