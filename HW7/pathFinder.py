import copy

def matrix_print(m):
    for row in m:
        print("".join(row))

def find_path(m, x, y):
    #取得迷宮邊界
    rows = len(m)
    cols = len(m[0])
    
    print(f"=========================\nx={x} y={y}")
    matrix_print(m)

    #1.邊界檢查跟障礙物判斷
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    if m[x][y] == '*' or m[x][y] == '+':
        return False
    
    #2.標記目前路徑為 '.'
    #如果是空白，表示還沒走過，標記為嘗試中
    m[x][y] = '.'
    
    #3.終點判斷(抵達邊界即為找到出口)
    if x == rows - 1 or y == cols - 1:
        return True

    #4.遞迴探索四個方向 (右、下、左、上)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        #檢查下一步是否在範圍內且為空白路徑 ' '
        if 0 <= nx < rows and 0 <= ny < cols and m[nx][ny] == ' ':
            if find_path(m, nx, ny):
                return True

    #5.回溯 (Backtracking)
    # 如果四個方向都走不通，將這個點標記為死路 '+'
    m[x][y] = '+'
    return False

#初始化迷宮
maze_str = [
    "********",
    "** * ***",
    "      ***",
    "* ******",
    "* **",
    "***** **"
]
maze = [list(row) for row in maze_str]

#執行搜尋
if find_path(maze, 2, 0):
    print("\n找到出口了！最終路徑如下：")
else:
    print("\n無解！")

print("=========================")
matrix_print(maze)
