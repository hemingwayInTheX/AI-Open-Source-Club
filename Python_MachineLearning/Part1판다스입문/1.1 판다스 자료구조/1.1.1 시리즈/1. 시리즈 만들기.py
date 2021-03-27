#시리즈는
# 1. 순차적으로 나열된 1차원 배열의 형태
# 2. 인덱스는 데이터 값과 일대일 대응. 이때 인덱스는 데이터값의 주소값으로, 인덱스를 알면
# 해당 데이터 값에 바로 접근 가능
# 3. 딕셔너리와 비슷한 구조(키와 값 {k:v})

#시리즈 만들기
# 딕셔너리와 구조가 비슷하기에 딕셔너리를 시리즈로 변환하는 방법을 자주 사용함. 
# 사용법 : pandas.Series(딕셔너리형 데이터) 
# 리턴값 : 시리즈 객체

#pandas 불러오기
import pandas as pd

#key:value 쌍으로 딕셔너리 생성 및 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

#판다스 Series() 함수로 딕셔너리를 시리즈로 변환 후 sr에 저장
sr = pd.Series(dict_data)

#sr 자료형 출력 
print(type(sr))
print('\n')

#sr에 저장된 값 출력
print(sr)
