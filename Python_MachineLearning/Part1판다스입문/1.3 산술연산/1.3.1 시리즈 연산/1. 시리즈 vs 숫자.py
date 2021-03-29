# 판다스 객체의 산술연산은 3단계 프로세스를 거친다
# 1. 행/열 인덱스를 기준으로 모든 원소를 정렬
# 2. 동일한 위치에 있는 원소끼리 일대일 대응
# 3. 일대일 대응이 되는 원소끼리 연산 처리(대응되는 원소가 없으면 NaN)

# 시리즈 vs 숫자
# Series 객체 + 연산자( +, -, *, /) + 숫자
# 리턴값 : 시리즈의 개별 원소에 각각 숫자를 더하고 계산한 결과를 시리즈 객체를 반환
# 추가 : 덧셈 뺄셈 곱셈 나눗셈 모두 가능

import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 생성
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

# 학생의 과목별 점수를 200으로 나누기
percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))

# 결과값
# 국어    100
# 영어     80
# 수학     90
# dtype: int64


# 국어    0.50
# 영어    0.40
# 수학    0.45
# dtype: float64


# <class 'pandas.core.series.Series'>