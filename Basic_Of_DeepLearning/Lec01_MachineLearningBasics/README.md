# Lec01_MachineLearningBasics

> ## What is ML?
* 자료, 현상에서 학습하는 프로그램
***
> ## Supervised/Unsupervised Learning
* Supervised Learning: labeled examples(cat,dog...)들을 활용하여 학습
* Unsupervised Learning: un-labeled data들을 활용... 기준이 정해지지 않고 기계 스스로 학습
> ## Traning Data Set?
1. Y라는 label과 X라는 data를 매개변수로 가지는 set이 있을 때, Y label들을 가지고 학습을 함.
2. X(test)가 들어오면, 그에 맞는 label을 정한다.
    - *AlphaGo 또 한, 수많은 기보 Traning Data Set을 학습. 상대가 바둑알을 두었을 때 data를 입력받아 그에 맞는 수를 두기에 Supervised Learning의 예라고 할 수 있다.*
> ## Types Of Supervised Learning
* 공부 시간에 따른 성적을 예측하는 것과 같은 regression(회귀).
* pass/non-pass와 같은 binary classification.
* A,B,C 학점제와 같은 multiclass(multi-label) classification.