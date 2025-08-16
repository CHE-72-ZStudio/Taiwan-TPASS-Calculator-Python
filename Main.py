"""
Main.py
此模組為「中華民國（臺灣）TPASS 通勤月票計算程式」的唯一入口
"""

import sys

import Func
from Studio import *

if __name__ == "__main__":
    # 定義 中／英 程式名稱、程式版本號，如果日後有需要更新時，更改此處即可避免缺失遺漏
    program_zh = "中華民國（臺灣）TPASS 通勤月票計算程式（Python）"
    program_en = "Taiwan TPASS Calculator (Python)"
    version = "1.0.10"

    print("歡迎您使用「{}」Ver{}，本程式由 CHE_72 ZStudio 製作".format(program_zh, version))  # 輸出中文程式名稱、程式版本號、工作室名稱
    print("\033[38;5;208m本程式可用來協助您分析購買「TPASS 通勤月票」是否划算，並將結果儲存在 \"TPASS_Result.txt\" 中。\033[0m")  # 輸出中文程式目的
    print("\033[38;5;208m以下所有問題請依照提示輸入「半形阿拉伯數字」回答\033[0m\n")  # 輸出中文使用提示，避免使用者誤用全形數字或中文數字

    func_manual = ("\033[38;5;208m\n「功能選擇平臺」使用說明\t0 顯示本則使用說明\t1 開始分析搭乘紀錄並計算結果\n"
                   "7 顯示英文原版的 GNU GPLv3 開源授權許可（具有法律效力）\t8 顯示中文翻譯的 GNU GPLv3 開源授權許可（僅供理解參考）\n"
                   "9 顯示工作室名稱與程式版權宣告\t10 結束運行並退出程式\n\033[0m")  # 「功能選擇平臺」使用說明

    while True:
        print("這裡是「功能選擇平臺」，請選擇您要使用的功能")
        print("\033[38;5;43m0：顯示使用說明、1：開始計算分析、7：顯示開源許可（英文原版）、8：顯示開源許可（中文翻譯）、9：顯示作者宣告、10：結束程式運行")
        func = -1  # 「功能選擇平臺」的功能變數

        try:  # 讀取使用者輸入至功能變數，並嘗試轉換成整數
            func = Func.check_input("--> \033[0m", 0, 10)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至方案變數，依序傳入 詢問內容、最小數值、最大數值
        except Func.RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「功能選擇平臺」
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 返回「功能選擇平臺」
        except Exception:  # 例外處理，捕捉其他未預期的錯誤
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「功能選擇平臺」
        else:
            match func:  # 根據功能變數判斷，切換不同功能
                case 0:  # 功能0：顯示使用說明
                    print(func_manual)  # 輸出「功能選擇平臺」簡易使用說明
                case 1:  # 功能1：開始計算分析
                    Func.analyze(program_zh, version)
                case 4:  # 功能4：隱藏的小彩蛋
                    print("\033[38;5;201m恭喜您找到隱藏的小彩蛋，祝福您事事順心、萬事如意\033[0m")
                case 6:  # 功能6：隱藏的小彩蛋
                    print("\033[38;5;201m恭喜您找到隱藏的小彩蛋，祝福您的生活六六大順\033[0m")
                case 7:  # 功能7：顯示開源許可（英文原版）
                    # 嘗試開啟 LICENSE 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("LICENSE", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"LICENSE\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 8:  # 功能8：顯示開源許可（中文翻譯）
                    # 嘗試開啟 LICENSE_ZH 檔案為 gpl 句柄，否則輸出錯誤訊息並取消印出開源許可
                    try:
                        with open("LICENSE_ZH", "r", encoding="UTF-8") as gpl:
                            for line in gpl:
                                print(line, end="")
                    except FileNotFoundError:
                        print("\033[38;5;197m開啟 \"LICENSE_ZH\" 時出現錯誤，請檢查資料夾內是否包含此檔案")
                case 9:  # 功能9：顯示作者宣告
                    print("「{}」Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))
                    print("{} Ver{} , Copyright (C) 2025-present CHE_72 ZStudio".format(program_en, version))
                    print(Studio_ZH)  # Studio.py 中的中文版工作室宣告
                case 10:  # 功能10：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
                case _:  # 其他錯誤的功能選擇輸入
                    print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後重新輸入，現正返回「功能選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
else:  # 如果使用者誤將本程式作為模組引用
    print("\033[38;5;197m本程式為「中華民國（臺灣）TPASS 通勤月票計算程式」的主入口\n請直接運行 Main.py，而非透過其他模組引入本程式\033[0m\a\n")  # 輸出提示訊息提醒使用者正確使用方式
    sys.exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"
