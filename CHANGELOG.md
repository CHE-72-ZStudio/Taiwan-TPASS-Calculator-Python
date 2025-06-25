# 「中華民國（臺灣）TPASS 通勤月票計算程式」的變更日誌
## Change Log for Taiwan TPASS Calculator (Python)

## UNRELEASED ~~V0.1.11 (2025-MM-DD)~~ Title
### 新增功能 Added
- 開放 北宜跨城際及雙北 \$2,300、澎湖縣公車 \$150、澎湖縣車船 \$400 月票方案的計算
- 大量新增與程式運行流程相關的提示訊息，方便您得知程式目前的運作情形
### 功能修復 Fixed
- 修復在輸入票價金額與搭乘次數時，可能會因為出現錯誤導致無法正確儲存數據的問題
### 提升進步 Improved
- 優化在輸出檔案 `TPASS_Result.txt` 中，時間戳記的顯示效果，現在遇到空位會自動補 0
- 現在在輸出結果時，會同時顯示您當下選擇評估的月票方案，以便您比較不同種類月票的花費金額
- 優化程式輸出的文字內容與顯示顏色

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
#### Taiwan TPASS Calculator (Python), Copytight (C) 2025-present CHE_72 ZStudio.  