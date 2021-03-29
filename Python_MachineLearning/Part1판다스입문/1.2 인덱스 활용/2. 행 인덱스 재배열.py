# 행 인덱스 재배열은 reindex() 메소드를 이용하면 데이터프레임의 행 인덱스를 새로운 배열로 재지정할 수 있다.
# 사용법 : DataFrame 객체.reindex( 새로운 인덱스 배열 )
# 리턴값 : 새로운 데이터프레임 객체를 반환
# 유의사항 : 기존 데이터프레임에 존재하지 않는 행 인덱스가 새롭게 추가되는 경우면 그 행의 데이터
#            값은 NaN 값이 된다. 따라서 이 값을 대신해서 유효한 값을 넣어주려면 아래 예제와 같이
#            fill_value=0(원하는 값) 와 같이 옵션을 입력해줘야 한다.

import pandas as pd

# 딕셔너리 정의
dict_data = {'c0':[1,2,3],'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12]}

# 딕셔너리를 데이터프레임으로 변환 및 인덱스를 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 인덱스를 r0 ~ r4로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

# reindex로 발생한 NaN 값을 숫자 0으로 채우기
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)

# 결과값
#     c0  c1  c2  c3
# r0   1   4   7  10
# r1   2   5   8  11
# r2   3   6   9  12


#      c0   c1   c2    c3
# r0  1.0  4.0  7.0  10.0
# r1  2.0  5.0  8.0  11.0
# r2  3.0  6.0  9.0  12.0
# r3  NaN  NaN  NaN   NaN
# r4  NaN  NaN  NaN   NaN


#     c0  c1  c2  c3
# r0   1   4   7  10
# r1   2   5   8  11
# r2   3   6   9  12
# r3   0   0   0   0
# r4   0   0   0   0