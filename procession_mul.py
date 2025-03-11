# 행렬곱 예제
import numpy as np

def matmul(A, B):
    return np.dot(A, B)  # 또는 A @ B

# 예제 행렬
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 행렬 곱 실행
result = matmul(A, B)
print(result)
