# 데이터프레임에 어떤 숫자로 사칙연산을을 수행하면 모든 원소에 적용된다. 
# 사용법 : DataFrame 객체 + 연산자( +, -, *, / ) + 숫자
# 리턴값 : 새로운 데이터프레임 객체

import pandas as pd
import seaborn as sns # cmd창에서 pip install seaborn 

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 생성
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) # 첫 5행만 표시
print('\n')
print(type(df))
print('\n')

# 데이터프레임 숫자 10 더하기
addition = df + 10
print(addition.head())
print('\n')
print(type(addition))

# 결과값

#     age     fare
# 0  22.0   7.2500
# 1  38.0  71.2833
# 2  26.0   7.9250
# 3  35.0  53.1000
# 4  35.0   8.0500


# <class 'pandas.core.frame.DataFrame'>


#     age     fare
# 0  32.0  17.2500
# 1  48.0  81.2833
# 2  36.0  17.9250
# 3  45.0  63.1000
# 4  45.0  18.0500


# <class 'pandas.core.frame.DataFrame'>

# 데이터프레임의 크기와 모양은 변함없음