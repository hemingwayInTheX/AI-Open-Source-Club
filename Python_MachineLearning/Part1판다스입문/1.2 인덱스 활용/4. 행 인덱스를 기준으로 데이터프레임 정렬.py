# 행 인덱스를 기준으로 데이터프레임을 정렬할때는 sort_index() 메소드를 활용하면 된다. 이때 행 인덱스를 기준으로 데이터프레임의 값을 정렬한다
# 사용법 : DataFrame 객체.sort_index()
# 리턴값 : 새롭게 정렬된 데이터프레임을 반환한다. 
# 추가 : ascending 옵션을 사용하여 오름차순 또는 내림차순 설정가능
#        ascending=False : 내림차순 정렬
#        ascending=True  : 오름차순 정렬

import pandas as pd

# 딕셔너리 정의
dict_data = {'c0':[1,2,3],'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12]}

# 딕셔너리를 데이터프레임으로 변환 및 인덱스를 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 내림차순으로 행 인덱스 정렬
ndf = df.sort_index(ascending=False)
print(ndf)

# 결과값
#     c0  c1  c2  c3
# r0   1   4   7  10
# r1   2   5   8  11
# r2   3   6   9  12


#     c0  c1  c2  c3
# r2   3   6   9  12
# r1   2   5   8  11
# r0   1   4   7  10

# 추가로 특정 열의 데이터 값을 기준으로 데이터프레임을 정렬할 수 있는데, 이때 sort_values() 메소드를 활용하면 된다.
# 사용법 : DataFrame 객체.sort_values()
# 리턴값 : 새롭게 정렬된 데이터프레임 객체
# 추가 : ascending 옵션을 사용하여 오름차순 또는 내림차순 설정가능
#        ascending=False : 내림차순 정렬
#        ascending=True  : 오름차순 정렬


# c1 열을 기준으로 내림차순 정렬
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)

# 결과값
#     c0  c1  c2  c3
# r2   3   6   9  12
# r1   2   5   8  11
# r0   1   4   7  10