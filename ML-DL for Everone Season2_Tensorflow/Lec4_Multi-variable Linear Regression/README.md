## Lec4. Multi-variable Linear Regression

### 1. Predicting exam score : Regression using one input(x)

> | X ( Hours ) | Y ( score ) |
> | :---------: | :---------: |
> |     10      |     90      |
> |      9      |     80      |
> |      3      |     50      |
> |      2      |     60      |
> |     11      |     40      |



### 2. Predicting exam score : Regression Using three inputs(x1, x2, x3)

> | x1 ( quiz 1 ) | x2 ( quiz 2 ) | x3 ( midterm 1 ) | Y ( Final ) |
> | :-----------: | :-----------: | :--------------: | :---------: |
> |      73       |      80       |        75        |     152     |
> |      93       |      88       |        93        |     185     |
> |      89       |      91       |        90        |     180     |
> |      96       |      98       |       100        |     196     |
> |      73       |      66       |        70        |     142     |



### 3. Multi-variable

> w1x1 + w2x2 + w3x3 + ... + wnxn과 같이 길고 복잡하게 쓰지 않고 Matrix Multiplication( Dot Product )를 이용해 간단하게 표현한다. ( H(X) = XW )