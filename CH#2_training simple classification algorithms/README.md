# ✔ 2.1.1 ~ 2.1.2 퍼셉트론 학습 규칙

머신러닝에서 __'기계에게 학습을 시킨다는 것'__ 은 __우리가 예측한 결과값과 가장 근사한 
결과를 내도록 합리적인 가중치와 편향을 탐색하는것__ 을 의미합니다.
> - w = 가중치
> - b = 편향

* Perceptron = 단위계단 함수 사용(최종입력이 임계값보다 크면 1 작으면 -1로 예측)
        
      1.  단위계단 함수는 예측값을 만드는 함수라 생각합시다.
       
      2.  fit 메서드에서 예측값을 기반으로 가중치 업데이트를 시키고, 이를 기반으로 다음
        
        입력값이 들어왔을 때 정확한 예측을 할 수 있도록 해줍니다.
     

예를 들어 학습률이 0.5, 곱셈계수가 2일 경우를 생각해봅시다.

위 식을 계산하면 업데이트 값이 -1이 나오는데, 이 업데이트된 가중치는 다음 입력 시에 활성이 덜 되어 0으로
정확히 예측하도록 합니다.
asdf
