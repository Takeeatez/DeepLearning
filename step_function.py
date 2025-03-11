# 계단 함수 구현하기
import numpy as np

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

print(step_function(5)) # 출력값 1
print(step_function(-3)) # 출력값 0