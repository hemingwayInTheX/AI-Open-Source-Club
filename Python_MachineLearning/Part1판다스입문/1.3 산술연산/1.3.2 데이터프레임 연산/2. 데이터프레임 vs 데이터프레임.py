# 데이터프레임 끼리의 연산은 동일한 위치의 원소끼리 계산한다.
# 사용법 : DataFrame1 + 연산자( +, -, *, / ) + DataFrame2
# 리턴값 : 새로운 데이터프레임
# 유의사항 : 데이터프레임 중에 매칭되지 않는 것이 있다면 NaN값을 출력

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail()) # 마지막 5행 표시
print('\n')
print(type(df))
print('\n')

# 데이터프레임 숫자 10 더하기
addition = df + 10
print(addition.tail()) # 마지막 5행 표시
print('\n')
print(type(addition))
print('\n')

# 데이터프레임끼리 연산하기(addition -df)
subtraction = addition - df
print(subtraction.tail()) # 마지막 5행 표시
print('\n')
print(type(subtraction))

# 결과값

#       age   fare
# 886  27.0  13.00
# 887  19.0  30.00
# 888   NaN  23.45
# 889  26.0  30.00
# 890  32.0   7.75


# <class 'pandas.core.frame.DataFrame'>


#       age   fare
# 886  37.0  23.00
# 887  29.0  40.00
# 888   NaN  33.45
# 889  36.0  40.00
# 890  42.0  17.75


# <class 'pandas.core.frame.DataFrame'>


#       age  fare
# 886  10.0  10.0
# 887  10.0  10.0
# 888   NaN  10.0
# 889  10.0  10.0
# 890  10.0  10.0


# <class 'pandas.core.frame.DataFrame'>