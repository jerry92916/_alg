[對話紀錄-Python 最小編輯距離與對齊程式](https://gemini.google.com/share/9a5b92b9a653)
---
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
