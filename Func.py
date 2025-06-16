"""
Func.py
"""

import sys

TPASS_city = ["顯示使用說明", "基北北桃生活圈", "桃竹竹苗生活圈", "中彰投苗生活圈", "南高屏生活圈", "北宜生活圈", "花蓮縣", "雲林縣",
              "臺東縣：臺東縣都市內 $299", "大嘉義生活圈：嘉義縣市跨城際 $399", "返回上層選單", "結束程式運行"]  # 城市選擇平臺
KPPT_type = ["基北北桃跨城際 $1,200", "基隆市都市內 $288"]
TCCM_type = ["桃竹竹苗跨城際 $1,200", "桃竹竹跨城際 $799", "竹竹苗跨城際 $699", "竹竹跨城際 $288"]
CCTM_type = ["中彰投苗跨城際 臺中市民 $699", "中彰投苗跨城際 非臺中市民 $999", "臺中市都市內 臺中市民 $299",
             "臺中市都市內 非臺中市民 $599", "彰化縣都市內 $699", "南投縣都市內 $699"]
NKP_type = ["南高屏跨城際 $999", "臺南市都市內 $299", "臺南市都市內 含臺鐵 $399", "高雄市都市內 $399",
            "屏東縣都市內 $299", "屏東縣都市內 含臺鐵 $399"]
BY_type = ["北宜跨城際及雙北 $2,300", "北宜跨城際 $1,800", "宜蘭縣都市內 $750"]
HL_type = ["花蓮縣都市內 $199", "花蓮縣都市內 含公路客運 $399"]
YL_type = ["雲林縣都市內 $199", "雲林縣都市內 含臺鐵跨區7站 $399"]


class RangeError(ValueError):
    """
    例外類別：當數值超出自訂義的合理範圍時拋出的自訂例外，繼承自內建的數值錯誤
    """
    pass


def check_input(prompt, range_min=None, range_max=None):
    """
    公開函數：讀取使用者輸入的內容，轉換成整數並進行範圍驗證，在輸入無效或超出範圍時會拋出例外
    由 Gemini Code Assist 提供建議，符合 DRY 原則

    參數：
        * prompt (str)：顯示給使用者的提示訊息
        * range_min (int, optional)：範圍內允許出現的最小值
        * range_max (int, optional)：範圍內允許出現的最大值

    回傳：
        * value (int)：通過驗證的整數輸入

    拋出：
        * ValueError：如果輸入無法轉換為整數時自動拋出的內建例外
        * RangeError：如果輸入超出指定的範圍時手動拋出的自訂例外
    """
    value = int(input(prompt))  # 讀取使用者輸入後嘗試轉換成整數，若無法轉換會自動拋出 ValueError

    # 如果有傳入 最小／最大值，則檢查使用者輸入是否超出範圍，若超出範圍會手動拋出自訂的 RangeError 例外，表示數值超出合理範圍
    if range_min is not None and value < range_min:
        raise RangeError
    if range_max is not None and value > range_max:
        raise RangeError

    return value  # 回傳正確轉換成整數的數值


def print_list(content_list, offset=0):  # TODO more Pythonic?
    """
    公開函數：用於遍歷印出列表，並能顯示中文頓號與輸入用箭頭

    參數：
        * content_list (list)：要被遍歷印出的列表資料
        * offset (int, optional)：在印出數值時的偏移量，預設為 0 表示不偏移，「類別選擇平臺」為 1 以適應類別編號
    """
    for i in range(len(content_list)):
        if i == len(content_list) - 1:  # 如果是列表中的最後一項
            print("{}: {}\n".format(i + offset, content_list[i]), end='')  # 印出編號與列表文字
        else:
            print("\033[38;5;43m{}: {}".format(i + offset, content_list[i]), end='、')  # 印出編號與列表文字，以頓號分隔元素


def analyze():
    """
    用於 Main.py 呼叫的分析函數，也是本程式的核心分析邏輯部分
    """
    while True:
        print("這裡是「都會選擇平臺」，請選擇您經常通勤的生活圈")
        print_list(TPASS_city)

        try:  # 讀取使用者輸入至時間變數，並嘗試轉換成整數
            city = int(input())
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「時間選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「都會選擇平臺」

        match city:
            case 0:  # 城市0：顯示使用說明
                pass
            case 1:  # 城市1：基北北桃生活圈
                pass
            case 2:  # 城市2：桃竹竹苗生活圈
                pass
            case 3:  # 城市3：中彰投苗生活圈
                pass
            case 4:  # 城市4：南高屏生活圈
                pass
            case 5:  # 城市5：北宜生活圈
                pass
            case 6:  # 城市6：花蓮縣
                pass
            case 7:  # 城市7：雲林縣
                pass
            case 8:  # 城市8：臺東縣：臺東縣都市內 $299
                pass
            case 9:  # 城市9：大嘉義生活圈：嘉義縣市跨城際 $399
                pass
            case 10:  # 城市10：返回上層選單
                print("\033[38;5;43m正在返回「功能選擇平臺」\033[0m\n\a")  # 輸出提示訊息與通知聲音
                return  # 回到「功能選擇平臺」
            case 11:  # 城市11：結束程式運行
                print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                sys.exit(0)  # 呼叫系統正常結束本程式運行
            case _:
                print("\033[38;5;197m您的輸入內容出現錯誤，請檢查後輸入正確選項，現正返回「都會選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「都會選擇平臺」
