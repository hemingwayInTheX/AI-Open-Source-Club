# Lec02_LinearRegression

> ## Linear Regression? (선형회귀)
Regression 모델의 Training Data Set을 정열해 놓고, H(x)=Wx+b 공식을 갖는 직선들 중 Data Set 정렬과 인접한 선을 탐색한다. 직선들을 Linear Hypothesis라 함. (예측값)

> ## Cost Function
- How fit the line to our data? ... (H(x)-y)^2
- Data와 Linear Hypothesis간의 거리를 구하고, Data 총 개수 m으로 나누는 것 그것이 Cost.

> ## Goal
minimize cost(W,b)를 구하는 것이 목표이다. 즉, cost를 최소화하는 W와 b를 구하는 것이 Linear regression의 학습 목표라고 할 수 있다. 이는 많은 Algorithm을 통해 성취할 수 있다.
