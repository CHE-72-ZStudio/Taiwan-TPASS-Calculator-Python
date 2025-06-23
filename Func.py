"""
Func.py
此模組提供分析、計算、輸出的相關功能，包含：

* _plan_input：詢問使用者的「方案選擇平臺」，並回傳最終選擇的月票方案編號
* check_input：檢查使用者輸入是否無效或超出範圍，並回傳輸入數值或拋出對應例外
* print_list：遍歷印出列表，並顯示編號與頓號
* analyze：分析函數，本程式的核心分析邏輯部分
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
        * name (str)

    拋出：
        * ValueError：
        * RangeError：
    """
    print("\n這裡是「方案選擇平臺」，請選擇您想要分析的 \033[38;5;43m{}\033[0m 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
    print_list(city_plan, 1)  # 呼叫列表印出函式，印出「各城市生活圈」的選單列表
    plan = check_input("--> \033[0m", 1, len(city_plan))  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至方案變數，依序傳入 詢問內容、最小數值、最大數值
    name = city_plan[plan - 1]
    print("\n您選擇了 \033[38;5;43m{}\033[0m 當中的 \033[38;5;43m{}\033[0m 月票方案".format(TPASS_city[city], name))
    return plan, name


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


def analyze(program, ver):
    """
    用於 Main.py 呼叫的選單函數，用於選擇不同的生活圈與具體的月票方案後，呼叫 calculate 函數
    也是本程式的核心分析邏輯部分
    """
    while True:
        city = -1
        try:
            print("\n這裡是「都會選擇平臺」，請選擇您經常通勤的生活圈")  # 輸出「都會選擇平臺」的提示訊息
            print_list(TPASS_city)  # 呼叫列表印出函式，印出「都會選擇平臺」的選單列表
            city = check_input("--> \033[0m", 0, len(TPASS_city) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至生活圈變數，依序傳入 詢問內容、最小數值、最大數值

            match city:
                case 0:  # 城市0：顯示使用說明
                    pass
                case 1:  # 城市1：基北北桃生活圈
                    plan, name = _plan_input(city, KPPT_plan)
                    match plan:
                        case 1:  # 月票1：基北北桃跨城際 成人 $1,200
                            trans_list = ["結束輸入，開始計算", "臺北捷運+環狀線", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_price = [15, 7]
                        case 2:  # 月票2：基北北桃跨城際 學生 $1,200
                            trans_list = ["結束輸入，開始計算", "臺北捷運+環狀線", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_price = [12, 6]
                        case 3:  # 月票3：基隆市都市內 $288
                            trans_list = ["結束輸入，開始計算", "基隆市 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 288

                case 2:  # 城市2：桃竹竹苗生活圈
                    plan, name = _plan_input(city, TCCM_plan)
                    match plan:
                        case 1:  # 月票1：桃竹竹苗跨城際 $1,200
                            trans_list = ["結束輸入，開始計算", "桃園/新竹/苗栗 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 1200
                        case 2:  # 月票2：桃竹竹跨城際 $799
                            trans_list = ["結束輸入，開始計算", "桃園/新竹 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 799
                        case 3:  # 月票3：竹竹苗跨城際 $699
                            trans_list = ["結束輸入，開始計算", "新竹/苗栗 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 4:  # 月票4：竹竹跨城際 $288
                            trans_list = ["結束輸入，開始計算", "新竹（縣/市）市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 288
                case 3:  # 城市3：中彰投苗生活圈
                    plan, name = _plan_input(city, CCTM_plan)
                    match plan:
                        case 1:  # 月票1：中彰投苗跨城際 臺中市民 $699
                            trans_list = ["結束輸入，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 2:  # 月票2：中彰投苗跨城際 非臺中市民 $999
                            trans_list = ["結束輸入，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 999
                        case 3:  # 月票3：臺中市都市內 臺中市民 $299
                            trans_list = ["結束輸入，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 299
                        case 4:  # 月票4：臺中市都市內 非臺中市民 $599
                            trans_list = ["結束輸入，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 599
                        case 5:  # 月票5：彰化縣都市內 $699
                            trans_list = ["結束輸入，開始計算", "彰化縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 6:  # 月票6：南投縣都市內 $699
                            trans_list = ["結束輸入，開始計算", "南投縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                case 4:  # 城市4：南高屏生活圈
                    plan, name = _plan_input(city, NKP_plan)
                    match plan:
                        case 1:  # 月票1：南高屏跨城際 $999
                            trans_list = ["結束輸入，開始計算", "臺南/高雄/屏東 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]  # TODO
                            price = 999
                        case 2:  # 月票2：大臺南公車 $299
                            trans_list = ["結束輸入，開始計算", "大臺南公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 299
                        case 3:  # 月票3：大臺南公車+臺鐵 $399
                            trans_list = ["結束輸入，開始計算", "大臺南公車", "臺灣鐵路", "結束程式運行"]
                            price = 399
                        case 4:  # 月票4：高雄市區 $399
                            trans_list = ["結束輸入，開始計算", "高雄市 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]  # TODO
                            price = 399
                        case 5:  # 月票5：屏東縣公車暢行 $299
                            trans_list = ["結束輸入，開始計算", "屏東縣 市區公車", "公路客運", "結束程式運行"]
                            price = 299
                        case 6:  # 月票6：屏東縣無限暢行 $399
                            trans_list = ["結束輸入，開始計算", "屏東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                        case 7:  # 月票7：高雄市公車暢遊 MeNGo（非 TPASS） $199
                            trans_list = ["結束輸入，開始計算", "高雄市 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 399
                case 5:  # 城市5：北宜生活圈
                    plan, name = _plan_input(city, BY_plan)
                    match plan:
                        case 1:  # 月票1：北宜跨城際及雙北 $2,300  # TODO: Search for Official Info.
                            trans_list = ["結束輸入，開始計算", "北宜通勤國道客運", "臺灣鐵路", "臺北捷運", "大臺北地區 市區公車", "宜蘭縣 市區公車", "結束程式運行"]
                            price = 2300
                            print("\033[38;5;197m由於缺少官方完整資訊，目前無法計算「北宜跨城際及雙北 $2,300」的月票方案\033[0m\a\n")  # 輸出提示訊息與通知聲音
                            continue  # 由於信息不完整，直接跳過本方案的計算，回到「都會選擇平臺」
                        case 2:  # 月票2：北北宜跨城際通勤 $1,800
                            trans_list = ["結束輸入，開始計算", "臺灣鐵路", "公路客運", "宜蘭縣 市區公車", "結束程式運行"]
                            price = 1800
                        case 3:  # 月票3：宜蘭縣縣境內 $750
                            trans_list = ["結束輸入，開始計算", "宜蘭縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 750
                case 6:  # 城市6：花蓮縣
                    plan, name = _plan_input(city, HL_plan)
                    match plan:
                        case 1:  # 月票1：花蓮縣都市內 $199
                            trans_list = ["結束輸入，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 199
                        case 2:  # 月票2：花蓮縣都市內 含公路客運 $399
                            trans_list = ["結束輸入，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                case 7:  # 城市7：雲林縣
                    plan, name = _plan_input(city, YL_plan)
                    match plan:
                        case 1:  # 月票1：雲林縣都市內 $199
                            trans_list = ["結束輸入，開始計算", "雲林縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 199
                        case 2:  # 月票2：雲林縣都市內 含臺鐵跨區7站 $399
                            trans_list = ["結束輸入，開始計算", "雲林縣 市區公車", "臺灣鐵路（含 彰化/嘉義 跨區 7 站）", "公路客運", "結束程式運行"]
                            price = 399
                case 8:  # 城市8：澎湖縣  # TODO: Search for Official Info.
                    plan, name = _plan_input(city, PH_plan)
                    match plan:
                        case 1:  # 月票1：澎湖縣公車 $210  # 150 or 210 ?
                            trans_list = ["結束輸入，開始計算", "澎湖縣 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 210
                        case 2:  # 月票2：澎湖縣車船 $1000  # 400 or 1000 ?
                            trans_list = ["結束輸入，開始計算", "澎湖縣 市區公車", "馬公-望安-七美 交通船", "結束程式運行"]
                            price = 1000
                    print("\033[38;5;197m由於缺少官方完整資訊，目前無法計算「澎湖縣」的所有月票方案\033[0m\a\n")  # 輸出提示訊息與通知聲音
                    continue  # 由於信息不完整，直接跳過本方案的計算，回到「都會選擇平臺」
                case 9:  # 城市9：臺東縣：臺東縣都市內 $299
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    name = TPASS_city[city]
                    trans_list = ["結束輸入，開始計算", "臺東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                    price = 299
                case 10:  # 城市10：大嘉義生活圈：嘉義縣市跨城際 $399
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    name = TPASS_city[city]
                    trans_list = ["結束輸入，開始計算", "嘉義縣/市 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
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

        amount, times_list = [0 for t in range(len(trans_list))], [0 for t in range(len(trans_list))]
        tp_metro_original = 0

        while True:
            try:
                print("\n這裡是「交通選擇平臺」，請選擇您要搭乘的大眾運輸工具")  # 輸出「數據輸入平臺」的提示訊息
                print_list(trans_list)  # 呼叫列表印出函式，印出「都會選擇平臺」的選單列表
                trans = check_input("--> \033[0m", 0, len(trans_list) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至交通工具變數，依序傳入 詢問內容、最小數值、最大數值

                match trans_list[trans]:
                    case "結束輸入，開始計算":
                        print("calculating")
                        break
                    case "結束程式運行":
                        print("exiting")
                        sys.exit(0)
                    case "臺北捷運+環狀線":  # 呼叫 臺北捷運+環狀線 專用輸入函式
                        print("You are inputing taipei metro")
                        print("just input 0")
                        for m in range(20, 70, 5):
                            times = check_input("NT${} How many times".format(m), 0)
                            times_list[trans] += times
                            tp_metro_original += times * m
                        if 11 <= times_list[trans] <= 20:
                            amount[trans] = tp_metro_original * 0.95
                        elif 21 <= times_list[trans] <= 40:
                            amount[trans] = tp_metro_original * 0.9
                        elif 41 <= times_list[trans]:
                            amount[trans] = tp_metro_original * 0.85
                        else:
                            amount[trans] = tp_metro_original
                    case "大臺北地區 市區公車":  # 呼叫 大臺北地區 市區公車 專用輸入函式
                        print("You are inputing taipei bus")
                        print("just input 0")
                        for m in bus_price:
                            times = check_input("NT${} How many times".format(m), 0)
                            times_list[trans] += times
                            amount[trans] += times * m
                    case _:  # 呼叫 一般輸入函式
                        print("You are inputing {}".format(trans_list[trans]))
                        while True:
                            money = check_input("How much money?", 0)
                            if money == 0:
                                break
                            times = check_input("NT${} How much times_list?".format(money), 0)
                            if times == 0:
                                break
                            times_list[trans] += times
                            amount[trans] += times * money

            except RangeError:  # 如果使用者輸入超出正常範圍的內容
                print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「交通選擇平臺」
            except ValueError:  # 如果使用者輸入無法轉換成整數的內容
                print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「交通選擇平臺」
            except Exception as e:  # 例外處理，捕捉其他未預期的錯誤
                print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                print(e)  # TODO: remove this after the test is done
                continue  # 回到「交通選擇平臺」

        # 直接將 calculate() 的邏輯接在這裡？使用參數 trans_list(list) price(int)
        total, result = 0, "本月共搭乘："
        for m in amount:
            total += m

        for t in range(1, len(trans_list) - 1):
            result += "  {}：{}次，共{:,}元".format(trans_list[t], times_list[t], amount[t])  # TODO 頓號

        if total < price:
            result += "\n本月無須另外購買 TPASS 通勤月票，共計花費 {:,} 元".format(total)
        elif total == price:
            result += "\n本月無論是否購買 TPASS 通勤月票，皆要花費 {:,} 元".format(price)
        elif total > price:
            result += "\n建議本月購買「{}」方案的 TPASS 通勤月票，可省下 {:,} 元".format(name, total - price)
        print(result)


        # 直接將 output() 的邏輯接在這裡？
        try:
            with open("TPASS_Result.txt", "a+", encoding="UTF-8") as file:
                stamp = time.localtime()
                file.write("{}-{}-{} {}:{}\n".format(stamp.tm_year, stamp.tm_mon, stamp.tm_mday, stamp.tm_hour, stamp.tm_min))
                file.write("{}\n".format(result))
                file.write("「{}」Ver{}\n".format(program, ver))
                file.write("{}\n".format("=" * 36))
        except:
            print("encounter some errors when trying to write \"TPASS_Result.txt\"")
        else:
            print("write file successfully")
            print("going back to city selection")