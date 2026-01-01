import numpy as np

x = np.array([26, 25, 20, 23, 28, 28, 29, 30, 28, 35, 36, 33, 29, 27, 30, 33, 22, 20, 19, 22, 23, 29, 30, 33, 28, 33, 31, 38, 26, 22])
y = np.array([3000, 2000, 2150, 1500, 5500, 6000, 5123, 6010, 6648, 7001, 7214, 7101, 6812, 5651, 6468, 7510, 4031, 3984, 1594, 4010, 3151, 5413, 6641, 6847, 7000, 6413, 7300, 7701, 3101, 3100])

def greedy_search(x, y, iterations=10000):
    b0, b1 = 0.0, 0.0
    step = 0.1
    
    for _ in range(iterations):
        curr_mse = np.mean((y - (b0 + b1 * x)) ** 2)
        # 測試四個方向（b0增減, b1增減），選擇能降低誤差的
        moved = False
        for db0, db1 in [(step, 0), (-step, 0), (0, step), (0, -step)]:
            if np.mean((y - ((b0+db0) + (b1+db1) * x)) ** 2) < curr_mse:
                b0 += db0
                b1 += db1
                moved = True
                break
        if not moved: step *= 0.5 # 如果都不能動了，縮小步長繼續找
    return b0, b1

b0, b1 = greedy_search(x, y)
print(f"【貪婪法】截距: {b0:.4f}, 斜率: {b1:.4f}")
