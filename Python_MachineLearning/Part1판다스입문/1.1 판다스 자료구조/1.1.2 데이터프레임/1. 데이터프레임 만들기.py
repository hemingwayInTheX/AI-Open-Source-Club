# 데이터프레임
# 1. 2차원 배열
# 2. 데이터프레임의 열은 각각 시리즈 객체임
# 3. 시리즈를 열벡터라고 한다면, 데이터프레임은 2차원 벡터 또는 행렬임

# 데이터프레임 구조 예시                열 이름
#                      Column 0   Column 1   Column 2   Column 3
#           Index 0     Data 0     Data 0     Data 0     Data 0 
#           Index 1     Data 1     Data 1     Data 1     Data 1
# 행 인덱스 Index 2     Data 2     Data 2     Data 2     Data 2
#           Index 3     Data 3     Data 3     Data 3     Data 3
#           Index 4     Data 4     Data 4     Data 4     Data 4
#                         ↑          ↑          ↑          ↑
#                      시리즈 0   시리즈 1   시리즈 2   시리즈 3

# 데이터프레임은 행과 열을 나타내기 위해 두 가지 종류의 주소를 사용
# 행 인덱스 & 열 레이블

# 간단하게 이야기하자면 데이터프레임은 여러 개의 시리즈를 모아 놓은 집합으로 보면 된다.

# 딕셔너리 ( k : v ) => 데이터프레임 변환
# 사용법 : pandas.DataFrame(딕셔너리 객체)
# 리턴값 : 데이터프레임
# 추가로 딕셔너리의 값은 데이터프레임의 열이 되고, 딕셔너리의 카 값은 해당 열의 레이블이 된다.

import pandas as pd

# 열 이름을 key, 리스트를 value
dict_data = {'c0':[1,2,3],'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12]}

# 판다스 함수로 변환 
df = pd.DataFrame(dict_data)

# 타입 확인 및 출력
print(type(df))
print('\n')
print(df)

# 결과값
# <class 'pandas.core.frame.DataFrame'>


#    c0  c1  c2  c3
# 0   1   4   7  10
# 1   2   5   8  11
# 2   3   6   9  12