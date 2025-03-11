# ReLu(렐루) 함수 구현
import numpy as np
import matplotlib.pyplot as plt  
# ReLU 함수 정의
def relu(x):
    return np.maximum(0, x)

# x 값 설정 (-5에서 5까지 100개)
x = np.linspace(-5, 5, 100)
y = relu(x)  # ReLU 함수 적용

# 그래프 그리기
plt.plot(x, y, label="ReLU Function", color="blue", linewidth=2)
plt.axhline(0, color="black", linestyle="--", linewidth=1)  # x축
plt.axvline(0, color="black", linestyle="--", linewidth=1)  # y축
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.title("ReLU Activation Function")
plt.grid(True)  # 격자 추가
plt.legend()
plt.show()
