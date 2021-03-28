# 열 1개 선택
# 사용법 :
#           1. DataFrame 객체["열 레이블"]
#           2. DataFrame 객체.열 레이블 *열 레이블이 꼭 문자열이여야함
# 리턴값 : 시리즈 객체 반환

# 열 n개 선택(데이터프레임 생성)
# 사용법 : DataFrame 객체[ [열1, 열2, ..., 열 n] ] 
# 리턴값 : 데이터프레임(리스트의 원소로 열 이름 한개만 있어도 2중 대괄호를 사용하는 것으로 데이터프레임 반환)

import pandas as pd

exam_data = { '이름' : ['서준', '우연', '민아'],
              '수학' : [ 90, 80, 70],
              '영어' : [ 95, 94, 56],
              '음악' : [ 54, 34, 23],
              '체육' : [ 100, 90, 100]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))

# 수학점수만 추출
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

# 영어 점수만 추출
english1 = df.영어
print(english1)
print(type(english1))

# 결과값
#    이름  수학  영어  음악   체육
# 0  서준  90  95  54  100
# 1  우연  80  94  34   90
# 2  민아  70  56  23  100
# <class 'pandas.core.frame.DataFrame'>
# 0    90
# 1    80
# 2    70
# Name: 수학, dtype: int64
# <class 'pandas.core.series.Series'>


# 0    95
# 1    94
# 2    56
# Name: 영어, dtype: int64
# <class 'pandas.core.series.Series'>

musich_gym = df[['음악', '체육']]
print(musich_gym)
print(type(musich_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

# 결과값
#    음악   체육
# 0  54  100
# 1  34   90
# 2  23  100
# <class 'pandas.core.frame.DataFrame'>


#    수학
# 0  90
# 1  80
# 2  70
# <class 'pandas.core.frame.DataFrame'>

# 범위 슬라이싱의 고급 활용
# 사용법 : DataFrame 객체.iloc[ 시작 인덱스:끝인덱스:슬라이싱 간격]
# 리턴값 : 슬라이싱 간격만큼 이동하면서 행값을 가지고옴

# 역순으로 하려면 슬라이싱 간격을 -1로 설정

