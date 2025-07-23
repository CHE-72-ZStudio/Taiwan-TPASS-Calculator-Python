# 「中華民國（臺灣）TPASS 通勤月票計算程式」的開發手冊
## Developer Manual for Taiwan TPASS Calculator (Python)

## 0. 目錄

1. [環境需求](#1-環境需求-environment-requirements)
2. [安裝配置](#2-安裝配置-installation--configuration)
3. [基本使用](#3-基本使用-basic-usage)
4. [專案結構](#4-專案結構-project-structure)

---

## 1. 環境需求 Environment Requirements
- **作業系統**：
    - Microsoft Windows 10+
    - Apple macOS 10.9+
    - Linux
- **依賴套件**：
    - Python 3.10+（支援 match...case... 語法）  
    - 支援 ANSI 轉義碼與中文字體顯示的終端輸出程式（ANSI 轉義碼用於 8 位元顏色顯示）  
    - 本專案的 Python 模組需求已在 `Requirements.txt` 文件中列出。您可以使用 pip 安裝所有模組依賴： `pip install -r Requirements.txt`  

## 2. 安裝配置 Installation & Configuration
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/releases) 頁面下載本程式檔案的壓縮檔 `Source Code`，解壓縮後放置於適當的位置
2. 確認解壓縮後的 `Main.py` 與程式運行時的其他必備檔案放置於同一文件夾路徑下  
3. 請確認您的電腦中已安裝 Python (>=3.10)，若是尚未安裝，可至 [Download Python](https://www.python.org/downloads/) 網頁下載安裝適合您作業系統的 Python 版本  
    > （若您已安裝完成合乎此程式要求的 Python 版本，可忽略這步驟）
4. 在該文件夾路徑中的終端窗口中輸入 `python Main.py` 以執行 `Main.py`  
5. 程式在輸出必要資訊後會進入「功能選擇平臺」，依據您所想要使用的功能輸入功能對應的半形數字後按下 `Enter/Return` 按鍵  

## 3. 基本使用 Basic Usage
請參照 [USER.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/USER.md) 文件中的第 3 章

## 4. 專案結構 Project Structure
- `Main.py`：本程式的唯一入口，處理「功能選擇平臺」邏輯與程式初始化
- `Func.py`：本程式的分析運行核心，處理輸入分析的相關功能，如分析計算、使用者輸入驗證、檔案寫入等
- `Studio.py`：存放簡短開源資訊與工作室 ASCII 藝術宣告

### 中華民國（臺灣）TPASS 通勤月票計算程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Taiwan TPASS Calculator (Python), Copytight (C) 2025-present CHE_72 ZStudio.  