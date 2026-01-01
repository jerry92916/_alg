import numpy as np

# 數據準備
x = np.array([26, 25, 20, 23, 28, 28, 29, 30, 28, 35, 36, 33, 29, 27, 30, 33, 22, 20, 19, 22, 23, 29, 30, 33, 28, 33, 31, 38, 26, 22])
y = np.array([3000, 2000, 2150, 1500, 5500, 6000, 5123, 6010, 6648, 7001, 7214, 7101, 6812, 5651, 6468, 7510, 4031, 3984, 1594, 4010, 3151, 5413, 6641, 6847, 7000, 6413, 7300, 7701, 3101, 3100])

def compute_mse(b0, b1, x, y):
    return np.mean((y - (b0 + b1 * x)) ** 2)

def greedy_linear_regression(x, y):
    # 初始化參數
    b0, b1 = 0.0, 0.0
    current_mse = compute_mse(b0, b1, x, y)
    
    # 定義貪婪搜尋的步進值
    learning_steps = [100, 10, 1, 0.1, 0.01, 0.001]
    
    for step in learning_steps:
        while True:
            # 貪婪地尋找四個方向中最好的那一個
            directions = [
                (b0 + step, b1), # 增加 b0
                (b0 - step, b1), # 減少 b0
                (b0, b1 + step), # 增加 b1
                (b0, b1 - step)  # 減少 b1
            ]
            
            best_move = None
            min_mse = current_mse
            
            for next_b0, next_b1 in directions:
                mse = compute_mse(next_b0, next_b1, x, y)
                if mse < min_mse:
                    min_mse = mse
                    best_move = (next_b0, next_b1)
            
            # 如果找到了更好的移動方向，就更新參數並繼續在此步長下搜尋
            if best_move:
                b0, b1 = best_move
                current_mse = min_mse
            else:
                # 如果四個方向都沒有更好，則縮小步長進入下一輪搜尋
                break
                
    return b0, b1

# 執行
b0, b1 = greedy_linear_regression(x, y)
print(f"【貪婪法執行結果】")
print(f"截距 (b0): {b0:.4f}")
print(f"斜率 (b1): {b1:.4f}")
