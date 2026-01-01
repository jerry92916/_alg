import numpy as np
import random

x = np.array([26, 25, 20, 23, 28, 28, 29, 30, 28, 35, 36, 33, 29, 27, 30, 33, 22, 20, 19, 22, 23, 29, 30, 33, 28, 33, 31, 38, 26, 22])
y = np.array([3000, 2000, 2150, 1500, 5500, 6000, 5123, 6010, 6648, 7001, 7214, 7101, 6812, 5651, 6468, 7510, 4031, 3984, 1594, 4010, 3151, 5413, 6641, 6847, 7000, 6413, 7300, 7701, 3101, 3100])

def compute_mse(b0, b1, x, y):
    return np.mean((y - (b0 + b1 * x)) ** 2)

def hill_climbing(x, y, iterations=100000):
    b0, b1 = 0.0, 0.0
    current_mse = compute_mse(b0, b1, x, y)
    step = 0.5 # 每次移動的步長
    
    for _ in range(iterations):
        # 產生一點點位移
        next_b0 = b0 + random.uniform(-step, step)
        next_b1 = b1 + random.uniform(-step, step)
        next_mse = compute_mse(next_b0, next_b1, x, y)
        
        if next_mse < current_mse:
            b0, b1, current_mse = next_b0, next_b1, next_mse
    return b0, b1

b0, b1 = hill_climbing(x, y)
print(f"【爬山演算法】截距: {b0:.4f}, 斜率: {b1:.4f}")
