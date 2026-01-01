import numpy as np

#固定真實分佈p
p = np.array([0.2, 0.5, 0.3])

#初始化q
logits = np.random.randn(3)

#softmax函數，確保q是合法機率分佈
def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / np.sum(exp_z)

def cross_entropy(p, q):
    return -np.sum(p * np.log(q + 1e-12))  #防止log(0)

lr = 0.1

#梯度下降
for step in range(1000):
    q = softmax(logits)
    
    #cross entropy對logits的梯度
    grad = q - p
    
    #更新 logits
    logits -= lr * grad
    
    if step % 100 == 0:
        print(f"Step {step}")
        print("q =", q)
        print("Cross Entropy =", cross_entropy(p, q))
        print("-" * 40)

#最終結果
q_final = softmax(logits)
print("Final q:", q_final)
print("True p :", p)
