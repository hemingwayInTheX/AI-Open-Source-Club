# 행 인덱스 초기화는 reset_index() 메소드를 활용하여 행 인덱스를 정수형 위치 인덱스로 초기화할 수 있다. 이때 기존 행 인덱스는 열로 이동한다.
# 사용법 : DataFrame 객체.reset_index()
# 리턴값 : 새로운 데이터프레임 객체

import pandas as pd

# 딕셔너리 정의
dict_data = {'c0':[1,2,3],'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12]}

# 딕셔너리를 데이터프레임으로 변환 및 인덱스를 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 행 인덱스를 정수형으로 초기화
ndf = df.reset_index()
print(ndf)

# 결과값
#     c0  c1  c2  c3
# r0   1   4   7  10
# r1   2   5   8  11
# r2   3   6   9  12


#   index  c0  c1  c2  c3
# 0    r0   1   4   7  10
# 1    r1   2   5   8  11
# 2    r2   3   6   9  12
