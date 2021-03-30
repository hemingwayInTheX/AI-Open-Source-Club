## #Lec2. Simple Linear Regression
### 1. Regression이란?
> "후퇴, 퇴보, 되돌아가다, 회귀" 등의 의미를 갖지만 "Regression toward the mean. 즉, 전체 평균으로 돌아가려는 특징이 있는 통계적 원리를 설명하는 말이다.  


### 2. Linear Regression
> 데이터를 가장 잘 대변하는 직선의 방정식을 찾는 것
> $$
> y  = ax + b
> $$
> 


### 3. Hypothesis ( Linear )
> *W = Weight   /   b = bias
> $$
> H(x) = Wx + b
> $$
> 


### 4. Cost
> 데이터의 값과 Hypothesis의 차이를 나타내는 값  
> $$
> Cost(W, b) = \frac{1}{m}\sum\limits_{i=1}^{m}{(H(x_i)-y_i)^2}
> $$
> 


### 5. Goal : Minimize Cost
> 위의 내용에 대한 결과로 Learning이란 Cost를 정의하고 이를 최소화하는 과정을 말한다.


### 6. Gradient Descent Algorithm
> 보편적인 Cost 최소화 알고리즘   
> 초기값 부터 Weight, Bias 값의 기울기를 조정해 나가며 해당하는 방정식을 찾아간다.  
> *Gradient Tape : 변수들을 기록하는 역할이며, 후에 변수들에 대한 기울기 값. 즉, 미분값을 반환하기 위함  
> *Learning rate : Gradient 값을 얼마만큼 적용할지 정해주는 변수( 매우 작은 값을 사용 )  
> *Epoch : 반복회수
