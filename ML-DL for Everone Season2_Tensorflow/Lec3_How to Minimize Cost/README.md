---
title: "Lec3_How to Minimize Cost"
tags:
  - Blog
  - MathJax
  - Jekyll
  - LaTeX
use_math: true
---

## # Lec3. How to Minimize Cost

### 1. Simplified Hypothesis

> $$
> H(x) = Wx
> $$
>
> $$
> Cost(W) = \frac{1}{m}\sum\limits_{m=1}^{i}(Wx_i-y_i)^2
> $$
>
> 

### 2. Gradient Descent Algorithm( 경사하강법 )

> W, b 값을 Update 하는 것으로 W에 Learning_rate * (Cost의 편미분 값)을 빼는 것을 반복해 주변 경사를 따라 낮은 곳으로 이동하게 하는 알고리즘

### 3. Local Minimum Problem

> 주변보다는 낮은 지점이지만 더 낮은 지점(Global Minimum)이 있는 경우 제대로된 최저점을 찾지 못하는 문제가 발생하는데 그렇기 때문에 Convex Function으로 만들어 주는 과정이 필요하다.