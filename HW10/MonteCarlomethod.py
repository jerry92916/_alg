import random

def monte_carlo_n_dim(f, bounds, N=100000):
    """
    使用蒙地卡羅法計算 n 維積分
    
    參數:
    f: 待積分函數
    bounds: 積分範圍 [(x1_min, x1_max), (x2_min, x2_max), ...]
    N: 隨機取樣點數 (N 越大越精準)
    """
    dims = len(bounds)
    
    # 1. 計算超長方體的總體積 V
    total_volume = 1.0
    for low, high in bounds:
        total_volume *= (high - low)
    
    # 2. 在範圍內隨機取樣並累加函數值
    total_f_sum = 0
    for _ in range(N):
        # 為每個維度產生一個隨機座標
        point = [random.uniform(low, high) for low, high in bounds]
        total_f_sum += f(point)
    
    # 3. 積分值 = 體積 * 平均函數值
    average_f = total_f_sum / N
    return total_volume * average_f

# --- 測試範例 ---
if __name__ == "__main__":
    # 測試一個高維球體的體積（例如單位超球體的 1/2^n 部分）
    # 函數：如果點在單位圓/球內 return 1，否則 0
    def in_unit_sphere(p):
        return 1 if sum(x**2 for x in p) <= 1 else 0

    # 計算 4 維單位超球體在第一象限的「體積」
    # 範圍均為 [0, 1]，維度 n=4
    n_dim = 4
    bounds_4d = [(0, 1)] * n_dim
    
    # 理論值：(1/2^n) * (pi^(n/2) / Gamma(n/2 + 1))
    # 對於 4 維球體，總體積是 (pi^2)/2 ≈ 4.9348，第一象限是其 1/16 ≈ 0.3084
    result = monte_carlo_n_dim(in_unit_sphere, bounds_4d, N=500000)
    
    print(f"{n_dim}維超球體(局部)積分結果: {result:.6f}")
    print(f"與理論值比較: 0.308425")
