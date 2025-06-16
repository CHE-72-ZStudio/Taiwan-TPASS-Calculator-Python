"""
Func.py
"""

import sys
import time

TPASS_city = ["顯示使用說明", "基北北桃生活圈", "桃竹竹苗生活圈", "中彰投苗生活圈", "南高屏生活圈", "北宜生活圈", "花蓮縣", "雲林縣",
              "澎湖縣", "臺東縣：臺東縣都市內 $299", "大嘉義生活圈：嘉義縣市跨城際 $399", "返回上層選單", "結束程式運行"]  # 城市選擇平臺
KPPT_plan = ["基北北桃跨城際 成人 $1,200", "基北北桃跨城際 學生 $1,200", "基隆市都市內 $288"]
TCCM_plan = ["桃竹竹苗跨城際 $1,200", "桃竹竹跨城際 $799", "竹竹苗跨城際 $699", "竹竹跨城際 $288"]
CCTM_plan = ["中彰投苗跨城際 臺中市民 $699", "中彰投苗跨城際 非臺中市民 $999", "臺中市都市內 臺中市民 $299",
             "臺中市都市內 非臺中市民 $599", "彰化縣都市內 $699", "南投縣都市內 $699"]
NKP_plan = ["南高屏跨城際 $999", "大臺南公車 $299", "大臺南公車+臺鐵 $399", "高雄市區 $399",
            "屏東縣公車暢行 $299", "屏東縣無限暢行 $399", "高雄市公車暢遊（MeNGo 非 TPASS） $199"]
BY_plan = ["北宜跨城際及雙北 $2,300？", "北北宜跨城際通勤 $1,800", "宜蘭縣縣境內 $750"]
HL_plan = ["花蓮縣都市內 $199", "花蓮縣都市內 含公路客運 $399"]
YL_plan = ["雲林縣都市內 $199", "雲林縣都市內 含臺鐵跨區7站 $399"]
PH_plan = ["澎湖縣公車 $210？", "澎湖縣車船 $1000？"]


class RangeError(ValueError):
    """
    例外類別：當數值超出自訂義的合理範圍時拋出的自訂例外，繼承自內建的數值錯誤
    """
    pass


