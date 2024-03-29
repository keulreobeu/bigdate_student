# word 2 vec

기존의 자연어 처리는 원핫 인코딩처럼 단어를 원자취급하여 단어간 유사성을 표현하지 못한 체 사용하였다.

대표적으로 통계적 언어 모델링에서 사용된 N-gram처럼 어떤단어가 어떻게 많이 사용되었다 정도만 알 수 있었다.

이는 원 핫 인코딩처럼 0과 1로만 표현하는 희소표현으로 인해 단어간 유사성을 표현하지 못하는 점에서 시작되었다.

word 2 vec는 이러한 문제를 해결하기 위해 다차원 공간에서 분산표현을 통해 문자의 백터를 학습 생성하여 코사인 유사도와 같이 유사성을 가질 수 있는 백터를 통해 단어의 정보를 저장하여 위의 문제를 해결하려 하였다.

word 2 vec에는 2가지 방법을 통해 학습하여 백터를 생성한다.

### CBOW(countinuous Bag of Words)
CBOW방식은 타겟 단어 주변의 단어를 이용하여 타겟 단어를 예측하는 방식입니다.
윈도우 크기가 2라면 타겟 단어 앞 뒤 2개씩 총 4개의 단어를 이용하여 가운데 단어를 예측하여 백터를 만듭니다.

### Skip-fram
CBOW와 반대로 중심단어를 통해 주변 단어를 예측하는 방식입니다.
윈도우가 2라면 중심단어 앞 뒤 2단어씩 4단어가 어떤 단어가 올 지 예측하여 백터를 만듭니다.




# Transformer
Transformer는 attention만 사용하여 seq2seq구로조 만든 인코더-디코더 모델입니다.
RNN모델을 사용한 것 보다 더 우수한 성능을 보여준다.

기존의 seq2seq모델의 한계는 입력시퀸스를 하나의 백터로 압축표현을 하고 디코더로 출력을 하고 이때 입력에서 일부 소실이 일어나서 이 소실을 보정하기 위해 매 시점마다 전체 입력 문장을 다시 참고하고 더 나아가 예측해야할 단어와 연관이 있는 부분을 더 집중하게 해주는 attention을 사용했다.

하지만 transformer는 이 attention만을 이용하여 모델을 만들어 사용하여 입력 손실을 막고 여러개의 인코더-디코더를 통해 여러 시점을 분석하고 연관성 있는 부분을 잘 학습할수 있게 되었습니다.

