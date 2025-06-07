# 中華民國（臺灣）TPASS 通勤月票計算程式（Python）
## Taiwan TPASS Calculator (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)
    [![GitHub Release](https://img.shields.io/github/v/release/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/releases)
    [![GitHub License](https://img.shields.io/github/license/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/LICENSE)
    [![GitHub Last Commit](https://img.shields.io/github/last-commit/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/commits)
    [![Python 3](https://img.shields.io/badge/Python%203-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
    [![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?logo=PyCharm&logoColor=white)](https://www.jetbrains.com/pycharm/)

## 程式介紹 (Descriptions)
「中華民國（臺灣）TPASS 通勤月票計算程式」是一款 CLI 程式，可以根據您不同的乘車地區與數據，自動分析並計算總搭車金額，並與「TPASS 通勤月票」的售價做對比，協助您判斷是否購買當地的「TPASS 通勤月票」，進而節省在通勤上的花費。  
本分析程式支援分析各縣市不同種類月票的功能，讓您的月票選擇一站式搞定，節省下大量的時間並快速獲得計算後的建議結果。  

## 程式功能 (Features)
* 🇹🇼 **涵蓋各種縣市月票**：涵蓋各縣市目前已有的「TPASS 行政院通勤月票」，讓您可以快速進行不同種類月票的計算，找出當下最適合自己的月票方案！  
* 🚈 **涵蓋各式交通工具**：涵蓋各種月票可以使用的交通工具類別，您只須按照提示輸入對應內容即可獲得計算結果。
* 💾 **儲存計算結果**：程式會自動將每次的月票種類、輸入內容、計算結果與計算時間儲存至 `TPASS_Result.txt` 檔案中，您可以在日後直接該開啟檔案回顧之前的紀錄，不用再重新輸入一次！
* ⌨️ **易用的命令行介面**：透過不同的顏色顯示、完整的說明指引與簡易的數字選單，幫助您快速完成分析帳目的工作，節省大量時間。  

## 環境需求 (Requirements)
+ Python 3 
+ 支援 ANSI 轉義碼與中文字體顯示的終端輸出程式（ANSI 轉義碼用於 8 位元顏色顯示）  

- Microsoft Windows  
    * 對於一般使用者，建議使用 Windows 10+ 搭配 Windows Terminal ，容易上手使用  
    * 對於專業開發者，本程式可以搭配自身習慣且支援 8 位元顏色顯示的終端使用  
    > 目前僅建議專業開發者直接編譯運行本程式，我們預計會在未來發行可供一般使用者執行的可執行二進制檔，詳情可見「未來功能」區塊  
- Apple macOS / Linux  
    * 本程式尚未進行關於 macOS / Linux 的相容性測試  
    * 您可以先為此程式的相容性進行測試，若使用中遇到任何問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  
    > 我們預計會在未來增加對這些系統的兼容，並發行可執行二進制檔，詳情可見「未來功能」區塊  

## 使用說明 (Instructions)
1. A
2. B
3. C
4. D
5. E
6. F
7. G
> 更為詳細的使用說明可以參考 [MANUAL.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/MANUAL.md) 文件  

## V0.y.zz 更新日誌 (Changes in V0.y.zz)
* 首次測試版本釋出 First Pre-Release
    - 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色
    - 具備基本的接收使用者輸入、計算與輸出結果功能
    - 僅支援部分縣市的月票方案，尚未開發完成
> 所有更新紀錄可參閱 [CHANGELOG.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/CHANGELOG.md) 文件

## VX.y.zz 已知問題 (Known Issues in VX.y.zz)

> 如果您有發現任何其他這裡未列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本        | 增加功能     | 開發狀態             | 優先順序     | 預定發布          |
|-------------|----------|------------------|----------|---------------|
| ***1.0.0*** | 首次正式版本發佈 | 正在設計 (Designing) | 高 (High) | ***2025-??*** |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**主要**貢獻者／項目**主要**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/LICENSE) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 中華民國（臺灣）TPASS 通勤月票計算程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Taiwan TPASS Calculator (Python), Copytight (C) 2025-present CHE_72 ZStudio.  
