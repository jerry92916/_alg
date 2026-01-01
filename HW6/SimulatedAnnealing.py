import numpy as np
import random

x = np.array([26, 25, 20, 23, 28, 28, 29, 30, 28, 35, 36, 33, 29, 27, 30, 33, 22, 20, 19, 22, 23, 29, 30, 33, 28, 33, 31, 38, 26, 22])
y = np.array([3000, 2000, 2150, 1500, 5500, 6000, 5123, 6010, 6648, 7001, 7214, 7101, 6812, 5651, 6468, 7510, 4031, 3984, 1594, 4010, 3151, 5413, 6641, 6847, 7000, 6413, 7300, 7701, 3101, 3100])

def improved_sa(x, y, iterations=50000):
    b0, b1 = 0.0, 0.0
    current_mse = np.mean((y - (b0 + b1 * x)) ** 2)
    t = 1000.0 # 溫度
    
    for i in range(iterations):
        t *= 0.99 # 降溫
        next_b0 = b0 + random.uniform(-5, 5)
        next_b1 = b1 + random.uniform(-5, 5)
        next_mse = np.mean((y - (next_b0 + next_b1 * x)) ** 2)
        
        # 如果變好，或機率性接受變差的解
        if next_mse < current_mse or random.random() < np.exp((current_mse - next_mse) / (t + 1e-9)):
            b0, b1, current_mse = next_b0, next_b1, next_mse
    return b0, b1

b0, b1 = improved_sa(x, y)
print(f"【改良法(模擬退火)】截距: {b0:.4f}, 斜率: {b1:.4f}")
