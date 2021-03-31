# 사례들
# 1. 생산 라인에서 제품 이미지를 분석해 자동으로 분류 
#       - 일반적으로 합성곱 신경망(CNN) 사용하여 수행
# 2. 뇌를 스캔하여 종양 진단하기
#       - 시맨틱 분할 작업
#       - 일반적으로 CNN을 사용하여 이밎의 각 픽셀을 분류(종양의 정확한 위치와 모양을 결정)
# 3. 자동으로 뉴스 기사 분류 
#       - 자연어 처리(NLP) 작업
#       - 더 구체적으로 텍스트 분류이며, 순환 신경망(RNN), CNN, 트랜스포머를 사용해 해결
# 4. 토론 포럼에서 부정적인 코멘트를 자동으로 구분
#       - 텍스트 분류 작업
#       - NLP 도구 사용
# 5. 긴 문서를 자동으로 요약
#       - 텍스트 요약이라 불리는 NLP의 한 분야, NLP 도구 사용
# 6. 챗봇 도는 개인 비서 만들기 
#       - 자연어 이해(NLU)와 질문-대답 모듈을 포함해 여러가지 NLP 컴포넌트가 필요
# 7. 다양한 성능 지표를 기반으로 회사의 내년도 수익 예측
#       - 회귀 작업
#       - 선형 회귀나 다항 회귀 모델, 회귀 SVM, 회귀 랜덤 포레스트, 인공신경망과 같은 회귀 모델을 사용하여 해결
#       - 이전 성증 지표의 시퀸스를 고려한다면 RNN, CNN 또는 트랜스포머를 사용할 수 있음
# 8. 음성 명령에 반응하는 앱 
#       - 음성 인식 작업
#       - 오디오 샘플을 처리해야하는데, 이는 길고 복잡한 시퀸스이므로 일반적으로 RNN, CNN 또는 트랜스포머 사용
# 9. 신용 카드 부정 거래 감지
#       - 이상치 탐지 작업
# 10. 구매 이력을 기반으로 고객을 나누고 각 집합마다 다른 마케팅 전략을 계획 
#       - 군집 작업
# 11. 고차원의 복잡한 데이터셋을 명확하고 의미 있는 그래프로 표현
#       - 데이터 시각화 작업
#       - 차원 축소기법을 많이 사용
# 12. 과거 구매 이력을 기반으로 고객이 관심을 가질 수 있는 상품 추천하기
#       - 추천 시스템
#       - 과거 구매이력을 인공 신경망에 주입하고 다음에 구매할 가능성이 가장 높은 상품을 출력하는 것이 한 방법
#       - 모든 고객의 구매 이력을 기반으로 훈련
# 13. 지능형 게임 봇 만들기
#       - 보통 강화 학습으로 해결
#       - 시간 지나면 주어진 환경에서 보상이 최대가 되는 행동을 선택하는 에이전트를 훈련하는 머신러닝의 한 분야
#       - 예 : 알파고
