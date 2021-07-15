import streamlit as st
import pandas as pd
#from sidebar_value import Sidebar

# csv 파일 불러오기 및 결측치 처리
class LoadData():
    #파일 읽기
    def load_data(self):
        df = pd.read_csv('project.csv', encoding='CP949')
        return df
    #결측치 비율 확인 및 처리
    def missing_value(self,data):
        #각 특성마다 결측치의 총합 출력
        data.isnull().sum
        #결측치 비율 확인
        for col in data.columns:
            msperc = 'column : {:>10}\t Percent of NaN value: {: .2f}'.format(col,
                                                     100 * (data[col].isnull().sum() /
                                                     data[col].shape[0]))
            print('졸업생수 결측치 비율:',msperc)
        #'졸업생 수' 결측치 제거
        data = data.dropna()
        data_zero = data[
            (data['재학생수(학부)'] == 0) | (data['졸업생수(학부)'] == 0) | (data['전임교원수(학부+대학원)'] == 0) | (data['입학정원'] == 0) | (
                        data['정원내모집인원'] == 0) | (data['정원내지원자'] == 0) | (data['정원내입학자'] == 0) | (
                        data['정원내신입생충원율(%)'] == 0) | (data['경쟁률'] == 0)].index
        data = data.drop(data_zero)
        return data
    #필요없는 feature 삭제
    def drop_feature(self,data):
        data.drop(['대표학교코드', '대학구분', '설립구분', '학교상태', '기준년도', '입학정원',
                   '정원내모집인원', '정원내지원자'], axis=1,
                  inplace=True)
        return data
    #2008 ~ 2010년 sample 삭제
    def drop_year(self,data):
        dropYear = data[(data['공시연도'] >= 2008) & (data['공시연도'] <= 2010)].index
        data.drop(dropYear, inplace=True)
        return data
    #원자료 조건에 맞게 출력
    def display_raw_data(self,data,option):
        #조건에 따라 검색하면
        if option == "Yes":
            year_data = st.sidebar.selectbox('Year?', list(reversed(range(2010, 2021))))
            is_first = data['공시연도'] == year_data
            first_data = data[is_first]
            #지역별로 검색할지 설립유형으로 검색할지
            want_Raw = st.sidebar.radio("Kind", ["지역별", "설립유형"])
            #지역별 선택시
            if want_Raw == "지역별":
                type_data = st.sidebar.radio('Type?', ["비수도권", "수도권"])
                #수도권과 비수도권으로 구분해 검색조건 활성화
                if type_data == "수도권":
                    unique_loca = ["경기", "서울", "인천"]
                else:
                    unique_loca = ["강원", "경남", "경북", "광주", "대구", "대전", "부산", "세종", "울산", "전남", "전북", "제주", "충남", "충북"]
                select_loca = st.sidebar.selectbox('지역명', unique_loca)
                is_second = first_data['지역명'] == select_loca
                allData = first_data[is_second]
            #설립유형별로 검색할지
            else:
                type_data = st.sidebar.selectbox('Type?', ["사립", "국립"])
                is_second = first_data['설립유형'] == type_data
                allData = first_data[is_second]

            st.subheader(allData.shape)
            st.write(allData)
        else:
            st.subheader(data.shape)
            st.write(data)