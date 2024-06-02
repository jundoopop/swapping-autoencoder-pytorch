# Seoultech Campus Virtual Renewal - Fork

[Source - Swapping autoencoder for deep image manipulation](https://github.com/taesungp/swapping-autoencoder-pytorch)

위 라이브러리의 원리를 그대로 사용

## Motivation

평소에 Photoshop 의 생성형 AI를 이용한 사진 편집 기능의 원리를 이해하고자 했으며, 

위와 같은 소스의 예시를 보며 내가 원하는 사진의 스타일 적용도 궁금했음. 실제 포토샵 기능의 원리가 저 소스에서 적용됨

[Landscape Mixer 시연 영상](https://youtu.be/gsE3cLg8imI?si=2LGoziQu0ec0BtU9)


이렇게 실제 사진에 적용할 경우, 특히 건축 관련 분야에서 구체적인 도면을 만드는 작업에 임하기 전에 방향을 잡는데 큰 도움이 될 것이라 생각했음.

이 사진은 상단 링크 속 source의 readme 에서 가져온 예시임

![fork 한 소스의 예시 사진](https://camo.githubusercontent.com/67b4e0399bc4c2f2b51077db7391fbc6842750eb825e49b6005e111a5d6c7bdc/68747470733a2f2f74616573756e672e6d652f5377617070696e674175746f656e636f6465722f696e6465785f66696c65732f6368757263685f7374796c655f73776170732e676966)

## 적용 예시

### 사용한 텍스처

![크렘린궁](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrwbY1V-hVzeh24ht742wD-DHDkD_tkG34Tw&s)
![노트르담성당](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkL1z5YQJzSHOW4iuA6DPH2i_wqWh72O7SgQ&s)

### 서울과학기술대학교 정문
#### 원본
![정문](https://www.seoultech.ac.kr/storage/www/ckfinder/images/SNUST1649650141448.jpg)
#### 적용


### 서울과학기술대학교 미래관

### 


## 어려웠던 점

### 설치

프로젝트 제작의 대부분의 시간은 환경 설정에 쓰였다.

#### 1.PyTorch 설치

#### 2. CUDA 설정

CUDA 환경변수 설정

#### 3. Conda 에서 GPU 인식

#### 4. C++, C

C++ 컴파일러가 제대로 인식되지 않아 Visual Studio 2022 를 재설치하고, 컴파일러의 위치를 찾는 등의 시간이 소요됐다.

### 원리 이해