def _plan_input(city, city_plan):
    """
    內部函數：

    參數：
        * city (int)：
        * city_plan (list)：

    回傳：
        * plan (int)：

    拋出：
        * ValueError：
        * RangeError：
    """
    print("\n這裡是「方案選擇平臺」，請選擇您想要分析的 \033[38;5;43m{}\033[0m 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
    print_list(city_plan, 1)  # 呼叫列表印出函式，印出「各城市生活圈」的選單列表
    plan = check_input("--> \033[0m", 1, len(city_plan))  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至方案變數，依序傳入 詢問內容、最小數值、最大數值
    print("\n您選擇了 \033[38;5;43m{}\033[0m 當中的 \033[38;5;43m{}\033[0m 月票方案".format(TPASS_city[city], city_plan[plan - 1]))
    return plan


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


def analyze(name, ver):
    """
    用於 Main.py 呼叫的選單函數，用於選擇不同的生活圈與具體的月票方案後，呼叫 calculate 函數
    也是本程式的核心分析邏輯部分
    """
    while True:
        city = -1
        try:
            print("\n這裡是「都會選擇平臺」，請選擇您經常通勤的生活圈")  # 輸出「都會選擇平臺」的提示訊息
            print_list(TPASS_city)  # 呼叫列表印出函式，印出「都會選擇平臺」的選單列表
            city = check_input("--> \033[0m", 0, len(TPASS_city) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至時間變數，依序傳入 詢問內容、最小數值、最大數值

            match city:
                case 0:  # 城市0：顯示使用說明
                    pass
                case 1:  # 城市1：基北北桃生活圈
                    plan = _plan_input(city, KPPT_plan)
                    match plan:
                        case 1:  # 月票1：基北北桃跨城際 成人 $1,200
                            trans = ["結束輸入，開始計算", "臺北捷運", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_full, bus_half = 15, 7
                        case 2:  # 月票2：基北北桃跨城際 學生 $1,200
                            trans = ["結束輸入，開始計算", "臺北捷運", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_full, bus_half = 12, 6
                        case 3:  # 月票3：基隆市都市內 $288
                            trans = ["結束輸入，開始計算", "基隆市 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 288

                case 2:  # 城市2：桃竹竹苗生活圈
                    plan = _plan_input(city, TCCM_plan)
                    match plan:
                        case 1:  # 月票1：桃竹竹苗跨城際 $1,200
                            trans = ["結束輸入，開始計算", "桃園/新竹/苗栗 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 1200
                        case 2:  # 月票2：桃竹竹跨城際 $799
                            trans = ["結束輸入，開始計算", "桃園/新竹 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 799
                        case 3:  # 月票3：竹竹苗跨城際 $699
                            trans = ["結束輸入，開始計算", "新竹/苗栗 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 4:  # 月票4：竹竹跨城際 $288
                            trans = ["結束輸入，開始計算", "新竹（縣/市）市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 288
                case 3:  # 城市3：中彰投苗生活圈
                    plan = _plan_input(city, CCTM_plan)
                    match plan:
                        case 1:  # 月票1：中彰投苗跨城際 臺中市民 $699
                            trans = ["結束輸入，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 2:  # 月票2：中彰投苗跨城際 非臺中市民 $999
                            trans = ["結束輸入，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 999
                        case 3:  # 月票3：臺中市都市內 臺中市民 $299
                            trans = ["結束輸入，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 299
                        case 4:  # 月票4：臺中市都市內 非臺中市民 $599
                            trans = ["結束輸入，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 599
                        case 5:  # 月票5：彰化縣都市內 $699
                            trans = ["結束輸入，開始計算", "彰化縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 6:  # 月票6：南投縣都市內 $699
                            trans = ["結束輸入，開始計算", "南投縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                case 4:  # 城市4：南高屏生活圈
                    plan = _plan_input(city, NKP_plan)
                    match plan:
                        case 1:  # 月票1：南高屏跨城際 $999
                            trans = ["結束輸入，開始計算", "臺南/高雄/屏東 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]  # TODO
                            price = 999
                        case 2:  # 月票2：大臺南公車 $299
                            trans = ["結束輸入，開始計算", "大臺南公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 299
                        case 3:  # 月票3：大臺南公車+臺鐵 $399
                            trans = ["結束輸入，開始計算", "大臺南公車", "臺灣鐵路", "結束程式運行"]
                            price = 399
                        case 4:  # 月票4：高雄市區 $399
                            trans = ["結束輸入，開始計算", "高雄市 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]  # TODO
                            price = 399
                        case 5:  # 月票5：屏東縣公車暢行 $299
                            trans = ["結束輸入，開始計算", "屏東縣 市區公車", "公路客運", "結束程式運行"]
                            price = 299
                        case 6:  # 月票6：屏東縣無限暢行 $399
                            trans = ["結束輸入，開始計算", "屏東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                        case 7:  # 月票7：高雄市公車暢遊 MeNGo（非 TPASS） $199
                            trans = ["結束輸入，開始計算", "高雄市 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 399
                case 5:  # 城市5：北宜生活圈
                    plan = _plan_input(city, BY_plan)
                    match plan:
                        case 1:  # 月票1：北宜跨城際及雙北 $2,300  # TODO:UNKNOWN
                            trans = ["結束輸入，開始計算", "北宜通勤國道客運", "臺灣鐵路", "宜蘭縣 市區公車", "結束程式運行"]
                            price = 2300
                            continue  # 由於信息不完整，直接跳過本方案的計算，回到「都會選擇平臺」
                        case 2:  # 月票2：北北宜跨城際通勤 $1,800
                            trans = ["結束輸入，開始計算", "臺灣鐵路", "公路客運", "宜蘭縣 市區公車", "結束程式運行"]
                            price = 1800
                        case 3:  # 月票3：宜蘭縣縣境內 $750
                            trans = ["結束輸入，開始計算", "宜蘭縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 750
                case 6:  # 城市6：花蓮縣
                    plan = _plan_input(city, HL_plan)
                    match plan:
                        case 1:  # 月票1：花蓮縣都市內 $199
                            trans = ["結束輸入，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 199
                        case 2:  # 月票2：花蓮縣都市內 含公路客運 $399
                            trans = ["結束輸入，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                case 7:  # 城市7：雲林縣
                    plan = _plan_input(city, YL_plan)
                    match plan:
                        case 1:  # 月票1：雲林縣都市內 $199
                            trans = ["結束輸入，開始計算", "雲林縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 199
                        case 2:  # 月票2：雲林縣都市內 含臺鐵跨區7站 $399
                            trans = ["結束輸入，開始計算", "雲林縣 市區公車", "臺灣鐵路（含 彰化/嘉義 跨區 7 站）", "公路客運", "結束程式運行"]
                            price = 399
                case 8:  # 城市8：澎湖縣
                    plan = _plan_input(city, PH_plan)
                    match plan:
                        case 1:  # 月票1：澎湖縣公車 $210  # TODO 150?
                            trans = ["結束輸入，開始計算", "澎湖縣 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 210
                        case 2:  # 月票2：澎湖縣車船 $1000  #TODO 400?
                            trans = ["結束輸入，開始計算", "澎湖縣 市區公車", "馬公-望安-七美 交通船", "結束程式運行"]
                            price = 1000
                    continue  # 由於信息不完整，直接跳過本方案的計算，回到「都會選擇平臺」
                case 9:  # 城市9：臺東縣：臺東縣都市內 $299
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    trans = ["結束輸入，開始計算", "臺東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                    price = 299
                case 10:  # 城市10：大嘉義生活圈：嘉義縣市跨城際 $399
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    trans = ["結束輸入，開始計算", "嘉義縣/市 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                    price = 399
                case 10:  # 城市11：返回上層選單
                    print("\033[38;5;43m正在返回「功能選擇平臺」\033[0m\n\a")  # 輸出提示訊息與通知聲音
                    return  # 回到「功能選擇平臺」
                case 11:  # 城市12：結束程式運行
                    print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    sys.exit(0)  # 呼叫系統正常結束本程式運行
        except RangeError:  # 如果使用者輸入超出正常範圍的內容
            print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「都會選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「都會選擇平臺」
        except ValueError:  # 如果使用者輸入無法轉換成整數的內容
            print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「都會選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「都會選擇平臺」
        except Exception:  # 例外處理，捕捉其他未預期的錯誤
            print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「都會選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
            continue  # 回到「都會選擇平臺」

        # 直接將 calculate() 的邏輯接在這裡？使用參數 trans(list) price(int)
        total, result = 0, ""
        if total < price:
            result += "本月無須另外購買 TPASS 通勤月票，共計花費 {} 元".format(total)
        elif total == price:
            result += "本月無論是否購買 TPASS 通勤月票，皆要花費 {} 元".format(price)
        elif total > price:
            result += "建議本月購買 {} 方案的 TPASS 通勤月票，可省下 {} 元".format("", total - price)
        print(result)


        # 直接將 output() 的邏輯接在這裡？
        try:
            with open("TPASS_Result.txt", "a+", encoding="UTF-8") as file:
                time_stamp = time.localtime()
                file.write("{}-{}-{} {}:{}\n".format(time_stamp.tm_year, time_stamp.tm_mon, time_stamp.tm_mday, time_stamp.tm_hour, time_stamp.tm_min))
                file.write("{}\n".format(result))
                file.write("「{}」Ver{}\n".format(name, ver))
                file.write("{}\n".format("=" * 36))
        except:
            print("encounter some errors when trying to write \"TPASS_Result.txt\"")