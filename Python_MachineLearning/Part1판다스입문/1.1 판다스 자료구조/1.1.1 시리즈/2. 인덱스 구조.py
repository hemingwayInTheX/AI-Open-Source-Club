# 인덱스 구조는
# 1. 자기와 짝을 이루는 데이터 값의 순서와 주소를 저장
# 2. 활용가능하면 탐색, 정렬, 선택, 결합 등 데이터 조작 쉬워짐
# 3. 인덱스에는 크게 두 가지 종류가 있다.
#      a. 정수형 위치 인덱스(integer position)
#      b. 인덱스 이름(index name) or 인덱스 라벨(index label)
# 

# 시리즈 클래스의 index속성을 이용하여 인덱스 배열 선택
# 사용법 : Series객체.index

# 시리즈 클래스의 values 속성을 이용하여 데이터 값 배열 선택
# 사용법 : Series객체.values

# Series() 함수를 사용하여 파이썬 리스트를 시리즈로 변환할 수 있다.
# 하지만 이때 키처럼 인덱스로 변환될 값이 없다. 따라서 따로 정의가 없다면 인덱스(0, 1, 2)가 자동으로 지정됌

import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['20190-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 결과값
# 0    20190-01-02
# 1           3.14
# 2            ABC
# 3            100
# 4           True
# dtype: object

# 이를 활용하여 인덱스 배열과 데이터 값의 배열을 불러올 수 있다. 
# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)

# 결과 값
# RangeIndex(start=0, stop=5, step=1)


# ['20190-01-02' 3.14 'ABC' 100 True]