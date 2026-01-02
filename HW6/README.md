參考[學習筆記-線性迴歸(Linear Regression)](https://medium.com/@jason8410271027/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8-linear-regression-38b17484ee0a)的資料  
我的理解:  
1.爬山演算法:使用的是一種「隨機摸索」的策略，它不計算導數，而是單純嘗試在當前位置附近隨機找一點，只要比現在好就往那邊跳。  
2.貪婪法:採取盡可能地嘗試當前最優路徑，配合文章中提到的概念，尋找使誤差最小化的參數組合，在每一輪中，它會從定義好的四個移動方向中挑選當下最好的一個方向，直到所有方向都無法再降低誤差為止。  
3.改良法:在初期「高溫」時接受較差的解，增加跳出局部陷阱並找到全域最佳解的機會。  
4.梯度下降法:根據文章提到的最小平方差原理，梯度下降法透過計算誤差的「方向」來更新參數，所以我用了微積分中的連鎖律，讓參數 $b_0, b_1$ 朝著總誤差最小的方向「走」去。  
最後實作下來都很接近文章中線性回歸的解 = -4225.161153 + (338.192386 * Data)


---  

執行結果   
1.爬山演算法
```
PS C:\Users\宏傑\OneDrive\桌面\alg>  c:; cd 'c:\Users\宏傑\OneDrive\桌面\alg'; & 'c:\Users\宏傑\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\宏傑\.vscode\extensions\ms-python.debugpy-2025.18.0-win32-x64\bundled\libs\debugpy\launcher' '58613' '--' 'C:\Users\宏傑\OneDrive\桌面\alg\HillClimbing.py'
【爬山演算法】截距: -4224.1060, 斜率: 338.1539
```
2.貪婪法  
```
PS C:\Users\宏傑\OneDrive\桌面\alg>  c:; cd 'c:\Users\宏傑\OneDrive\桌面\alg'; & 'c:\Users\宏傑\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\宏傑\.vscode\extensions\ms-python.debugpy-2025.18.0-win32-x64\bundled\libs\debugpy\launcher' '65065' '--' 'C:\Users\宏傑\OneDrive\桌面\alg\Greedy.py'
【貪婪法執行結果】
截距 (b0): -4224.7320
斜率 (b1): 338.1770

```
3.改良法
```
PS C:\Users\宏傑\OneDrive\桌面\alg>  c:; cd 'c:\Users\宏傑\OneDrive\桌面\alg'; & 'c:\Users\宏傑\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\宏傑\.vscode\extensions\ms-python.debugpy-2025.18.0-win32-x64\bundled\libs\debugpy\launcher' '54338' '--' 'C:\Users\宏傑\OneDrive\桌面\alg\SimulatedAnnealing.py' 
【改良法(模擬退火)】截距: -4225.0030, 斜率: 338.1858
```
4.梯度下降法  
```
PS C:\Users\宏傑\OneDrive\桌面\alg>  c:; cd 'c:\Users\宏傑\OneDrive\桌面\alg'; & 'c:\Users\宏傑\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\宏傑\.vscode\extensions\ms-python.debugpy-2025.18.0-win32-x64\bundled\libs\debugpy\launcher' '63198' '--' 'C:\Users\宏傑\OneDrive\桌面\alg\GradientDescent.py'
【梯度下降法】截距: -4214.6781, 斜率: 337.8275
```

