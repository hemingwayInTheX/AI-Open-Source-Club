## #Lec2. Simple Linear Regression
### 1. Regression이란?
> "후퇴, 퇴보, 되돌아가다, 회귀" 등의 의미를 갖지만 "Regression toward the mean. 즉, 전체 평균으로 돌아가려는 특징이 있는 통계적 원리를 설명하는 말이다.  


### 2. Linear Regression
> 데이터를 가장 잘 대변하는 직선의 방정식을 찾는 것 ( Y = ax + b )


### 3. Hypothesis ( Linear )
> H(x) = Wx + b ( W = Weight, b = bias )


### 4. Cost
> 데이터의 값과 Hypothesis의 차이를 나타내는 값
> Cost(W, b) = $$\sum\limits_{i=1}^{m}({H(x)-y_i})^2


### 5. Goal : Minimize Cost
> 위의 내용에 대한 결과로 Learning이란 Cost를 정의하고 이를 최소화하는 과정을 말한다.