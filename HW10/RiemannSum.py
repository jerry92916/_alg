import itertools

def n_dimensional_riemann_sum(f, bounds, steps):
    """
    計算 n 維函數的黎曼積分
    
    參數:
    f: 待積分的函數，接受一個長度為 n 的 list 或 tuple
    bounds: 積分範圍，格式為 [(x1_min, x1_max), (x2_min, x2_max), ...]
    steps: 每個維度的切割份數，格式為 [n1, n2, ...]
    """
    n = len(bounds)
    dx = []
    grid_axes = []

    # 1. 計算每個維度的步長 (dx) 並建立座標點
    for i in range(n):
        low, high = bounds[i]
        d = (high - low) / steps[i]
        dx.append(d)
        # 產生該維度的取樣點 (左點法)
        grid_axes.append([low + j * d for j in range(steps[i])])

    # 2. 計算超體積單位 dV = dx1 * dx2 * ... * dxn
    dv = 1
    for d in dx:
        dv *= d

    # 3. 使用 itertools.product 產生所有維度的笛卡爾積（所有小格子的座標）
    total_sum = 0
    for point in itertools.product(*grid_axes):
        total_sum += f(point)

    return total_sum * dv

# --- 測試範例 ---
if __name__ == "__main__":
    # 範例 1: 二維積分 f(x, y) = x * y, x 從 0 到 1, y 從 0 到 1
    # 理論值應為 0.25
    func_2d = lambda p: p[0] * p[1]
    bounds_2d = [(0, 1), (0, 1)]
    steps_2d = [100, 100]
    result_2d = n_dimensional_riemann_sum(func_2d, bounds_2d, steps_2d)
    print(f"2D 積分結果: {result_2d:.6f}")

    # 範例 2: 三維積分 f(x, y, z) = x + y + z, 範圍皆為 0 到 1
    # 理論值應為 1.5
    func_3d = lambda p: sum(p)
    bounds_3d = [(0, 1), (0, 1), (0, 1)]
    steps_3d = [50, 50, 50]
    result_3d = n_dimensional_riemann_sum(func_3d, bounds_3d, steps_3d)
    print(f"3D 積分結果: {result_3d:.6f}")
