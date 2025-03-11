# 신경망에서의 행렬곱 
import numpy as np

# 입력 데이터 (예: 3개의 샘플, 4개의 입력 특징)
X = np.array([[0.5, 0.2, 0.1, 0.7],
              [0.9, 0.3, 0.4, 0.5],
              [0.8, 0.5, 0.6, 0.3]])

# 가중치 행렬 (4개의 입력 → 3개의 뉴런)
W = np.array([[0.2, 0.8, -0.5],
              [0.7, -0.3, 0.1],
              [-0.6, 0.9, 0.4],
              [0.3, 0.2, -0.8]])

# 편향 벡터 (각 뉴런에 대한 편향 값)
b = np.array([0.1, -0.2, 0.5])

# 신경망의 순전파(Forward Propagation)
Z = np.dot(X, W) + b  # 행렬 곱 + 편향 추가

# 활성화 함수 (ReLU)
def relu(x):
    return np.maximum(0, x)

A = relu(Z)  # 활성화 함수 적용

# 결과 출력
print("입력 X:")
print(X)
print("\n가중치 W:")
print(W)
print("\n선형 변환 결과 Z = XW + b:")
print(Z)
print("\n활성화 함수 적용 후 출력 A:")
print(A)
