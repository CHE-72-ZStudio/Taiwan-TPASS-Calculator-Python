"""
Main.py
此模組為「中華民國（臺灣）TPASS 通勤月票計算程式」的唯一入口
"""

import sys
import time

from Studio import *

if __name__ == "__main__":
    # 定義 中／英 程式名稱、程式版本號，如果日後有需要更新時，更改此處即可避免缺失遺漏
    program_zh = "中華民國（臺灣）TPASS 通勤月票計算程式（Python）"
    program_en = "Taiwan TPASS Calculator (Python)"
    version = "0.UNKNOWN.UNKNOWN"

    print("歡迎您使用「{}」Ver{}，本程式由 CHE_72 ZStudio 製作".format(program_zh, version))  # 輸出中文程式名稱、程式版本號、工作室名稱
    print("\033[38;5;208m本程式可用來協助您分析購買「TPASS 通勤月票」是否划算，並使用將結果儲存在 \"TPASS_Result.txt\" 中。\033[0m")  # 輸出中文程式目的
    print("\033[38;5;208m以下所有問題請依照提示輸入「半形阿拉伯數字」回答\033[0m\n")  # 輸出中文使用提示，避免使用者誤用全形數字或中文數字
    print("\033[38;5;197m本程式目前正在開發中，敬請期待\033[0m\a\n")  # 輸出中文使用提示，避免使用者誤用全形數字或中文數字
    print("「{}」Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))
    print("{} Ver{} , Copyright (C) 2025-present CHE_72 ZStudio".format(program_en, version))
    print(Studio_ZH)  # Studio.py 中的中文版工作室宣告
    with open("TPASS_Result.txt", "a+", encoding="UTF-8") as result:
        pass
    sys.exit(0)  # 呼叫系統正常結束本程式運行
else:  # 如果使用者誤將本程式作為模組引用
    print("\033[38;5;197m本程式為「中華民國（臺灣）TPASS 通勤月票計算程式」的主入口\n請直接運行 Main.py，而非透過其他模組引入本程式\033[0m\a\n")  # 輸出提示訊息提醒使用者正確使用方式
    sys.exit(0)  # 呼叫系統正常結束本程式運行