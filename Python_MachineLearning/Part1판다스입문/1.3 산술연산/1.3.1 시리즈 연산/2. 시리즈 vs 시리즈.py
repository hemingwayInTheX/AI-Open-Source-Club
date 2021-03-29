# 시리즈와 시리즈 사이에 사칙연산은 시리즈의 모든 인덱스에 대하여 같은 인덱스를 가진 원소끼리 계산한다
# 사용법 : Series1 + 연산자( +, -, *, / ) + Series2
# 리턴값 : 새 시리즈 반환
# 특이사항 : 과목명의 순서가 달라도 판다스는 같은 인덱스를 찾아 정렬한 후 같은 인덱스의 데이터 값끼리 사칙연산을 수행한다.   
#            또한 연산을 하는 두 시리즈의 원소 개수가 다르거나, 크기가 같더라도 인덱스 값이 다를 경우 매칭되는 인덱스를 제외하고 NaN값이 들어간다.

import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 생성
student1 = pd.Series({'영어':80, '국어':100, '수학':90})
student2 = pd.Series({'국어':70, '영어':90, '수학':60})
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 고막별 점수로 사칙연산
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

# 사칙연산 결과를 데이터프레임으로 생성(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# 결과값
# 국어    100
# 영어     80
# 수학     90
# dtype: int64


# 국어    70
# 영어    90
# 수학    60
# dtype: int64


# <class 'pandas.core.series.Series'>


#               국어           영어      수학
# 덧셈    170.000000   170.000000   150.0
# 뺄셈     30.000000   -10.000000    30.0
# 곱셈   7000.000000  7200.000000  5400.0
# 나눗셈     1.428571     0.888889     1.5

import numpy as np

# 딕셔너리 데이터로 판다스 시리즈 생성
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수 사칙연산 수행
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

# 사칙연산 결과를 데이터프레임으로 생성(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# 결과값

# 국어     NaN
# 영어    80.0
# 수학    90.0
# dtype: float64


# 수학    80
# 국어    90
# dtype: int64


# <class 'pandas.core.series.Series'>


#      국어        수학  영어
# 덧셈  NaN   170.000 NaN
# 뺄셈  NaN    10.000 NaN
# 곱셈  NaN  7200.000 NaN
# 나눗셈 NaN     1.125 NaN