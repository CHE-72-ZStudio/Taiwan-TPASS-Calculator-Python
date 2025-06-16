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
    - Apple macOS
    - Linux
- **依賴套件**：
    - Python 3.10+（支援 match...case... 語法）  
    - 支援 ANSI 轉義碼與中文字體顯示的終端輸出程式（ANSI 轉義碼用於 8 位元顏色顯示）  
    - 本專案的 Python 模組需求已在 `Requirements.txt` 文件中列出。您可以使用 pip 安裝所有模組依賴： `pip install -r Requirements.txt`  

## 2. 安裝配置 Installation & Configuration

## 3. 基本使用 Basic Usage
請參照 [USER.md](https://github.com/CHE-72-ZStudio/Taiwan-TPASS-Calculator-Python/blob/main/USER.md) 文件中的第 3 章

## 4. 專案結構 Project Structure
- `Main.py`：本程式的唯一入口，處理「功能選擇平臺」邏輯與程式初始化
- `Func.py`：本程式的分析運行核心，處理輸入分析的相關功能，如分析計算、使用者輸入驗證、檔案寫入等
- `Studio.py`：存放簡短開源資訊與工作室 ASCII 藝術宣告

### 中華民國（臺灣）TPASS 通勤月票計算程式（Python），著作權所有 (C) 2025-現在 CHE_72 ZStudio  
#### Taiwan TPASS Calculator (Python), Copytight (C) 2025-present CHE_72 ZStudio.  