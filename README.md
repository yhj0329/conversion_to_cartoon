# conversion_to_cartoon
OpenCV를 이용해서 이미지와 영상을 만화(cartoon) 스타일로 변환하는 프로그램이다.

## 기능
- 만화 이미지 효과를 늘리려면 edges를 구분할 수 있는 adaptiveThreshold가 민감해야 하기 때문에 C(임계값)을 낮춘다.
- 만화 이미지 효과를 줄이려면 edges를 구분할 수 있는 adaptiveThreshold가 둔감해야 하기 때문에 C(임계값)을 높인다.
- bilateralFilter의 sigmaColor는 색 공간에서 필터의 표준 편차이며 너무 크면 edge를 구분하지 못한다.
- bilateralFilter의 sigmaSpace는 좌표 공간에서 필터의 표준 편차이다.(100을 주면 가우시안 필터를 적용하는 것과 같다)

## 한계
- 강한 만화 이미지 효과를 주려고 adaptiveThreshold의 C(임계값)을 극한으로 낮추면 edge를 너무 많이 검출하기 때문에 오히려 지저분한 느낌을 받았다.
  그렇다고 너무 높이면 edge를 검출하지 않기 때문에 적당한 값을 찾는 것이 중요했다.
- edges를 살리며 smoothing을 하는 bilateralFilter는 원본 이미지와 영상에 noise가 없기 때문에 드라마틱한 변화를 가져오지 않아 만화 이미지 효과를 주는데는 미비한 역할을 하였다.
- edge를 너무 많이 찾으면 bitwise_and 연산에서 속도가 늦어져 원본 영상보다 영상 길이가 길어지는 현상이 나타났다.

## 이미지

#### 원본

![image](https://github.com/yhj0329/conversion_to_cartoon/assets/102153681/3f6d0f5a-a3f1-4c1b-9a2d-45e0b6894583)

#### 좋은 만화 이미지 & 나쁜 만화 이미지

<img width="1026" alt="result_image" src="https://github.com/yhj0329/conversion_to_cartoon/assets/102153681/3a0d293e-f583-42d1-bed5-39036686c0b2">

## 영상

#### 원본

https://github.com/yhj0329/conversion_to_cartoon/assets/102153681/57237dab-c5a3-4ffb-a674-b577390c8cd8

#### 좋은 만화 영상 & 나쁜 만화 영상

https://github.com/yhj0329/conversion_to_cartoon/assets/102153681/fdf7b3d8-def6-477f-86df-5f67fed261a6
