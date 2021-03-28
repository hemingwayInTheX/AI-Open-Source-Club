# 데이터프레임의 행 또는 열을 삭제하려면 drop() 메소드를 이용하면 된다.

# 행/열 삭제
# 행 삭제
# 사용법 : DataFrame 객체.drop(행 인덱스 또는 배열, axis=0)
# 열 삭제 
# 사용법 : DataFrame 객체.drop(열 레이블 또는 배열, axis=1)
# 리턴값 :새로운 객체 생성, 원본 객체 변경을 원하면 inplace=True 옵션 추가
# 유의사항 : 
    # 1. 행을 삭제할 때는 axis 옵션으로 axis=0을 입력 또는 별도로 입력 안함
    # 2. 열을 삭제할 때는 axis 옵션을 axis=1로 해야한다
    # 3. 동시 삭제를 원할 경우

import pandas as pd 

# DataFrame() 함수로 데이터프레임 변환
exam_data = {'수학' : [90, 80, 70], '영어':[98, 45, 23],
             '음악' : [56, 75, 43], '체육':[100, 100, 100]}
df = pd.DataFrame(exam_data, index=['나', '너', '우리'])
print(df)

# 데이터프레임 df 복사 후 df2의 1개 행(너) 삭제
df2 = df[:]
df2.drop('너', inplace=True)
print(df2)

# 데이터프레임 df 복사 후 df3의 2개 행(너와 우리) 삭제
df3 = df[:]
df3.drop(['너', '우리'], axis=0, inplace=True)
print(df3)

# 결과값
#     수학  영어  음악   체육
# 나   90  98  56  100
# 너   80  45  75  100
# 우리  70  23  43  100

#     수학  영어  음악   체육
# 나   90  98  56  100
# 우리  70  23  43  100

#    수학  영어  음악   체육
# 나  90  98  56  100

# 더 나아가 df3.drop()부분에 inplace=True 대신 df3 = df3.drop([위와 동일])을 해도 결과는 동일하다

# 열 삭제
import pandas as pd

# df4의 1개 열 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)

# df5의 2개 열 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)

# 결과값
#     영어  음악   체육
# 나   98  56  100
# 너   45  75  100
# 우리  23  43  100

#     수학   체육
# 나   90  100
# 너   80  100
# 우리  70  100