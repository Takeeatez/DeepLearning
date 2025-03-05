# AND 게이트 구현 프로그램

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # 각 매개변수 w1, w2는 theta 안에서 초기화
    tmp = x1*w1* + x2*w2
    if tmp <= theta: 
        return 0
    elif tmp > theta:
        return 1
    

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))