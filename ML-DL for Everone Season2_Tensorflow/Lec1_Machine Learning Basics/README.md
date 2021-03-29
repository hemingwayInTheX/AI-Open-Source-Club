## #Lec1. Machine Learning Basics
### 1. Machine Learning
> 일종의 소프트웨어인데 Explicit Programming에서 Logic 안의 Rules를 일일이 프로그래밍 하는 것을 넘어서 프로그램 자체가 데이터를 학습해 스스로 문제를 해결하게 하는 기법


### 2. Supervised Learning
> Label이 정해져 있는 데이터( Training Set )를 가지고 학습.
>> ex) Cat / Dog / Mug / Hat Label이 달려있는 데이터를 학습해 분류하는 프로그램


### 3. Unsupervised Learning
> 주어진 데이터를 스스로 분류하고 학습하는 것
>> ex) Google news grouping, Word Clustering


### 4. Type of Supervised Learning
> a. **Regression**             - Predicting final exam socre based on time spent  

>>|X ( Hours )|Y ( Score )|  
>>|:--:|:--:| 
>>|10|90|
>>|9|80| 
>>|3|50| 
>>|2|30| 
> b. **Binary Classification**  - Pass / non-Pass based on time spent 

>>|X ( Hours )|Y ( Pass / Fail )|  
>>|:--:|:--:| 
>>|10|P|
>>|9|P| 
>>|3|F| 
>>|2|F| 
> c. **Multi-Label Classification**  - Letter grade( A, B, C, E and F ) based on time spent 

>>|X ( Hours )|Y ( Grade )|  
>>|:--:|:--:| 
>>|10|A|
>>|9|B| 
>>|3|D| 
>>|2|F| 
