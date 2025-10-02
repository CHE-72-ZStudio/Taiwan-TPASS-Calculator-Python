# 中華民國（臺灣）TPASS 通勤月票計算程式（Python）
## Taiwan TPASS Calculator (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)
    [![GitHub Release](https://img.shields.io/github/v/release/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/releases)
    [![GitHub License](https://img.shields.io/github/license/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/LICENSE)
    [![GitHub Last Commit](https://img.shields.io/github/last-commit/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python)](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/commits)
    [![Python 3.10+](https://img.shields.io/badge/Python%203.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
    [![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?logo=PyCharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
> 「Ask DeepWiki」功能為由 Devin AI 生成的 Wiki 文檔，每週自動刷新一次，內容可能與最新版程式有所差異  
> 該 AI 生成的 Wiki 文檔與回覆內容僅供參考，我們對其不負任何擔保責任，實際情形請依本儲存庫最新提交為準  

## 程式介紹 (Descriptions)
「中華民國（臺灣）TPASS 通勤月票計算程式」是一款 CLI 程式，可以根據您不同的通勤生活圈與數據，自動分析並計算總搭車金額，並與當地的「TPASS 通勤月票」的售價做對比，協助您判斷是否購買月票方案，進而節省在通勤上的花費。  
本分析程式支援分析各縣市不同種類 TPASS 與 高雄MeNGo 月票的功能，讓您的月票選擇一站式搞定，節省下大量的時間並快速獲得計算後的建議結果。  

## 程式功能 (Features)
* 🇹🇼 **涵蓋各種縣市月票**：涵蓋各縣市目前已有的「TPASS 行政院通勤月票」，讓您可以快速進行不同種類月票的計算，找出當下最適合自己的月票方案！  
* 🚈 **涵蓋各式交通工具**：涵蓋各種月票可以使用的交通工具類別，您只須按照提示輸入對應內容即可獲得計算結果。
* 💾 **儲存計算結果**：程式會自動將每次的月票種類、輸入內容、計算結果與計算時間儲存至 `TPASS_Result.txt` 檔案中，您可以在日後直接該開啟檔案回顧之前的紀錄，不用再重新輸入一次！
* ⌨️ **易用的命令行介面**：透過不同的顏色顯示、完整的說明指引與簡易的數字選單，幫助您快速完成分析帳目的工作，節省大量時間。  

## 環境需求 (Requirements)
- Microsoft Windows  
    * Windows 10+ 64位元（2004 以上版本）搭配 [Windows 終端機 (Windows Terminal)](https://aka.ms/terminal)
        * Windows 11+ 已預裝 Windows 終端機，無須另外安裝  
- Apple macOS 10.9+  
- Linux （建議搭配 [KDE 的 Konsole](https://konsole.kde.org/download.html)）
> 一般的 Windows 使用者可以直接從 [Releases](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/releases) 頁面直接下載 `TTCP-Win-X.Y.ZZ.zip`  
> 目前僅建議專業開發者直接在 Apple macOS / Linux 編譯運行本程式，我們預計會在未來發行可供一般使用者執行的可執行二進制檔，詳情可見「未來功能」區塊

## 使用說明 (Instructions)
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/releases) 頁面下載對應系統的壓縮包 `TTCP-OS-X.Y.ZZ.zip`，解壓縮後放置於適當的位置  
2. 雙擊打開本程式的可執行二進制檔案 `TTCP-X.Y.ZZ-OS`，即可開始使用本程式  
3. 進入「功能選擇平臺」，依據您所想要使用的功能輸入對應的半形數字後按下 `Enter/Return` 按鍵  
4. 進入「都會選擇平臺」，依據您所想要分析的生活圈輸入對應的半形數字後按下 `Enter/Return` 按鍵  
    - （如果有的話）進入「方案選擇平臺」，您可以在該通勤生活圈依據想要分析的月票方案輸入對應的半形數字後按下 `Enter/Return` 按鍵  
5. 進入「交通選擇平臺」，依據您所想要搭乘的大眾運輸交通工具輸入對應的半形數字後按下 `Enter/Return` 按鍵  
6. 進入「數據輸入平臺」，使用半形數字輸入該交通工具搭乘的票價與次數後按下 `Enter/Return` 按鍵
    - 其他大眾運輸：程式會詢問您想要輸入的票價金額與對應的搭乘次數
        * 如果您已完成此項交通工具的輸入，想要輸入其他工具的數據，可以輸入 `0` 後按下 `Enter/Return` 按鍵，這時會返回「交通選擇平臺」，讓您可以選擇同一月票方案下的其他運輸工具  
    - 臺北捷運+環狀線：程式會依序詢問您不同的捷運票價對應的搭乘次數，您只需要依照提示使用半形數字輸入後按下 `Enter/Return` 按鍵即可
        * 因為臺北捷運的常客優惠，如果遇上 公車⇄︎捷運 的轉乘優惠情形，請將捷運的票價視為原價以便進行次數的輸入  
        * 按照程式循序回答完所有捷運票價對應的搭乘次數後，會返回「交通選擇平臺」，讓您可以選擇同一月票方案下的其他運輸工具  
    - 大臺北地區 市區公車：會依據您所選擇的身分，詢問您不同的公車票價對應的搭乘次數
        * 如果有 2 段票或是 3 段票的情形，請視為 2 次或是 3 次一段票的方式輸入
        * 如果遇上 公車⇄︎捷運 的轉乘優惠情形，請將轉乘的優惠票價算在公車次數中
        * 按照程式循序回答完所有公車票價對應的搭乘次數後，會返回「交通選擇平臺」，讓您可以選擇同一月票方案下的其他運輸工具
7. 如果您已完成該月票方案對應乘車數據的輸入，想要查看最終的計算結果，請在「交通選擇平臺」中輸入 `0` 後按下 `Enter/Return` 按鍵
8. 這時候程式會在螢幕上顯示出您的乘車總次數與總金額、通勤花費總金額與是否推薦購買「TPASS 通勤月票」的參考建議，您可以根據自身情形做決定
    - 程式同時會將當下的時間與最終的計算結果儲存在與主程式同資料夾下的 `TPASS_Result.txt` 中，方便您日後可以隨時查詢使用紀錄
9. 這時程式會出現綠色提示後回到「都會選擇平臺」，您可以繼續進行不同生活圈、不同月票方案、不同乘車數據的分析；也可以選擇返回「功能選擇平臺」切換程式的其他功能，或是分析完成後可以直接依照指示輸入對應的半形數字後按下 `Enter/Return` 按鍵以結束程式  
> 若您輸入的內容有誤，本程式將會自動提醒您，並提示即將返回的介面，以供您做好準備  
> 詳細的 用戶手冊可以參考 [USER.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/USER.md) 文件；開發手冊可以參考 [DEVELOPER.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/DEVELOPER.md) 文件  

## V1.0.10 更新日誌 (Changes in V1.0.10)
* 新增功能 Added
  - 開放 北宜跨城際及雙北 \$2,300、澎湖縣公車 \$150、澎湖縣車船 \$400 月票方案的計算
  - 新上架了一批驚喜的小彩蛋，等待您來尋寶
  - 現在會在總花費金額為 0 時出現額外的專屬提示內容，增加可讀性
* 功能修復 Fixed
  - 修復在輸入票價金額與搭乘次數時，可能會因為出現錯誤導致無法正確儲存數據的問題
* 提升進步 Improved
  - 優化在輸出檔案 `TPASS_Result.txt` 中，時間戳記的顯示效果，現在遇到空位會自動補 0
  - 大量新增與程式運行流程相關的提示訊息，方便您得知程式目前的運作情形
  - 現在在螢幕介面上顯示結果時，會同時顯示您當下選擇評估的月票方案，以便您比較不同種類月票的花費金額
  - 更新並優化程式輸出的文字內容與顯示顏色，使其更為清晰與精準
  - 優化在「臺北捷運+環狀線」的常客優惠票價顯示，現在會改為顯示進行四捨五入後的整數值
  - 現在會在輸出結果中包含 都會生活圈／縣市 的名稱，方便進行查找與判讀
* 文檔更新 Edited
  - 完善 `README.md`、`USER.md` 與 `DEVELOPER.md` 檔案中的描述
> 所有更新紀錄可參閱 [CHANGELOG.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/CHANGELOG.md) 文件

## V1.0.10 已知問題 (Known Issues in V1.0.10)
| 問題編號 (Issues Num) | 錯誤標題 (Issues Title) | 影響程度 (Priority) | 修復狀態 (Status) | 替代方案(Workaround)                | 詳細內容 (Datails)                                                       | 
|-------------------|---------------------|-----------------|---------------|---------------------------------|----------------------------------------------------------------------|
| None              | 缺少計算臺灣鐵路常客優惠方案的計算功能 | 部分 (Major)      | 等待處理 (Open)   | 自行根據加總後的票價，手動計算與判斷套用常客優惠後的總金額結果 | 由於沒有計算臺灣鐵路的電子票證常客優惠方案，導致計算結果會比實際花費高，程式進而會給出不適當的建議                    |
| None              | 高雄市公車暢遊月票方案計算錯誤     | 邊緣 (Minor)      | 即將發布 (Fixed)  | 自行根據加總後的票價，手動計算與判斷是否購買該月票       | 高雄市公車暢遊 MeNGo（非 TPASS）方案正確金額為 \$199，但在計算過程中誤植為 \$399，導致程式最終會給出不適當的建議 |
> 如果您有發現任何其他未在這裡列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本         | 增加功能                                                | 開發狀態              | 優先順序       | 預定發布          |
|--------------|-----------------------------------------------------|-------------------|------------|---------------|
| ***1.0.14*** | 在臺灣鐵路交通工具的輸入中，增加使用電子票證乘車的常客優惠方案計算功能                 | 功能規劃 (Planning)   | 中 (Medium) | ***2026-02*** |
| ***1.0.14*** | 更新與修正 `README.md`、`USER.md` 與 `DEVELOPER.md` 檔案中的描述 | 功能規劃 (Planning)   | 低 (Low)    | ***2026-02*** |
| ***1.0.14*** | 修復高雄市公車暢遊月票方案計算錯誤的問題                                | 準備發布 (Completed)  | 低 (Low)    | ***2026-02*** |
| ***1.0.14*** | 增加對使用者輸入票價進行邊界檢查的功能，確保輸入票價的合理性                      | 功能規劃 (Planning)   | 低 (Low)    | ***2026-02*** |
| 1.1.0        | 增加可以寫入 `TTCP_Diagnose.log` 診斷日誌檔案的功能                | 功能規劃 (Planning)   | 中 (Medium) | 2026-??       |
| 1.1.1        | 增加更多例外情形處理                                          | 正在討論 (Discussing) | 低 (Low)    | 2026-??       |
| 1.1.2        | 提升跨系統顯示相容性，並開始發行 macOS/Linux 可執行檔                   | 功能規劃 (Planning)   | 低 (Low)    | 2026-??       |
| 1.2.0        | 調整優化程式邏輯與簡化選單操作介面，降低運行時間並提升易用性，為即將新增的 GUI 功能做準備     | 功能規劃 (Planning)   | 中 (Medium) | 2026-??       |
| ***2.0.0***  | 增加跨平臺通用 GUI                                         | 功能規劃 (Planning)   | 中 (Medium) | ***202?-??*** |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/LICENSE) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 中華民國（臺灣）TPASS 通勤月票計算程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Taiwan TPASS Calculator (Python), Copyright (C) 2025-present CHE_72 ZStudio.  
