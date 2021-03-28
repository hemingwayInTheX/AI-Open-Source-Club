# 데이터프레임으로 변환할때 행 인덱스와 열 레이블 속성을 직접 정할 수 있음

#행 인덱스/열 레이블 설정
# 사용법 : pandas.DataFrame( 2차원 배열, index=행 인덱스 배열, columns=열 레이블 배열)
# 리턴값 : 매개변수로 넣어준 행 인덱스 배열과 열 레이블 배열으로 설정된 데이터프레임

import pandas as pd

df = pd.DataFrame([[15, '남', '공대'], [17, '여', '미대']], 
                    index=['곽기훈', '이현서'],
                    columns=['나이', '성별', '학교'])

print(df)
print(df.index)
print(df.columns)

# 결과값
#      나이 성별  학교
# 곽기훈  15  남  공대
# 이현서  17  여  미대
# Index(['곽기훈', '이현서'], dtype='object')
# Index(['나이', '성별', '학교'], dtype='object')

# 위의 예제를 통해서 df.index와 df.columns로 각각 행과 열을 접근할 수 있다.

# 데이터프레임의 행 인덱스와 열 이름 변경
# 행 인덱스 변경
# 사용법 : DataFrame 객체.index = 새로운 행 인덱스 배열
# 열 이름 변경
# 사욥법 : DataFrame 객체.columns = 새로운 열 레이블 배열

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df)
print(df.index)
print(df.columns)

# 결과값
#      연령 남녀  소속
# 학생1  15  남  공대
# 학생2  17  여  미대
# Index(['학생1', '학생2'], dtype='object')
# Index(['연령', '남녀', '소속'], dtype='object')


# 또한 데이터프레임에 rename() 메소드를 적용하면 행 인덱스 또는 열 이름의 일부를 선택하여 변경할 수 있다.

# 행 인덱스 변경
# 사용법 : DataFrame 객체.rename(index={기존인덱스:새 인덱스, ...})
# 열 이름 변경
# 사용법 : DataFrame 객체.rename(columns={기존 이름: 새 이름, ...})
# 리턴값 : 변경된 새로운 객체 반환
# 유의사항 : 원본 데이터프레임을 반환하는 것이 아니기 때문에 원본 객체를 변경하려면 inplace=True옵션을 사용해야한다.

import pandas as pd

df.rename(columns={'연령':'나이', '남녀':'성별', '소속':'학교'}, inplace=True)
df.rename(index={'학생1':'준서', '학생2':'현서'}, inplace=True)

print(df)

# 결과값
#     나이 성별  학교
# 준서  15  남  공대
# 현서  17  여  미대