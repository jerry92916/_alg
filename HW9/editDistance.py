import json

def editDistance(b, a):
    alen, blen = len(a), len(b)
    if alen == 0: return {'d': blen, 'm': []}
    if blen == 0: return {'d': alen, 'm': []}

    # 初始化矩陣，大小為 (blen+1) x (alen+1)
    m = [[0] * (alen + 1) for _ in range(blen + 1)]

    # 填入初始值（第一列與第一行）
    for i in range(blen + 1):
        m[i][0] = i
    for j in range(alen + 1):
        m[0][j] = j

    # 動態規劃填表
    for i in range(1, blen + 1):
        for j in range(1, alen + 1):
            if b[i-1] == a[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(
                    m[i-1][j-1] + 1, # 取代 (Substitution)
                    m[i][j-1] + 1,   # 插入 (Insertion)
                    m[i-1][j] + 1    # 刪除 (Deletion)
                )
    return {'d': m[blen][alen], 'm': m}

def align(b, a, m):
    i, j = len(b), len(a)
    ax, bx = '', ''
    
    # 從矩陣右下角往回溯到左上角
    while i > 0 and j > 0:
        # 情況 1: 來自上方 (b 刪除字元 或 a 插入空白)
        if m[i][j] == m[i-1][j] + 1:
            i -= 1
            bx = b[i] + bx
            ax = '-' + ax  # 使用 '-' 表示空格更清晰
        # 情況 2: 來自左方 (a 插入字元 或 b 插入空白)
        elif m[i][j] == m[i][j-1] + 1:
            j -= 1
            bx = '-' + bx
            ax = a[j] + ax
        # 情況 3: 來自左上方 (字元相同或取代)
        else:
            i -= 1
            j -= 1
            bx = b[i] + bx
            ax = a[j] + ax

    # 處理剩餘的邊界
    while i > 0:
        i -= 1
        bx = b[i] + bx
        ax = '-' + ax
    while j > 0:
        j -= 1
        bx = '-' + bx
        ax = a[j] + ax
    
    print(f'Align Result:')
    print(f'b: {bx}')
    print(f'a: {ax}')

def dump(m):
    """漂亮地印出矩陣"""
    for row in m:
        # 使用 json.dumps 讓陣列排版整齊
        print(json.dumps(row))

# --- 測試程式 ---
if __name__ == "__main__":
    # 測試資料
    str_b = "ATG ATCCG"
    str_a = "ATGCAATCCC"

    # 1. 計算編輯距離
    result = editDistance(str_b, str_a)
    
    print(f'字串 B: "{str_b}"')
    print(f'字串 A: "{str_a}"')
    print(f'最小編輯距離 (Edit Distance): {result["d"]}')
    
    print('\n==== 距離矩陣 m ====')
    dump(result['m'])
    
    print('\n==== 字串對齊 ====')
    align(str_b, str_a, result['m'])
