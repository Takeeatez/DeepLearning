# 계단 함수 numpy 응용해서 구현하기
import numpy as np

def step_function(x):
    y = x > 0  # Boolean 배열 생성 (True, False)
    return y.astype(np.int32)  # 정수형으로 변환 (32비트 정수)


x = np.array([-3, -1, 0, 1, 3])
print(step_function(x)) # 0 0 0 1 1
