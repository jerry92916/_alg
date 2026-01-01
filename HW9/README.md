# [陳宏傑的對話紀錄-Python 最小編輯距離與對齊程式](https://gemini.google.com/share/9a5b92b9a653)
---
本專案使用 Python 實作編輯距離（Edit Distance / Levenshtein Distance） 的動態規劃演算法，用來計算兩個字串之間轉換所需的最少操作次數，並進一步產生字串對齊（alignment）結果。

功能說明

Edit Distance 計算

支援三種基本操作：

插入（Insertion）

刪除（Deletion）

取代（Substitution）

使用動態規劃建立距離矩陣，時間複雜度為 O(n × m)

距離矩陣回溯（Alignment）

從矩陣右下角回溯到左上角

產生兩個字串的最佳對齊結果

使用 - 表示插入或刪除的位置

矩陣視覺化輸出

以 JSON 排版方式輸出距離矩陣，方便觀察動態規劃過程  

---
# 執行結果
```
PS C:\Users\宏傑\OneDrive\桌面\alg>  & 'c:\Users\宏傑\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\宏傑\.vscode\extensions\ms-python.debugpy-2025.18.0-win32-x64\bundled\libs\debugpy\launcher' '54385' '--' 'C:\Users\宏傑\OneDrive\桌面\alg\editDistance.py' 
字串 B: "ATG ATCCG"
字串 A: "ATGCAATCCC"
最小編輯距離 (Edit Distance): 3

==== 距離矩陣 m ====
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
[3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
[4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7]
[5, 4, 3, 2, 2, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 3, 2, 2, 2, 3, 4, 5]
[7, 6, 5, 4, 3, 3, 3, 3, 2, 3, 4]
[8, 7, 6, 5, 4, 4, 4, 4, 3, 2, 3]
[9, 8, 7, 6, 5, 5, 5, 5, 4, 3, 3]

==== 字串對齊 ====
Align Result:
b: ATG A-TCCG
a: ATGCAATCCC
```