### Transformer의 구조
![image](https://github.com/keulreobeu/bigdate_student/assets/112425846/7e5d14b7-0034-4f69-b9f6-f7feae39bdb4)
인코더에 들어오기 전 임베딩을 통해 문장을 백터화 하여 단어로 쪼갠 뒤 각 단어들의 순서정보를 가지게 하는데 이를 포지셔널 인코딩을 진행 후 인코더에 진입한다.
그 후 Multi-head self-Attention을 진행하는데 각각의 Quert에 대에서 모든 Key의 유사도를 구하여 각 키에 맵핑되어 있는 Value에 반영해줍니다. 이러한 밸류를 가중치가 다른 여러개의 self-Attention을 통해 계산하고 이 결과의 가중합을 반환한다. 이 가중합을 통해 단어가 어떤 의미로 사용되었는지 유추가 가능하다. 
그 후 Position-wise Feed Forward Neural Network에 Attention의 값이 전달되고 입력된 동일한 크기의 행렬로 연산되어 반환됩니다.

마지막으로 각 Attention이나 FFNN을 진행후 add(잔차연결)과 Norm(정규화)를 진행합니다.

잔차연결은 각 행렬에 잔차를 덧셈연산을 하고 정규화를 통해 기울기를 조절하여 기울기 소실이나 기울기 폭주를 완화시키는 역할을 한다. 이는 반복적인 자기회귀 연산을 하는 트렌스포머에서 기울기소실이나 폭주를 막아주는 역할을 한다.

디코더도 인코더에서 처럼 입력을 단어를 임베딩하여 문장행렬을 입력받는다. 이때 들어가는 문장은 정답을 가지는 문장으로 정답이 없다면 학습하지 못한다. 그리고 인코더와 다르게 Masked Multi-head self-Attention을 통해 처리되는데 이는 문장의 일부를 가려 현재 시점보다 미래시점의 단어를 보지 못하게 하여 현재시점의 값만 다음 서브층으로 넘겨 줄 수 있도록 한다.

인코더에서 나온 출력과 디코더 첫번째 서브층에서 나오는 출력이 두번째 서브층으로가게 되는데 비슷한 Multi-head Attention이지만 서로다른곳에서 온 값을 이용함으로 self가 아니다.  self-Attention은 Key, Value, Query모두 자기의 것을 사용하지만 디코더의 Attention의 Query는 첫번째 서브층에서 나온 Query를 사용하여 계산한다.

세번째 서브층인 FFNN을 통과한 후 나온 out put을 이용하여 정답을 만들고 자기회귀학습을 통해 학습을 진행한다.



# BERT 
BERT는 google에서 제안한 대용량의 레이블링되지 않은 데이터를 이용하여 사전학습을 진행하고, 레이블이 있는 다른 작업데이터와 함께 하이퍼파라미터를 재조정하여 모델의 성능을 높이는 과정이 있는데 이를 파인튜닝이라 한다.

BERT의 기본 구조는 트랜스포머의 인코더를 쌓아올린 구조이고, 많이쌓을 수록 self-Attention heads가 커진다.

특징으로는 문맥을 반영한 임베딩을 사용하고 있다. BERT는 트랜스포머처럼 왼쪽에서 오른쪽으로 마스킹을 하여 순차적으로 답을 찾는것이 아닌 임의로 일정량을 마스킹하여 그 빈칸의 단어를 알아내는 방식으로 학습을 한다.

구조는 transformer의 인코더층을 쌓아 올린것 처럼  self-Attention과 FFNN을 가지는 레이어층을 지나며 학습을 한다.

BERT는 사전에 등록된 단어가 아니더라도 단어를 있는 토큰단위로 쪼개어 임베딩하는데, 단어를 알고있는 원소단위로 쪼개어 서브워드를 만들고 이렇게 등장한 서브워드를 통해 토큰을 저장한다.
이러한 토큰 저장을 보고 나중에 직접 지정을 할 수 도 있다.

BERT의 포지서녈 임베딩은 트랜스포머의 포지셔널 인코딩과 유사한 다른 방법을 통하여 위치를 저장한다. 인코딩처럼 코사인, 사인 함수를 이용하여 만드는 것이 아닌 학습을 통해 임베딩 백터를 만들어 위치를 저장한다. 예를들어 문장의 단어 길이가 4라면 4개의 임베딩 백터를 이용하여 위치를 저장한다. 물론 BERT는 문장의 길이를 512를 최대 길이고 하고 있어 512개의 포지션 백터를 이용하여 위치를 저장한다.

### 마스크드 언어 모델
BERT는 사전훈련을 위해 입력텍스트의 15%의 단어를 랜덤으로 마스킹하고 인공신경망에게 가려진 단어를 예측하도록 합니다.
그렇다고 15%중 전체를 mask하여 학습하지 않고 대부분은 mask로 일부는 랜덤으로 나머지 일부는 변경하지 않고 학습을 한다.

### 다음 문장 예측
BERT는 단어를 학습한 후 문장을 학습하는데, 두 문장이 이어지는지 학습하는 과정이다. 이때 이어지는 문장 50% 이어지지 않는 문장50%를 주어 학습을 한다. 이때 두 문장은 SEP라는 토큰을 통해 구분된다.

다음문장 예측과 같이 문장들을 구분을 해줘야 하기 때문에 세그먼트 임베딩이라는 임베딩층을 하나 더 만들게 된다. SEP토큰을 기준으로 첫번째 문장은0 두번째 문장은1 처럼 2개의 임베딩백터를 더해주는 방식이다. 

BERT의 파인튜닝은 크게 4가지 방법이 있다.

### 하나의 텍스트에 대한 텍스트 분류 유형
대표적으로 영화의 감성분류, 문서 시작에 CLS라는 토큰을 넣고 그 토큰의 값이 어떻게 되는지(리뷰점수 등을 통해 긍부정 라벨링)예측하는 방법

### 하나의 텍스트에 대한 태깅 작업
각 텍스트에 대해서 품사가 어떻게 되는지 태깅하는 예측하는 방법 맨앞에 CLS 뒤에 SEP토큰을 넣는다.

### 텍스트의 쌍에 대한 분류 또는 회귀문제
두 문장이 주어졌을때 하나의 문장이 다른 문장과 어떤 관계(모순, 함, 중립)인지 추론해내는 방법 시작에 CLS토큰 문장사이와 끝에 SEP토큰을 넣어 학습한다.

### 질의 응답
두 문장중 앞의 문장이 질문이면 뒤의 문장이 답변이 오도록 학습한다. 토큰은 전과 같음



# GPT
트랜스포머의 디코더를 활용한 자동 회귀 언어 모델로 단어들을 제시하면 그 뒤에 나올 단어들을 예측하여 문장을 만들어 내는 모델을 말한다. 

GPT는 이러한 다음 단어(낱말)맞추기를 계속 학습시켜 만든 사전학습 모델이다.

방대한량의 문서를 순차적으로 학습하여 라벨링이 없이 진행하였지만 문서들 중에선 질의를 하면 응답을 하는 것 같은 데이터가 있어 기본적으론 Zero-shot Learning이지만 정답을 가지는 데이터도 있어 메타학습이라고 한다.

GPT모델을 사용하여 작업을 시키는 방법은 크게 3가지 방법을 가지고 있다.

### 제로샷 러닝
데이터에 라벨링이 전혀 없이 문서만 주어서 나머진 스스로 결과를 만드는 방법

### 원 샷러닝
데이터에 라벨링을 하나만 주어 나머지는 나머진 스스로 결과를 만드는 방법

### 퓨샷러닝
각 정답별 힌트(10~20개정도)라벨링을 하여 나머진 스스로 결과를 만드는 방법

이러한  GPT의 사전훈련모델을 이용하여 주로 텍스트 생성, 기계번역, 질의응답, 자연어 이해, 대화형시스템, 요약, 작문보조, 챗봇, 감정분석, 콘텐츠필터링 등 자연어와 관련된 작업을 시킬 수 있습니다.
