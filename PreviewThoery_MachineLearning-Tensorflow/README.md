# How to use <Tensorflow1.9.0>?

## <span style="color:green">What is "Tensor"?</span>
텐서는 수학적으로 어렵게 접근하면 "아무 차원이나 갖을 수 있는 값들의 집합", "다차원 배열의 일반화"라고 설명할 수 있지만,
여러개의 행렬(Matrix)들이 모인 "행렬 집합(Set of Matrix)"이라 생각하면 직관적으로 해당 개념을 받아들일 수 있을 것이다.
좀 더 쉽게 예시를 들면, '벡터','행렬','텐서'라는 공장이 있다고 가정을 하자. 벡터라는 공장은 오직 하나의 컨베이어 벨트만, 
행렬공장은 두 개의 컨베이어 벨트, 텐서공장은 세 개의 컨베이어 벨트가 있다. 어떤 공장이 하루 생산량이 더 많을까? 당연히
텐서공장의 하루 생산량이 가장 높을 것이다. 이와 같은 예시는 '텐서'가 머신러닝과 딥러닝을 구현하는데 있어 수 많은 데이터를
처리하고 표현하는데 적합한 자료형이라는 것을 보여주기 위함이다. 명확한 결론을 내리자면!! 텐서란 2차원 형태의 배열인 행렬, 
그 이상의 다차원의 배열임과 동시에 머신러닝과 딥러닝에서 의미하는 '데이터'라 생각하자!

## <span style="color:green">What is "Tensorflow"?</span>
자 그럼 텐서라는 의미를 파악했으면 도대체 {Tensor+flow}는 무엇일까? 우선 이것도 어렵게 설명하자면 "데이터 흐름 그래프를 
사용하여 수치 연산을 해주는 라이브러리"라 할 수 있다.....데이터 흐름? 그래프? 현시점에서 README를 작성하는 필자의 입장에서
저 개념들은 쉽게 와닿지 않는다. 하지만 위에서 들었던 공장 예시를 끌고오면 텐서공장에는 포장을 하는 3개의 컨베이어 벨트 뿐만 
아니라, 포장 후 위생상태 검사 및 품질 검사 등 이후 다양한 작업들이 남아있다. 즉 특정 공장에서 수 많은 제품들을 생산하기 위한
생산 공정의 흐름, 그 '흐름'의 결과로 인해 완제품들이 탄생한다. 이에 기반해서 다시 텐서플로우로 돌아오면! 텐서 형태의 데이터
(제품)들이 연산들의 그래프 흐름(공정 절차)에 따라 연산(공정 내용)이 이루어지는 것이라 볼 수 있다. 음..텐서플로우에 대한 자세한
이해는 본인도 좀 더 알아보고 다시 업로드해야겠다..

## Basic syntax of Tensorflow1.9.0
### 1. About session
텐서플로우의 연산은 좀 특이하다. 여기에서 연산은 단순히 피연산자들끼리 덧셈,뺄셈,곱셈과 같은 기존의 사칙연산으로 생각하면 안된다.
먼저 텐서플로우는 연산을 그래프로 표현하는데, 즉 연산을 바로 실행하는 것이 아니라 그래프로 먼저 변환한 다음 그래프의 실행 결과를 
반환 받는 것이라 생각하자...(어렵다..) 일단! "Tensorflow의 연산은 기존의 사칙연산과는 다르다"라고만 받아들이자. 다시 돌아와서
방금 그래프의 실행 결과를 반환 받는다고 했는데 바로 session이 그래프가 실행 결과를 받을 수 있도록 작동해주는 녀석이다. 그냥 
텐서들이랑 연산할려면 session이 필요하다고 이해하자. 그럼 아래의 코드를 보자.
<pre>
<code>
a=tf.constant(1)
b=tf.constant(2)
c=tf.add(a,b)
sess=tf.Session()
sess.run(c)
</code>
</pre>
a,b에 뭘 담고, c에 둘이 더한걸 저장했더니 sess라는 이상한놈이 보이는데, 저게 바로 session을 통한 텐서들간의 연산과정을 간단하게 보여주는 코드다.
4번째와 5번째줄을 유심히 보자.
<pre>
<code>
sess=tf.Session()
</code>
</pre>
텐서플로우 session을 준비했다. 그니까 연산할 준비를 마친것이다.
<pre>
<code>
sess.run(c)
</code>
</pre>
준비 마쳤으니까 인자값에 연산결과를 보여줄 텐서를 던져주고 실행한다. 그렇다면 아래와 같은 코드를 돌리면 어떤 결과가 나올까?
<pre>
<code>
sess.run(1+2)
</code>
</pre>
<pre>
<code>
~\anaconda3\envs\machineLearning\lib\site-packages\tensorflow\python\client\session.py in __init__(self, fetches, contraction_fn)
    284         raise TypeError('Fetch argument %r has invalid type %r, '
    285                         'must be a string or Tensor. (%s)' %
--> 286                         (fetch, type(fetch), str(e)))
    287       except ValueError as e:
    288         raise ValueError('Fetch argument %r cannot be interpreted as a '

TypeError: Fetch argument 3 has invalid type <class 'int'>, must be a string or Tensor. (Can not convert a int into a Tensor or Operation.)

</code>
</pre>
텐서플로우에게 1+2를 던져줬더니 오류가 난다. 앞서 말했듯이 session은 텐서들이 서로 연산하기 위한 일종의 장치이다. 연산하고자 하는 대상들이 텐서들이 아니면
session은 취급하지 않는다. 따라서 텐서플로우를 사용하는 이상 우리가 특정 연산을 하기 위해서는 텐서를 만드는 것이 가장 중요하다. 정리하자면 데이터가 'flow'하게
만드는 동작을 바로 session이 수행하는 것이다.(Tensorflow2.x버전 이상부터는 session이 사라졌다...ㅠ)

### 2.About Constant
텐서플로우도 C,C++,JAVA와 마찬가지로 상수와 변수 기능을 제공한다.(물론 필자는 똑같다해도 좀 다른 느낌이 든다) 상수는 constant()메서드를 이용해 정의한다. 아래 코드를
보자.
<pre>
<code>
a=tf.constant([5],dtype=tf.float32)
b=tf.constant([10],dtype=tf.float32)
c=tf.constant([2],dtype=tf.float32)

d=a*b+c
print(d)
</code>
</pre>

constant메서드의 각 인자들이 정의되는 내용을 보면 다음과 같은데
* value : 값(그냥 넣고싶은 값)
* dtype : 상수의 데이터형. 보통 float.32를 많이 쓴다.(이건 모르겠다ㅠ)
* shape : 행렬의 차원을 만들어줌
* name : 상수의 이름을 만들어준다..?
(사실 이 부분은 스터디멤버들과 같이 논의할 필요가 있다ㅠㅠ(그냥 모르겠다!))
그러면 이제 위 코드를 실행하면 print(d)결과가 뭘까? 
<pre>
<code>
Tensor("add_8:0",shape(1,),dtype=float32)
</code>
</pre>
우리가 통상 터미널에서 확인할 수 있는 어떤 숫자가 아닌 괴랄한 놈이 나온다. 이유가 뭘까? 저 위 session에서 말했듯이 텐서플로우는 데이터의 흐름을 그래프로 표현한 것이고, session은
그러한 동작을 해주도록 만드는 장치라 했다. 다시 말하면 (d=a*b+c)는 계산을 수행하는 것이 아니라 (a*b+c)그래프를 만들어주는 것이다. 일단 단순 사칙연산을 하지 않는다는 흐름을 기억하자!
