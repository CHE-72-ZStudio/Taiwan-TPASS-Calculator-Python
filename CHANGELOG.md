# 「中華民國（臺灣）TPASS 通勤月票計算程式」的變更日誌
## Change Log for Taiwan TPASS Calculator (Python)

## UNRELEASED ~~V1.0.14 (20YY-MM-DD) 大幅提升程式的準確性與健壯性~~
### 新增功能 Added
- 在輸入使用電子票證搭乘臺灣鐵路時，增加對應常客優惠方案的計算功能（尚未完成）
- 增加對使用者輸入票價進行邊界檢查的功能，確保輸入票價的合理性（尚未完成）
### 功能修復 Fixed
- 修復在計算高雄市公車暢遊月票方案時，由於月票方案金額設定錯誤，導致程式最終會給出不適當建議的問題
### 文檔更新 Edited
- 更新與修正 `README.md`、`USER.md` 與 `DEVELOPER.md` 檔案中的描述
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者

## V1.0.10 (2025-08-16) 首次正式版本發佈
### 新增功能 Added
- 開放 北宜跨城際及雙北 \$2,300、澎湖縣公車 \$150、澎湖縣車船 \$400 月票方案的計算
- 新上架了一批驚喜的小彩蛋，等待您來尋寶
- 現在會在總花費金額為 0 時出現額外的專屬提示內容，增加可讀性
### 功能修復 Fixed
- 修復在輸入票價金額與搭乘次數時，可能會因為出現錯誤導致無法正確儲存數據的問題
### 提升進步 Improved
- 優化在輸出檔案 `TPASS_Result.txt` 中，時間戳記的顯示效果，現在遇到空位會自動補 0
- 大量新增與程式運行流程相關的提示訊息，方便您得知程式目前的運作情形
- 現在在螢幕介面上顯示結果時，會同時顯示您當下選擇評估的月票方案，以便您比較不同種類月票的花費金額
- 更新並優化程式輸出的文字內容與顯示顏色，使其更為清晰與精準
- 優化在「臺北捷運+環狀線」的常客優惠票價顯示，現在會改為顯示進行四捨五入後的整數值
- 現在會在輸出結果中包含 都會生活圈／縣市 的名稱，方便進行查找與判讀
### 文檔更新 Edited
- 完善 `README.md`、`USER.md` 與 `DEVELOPER.md` 檔案中的描述
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## V0.1.5 (2025-06-17) 首次測試版本釋出
### 首次測試版本釋出 First Pre-Release
- 使用 CLI 介面與 ANSI 轉義碼顯示 8 位元顏色
- 具備基本的接收使用者輸入、計算與輸出簡易計算結果功能
- 僅支援部分縣市的月票方案，尚未開發完成
- 更新 `README.md` 中的描述
- 新增 `USER.md` 與 `DEVELOPER.md` 以取代過時的 `MANUAL.md`
### 貢獻清單 Contributor
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

### 中華民國（臺灣）TPASS 通勤月票計算程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Taiwan TPASS Calculator (Python), Copyright (C) 2025-present CHE_72 ZStudio.  