# 이전 예제에서 연산을 진행하다보면 공통 인덱스가 없어 NaN값이 들어가 반환하는데, 이런 상황을 피하기 위해 연산 메소드에 fill_value 옵션을 설정하여 적용한다
# 사용법 : Series1.add(Series2, fill_value=0) 덧셈
#          Series1.sub(Series2, fill_value=0) 뺄셈
#          Series1.mul(Series2, fill_value=0) 곱셈
#          Series1.div(Series2, fill_value=0) 나눗셈
# 리턴값 : 새로운 시리즈 반환

import pandas as pd
import numpy as np

# 딕셔너리 데이터로 판다스 시리즈 생성
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수 사칙연산 수행(연산 메소드)
sr_add = student1.add(student2, fill_value=0) # 덧셈
sr_sub = student1.sub(student2, fill_value=0) # 뺄셈
sr_mul = student1.mul(student2, fill_value=0) # 곱셈
sr_div = student1.div(student2, fill_value=0) # 나눗셈

# 사칙연산 결과를 데이터프레임으로 변환
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index=['덧셈', '뺼셈', '곱셈', '나눗셈'])
print(result)

# 결과값
# 국어     NaN
# 영어    80.0
# 수학    90.0
# dtype: float64


# 수학    80
# 국어    90
# dtype: int64


#        국어        수학    영어
# 덧셈   90.0   170.000  80.0
# 뺼셈  -90.0    10.000  80.0
# 곱셈    0.0  7200.000   0.0
# 나눗셈   0.0     1.125   inf

# 이때 inf는 무한대로 0으로 나눴을 때 나오는 값이다. 