# 方法1：直接運算
def power2n_v1(n):
    return 2**n

# 方法2：用遞迴(加法)
def power2n_v2(n):
    if n == 0:
        return 1
    return power2n_v2(n-1) + power2n_v2(n-1)

# 方法3：用遞迴(乘法)
def power2n_v3(n):
    if n == 0:
        return 1
    return 2 * power2n_v3(n-1)

# 方法4：用遞迴+查表 
memo = {}
def power2n_v4(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = power2n_v4(n-1) + power2n_v4(n-1)
    return memo[n]

# 用n=10測試
n = 10
print(f"方法1   結果: {power2n_v1(n)}")
print(f"方法2   結果: {power2n_v2(n)}")
print(f"方法3   結果: {power2n_v3(n)}")
print(f"方法4   結果: {power2n_v4(n)}")
