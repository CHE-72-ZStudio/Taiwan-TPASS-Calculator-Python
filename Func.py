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
KPPT_plan = ["基北北桃跨城際 成人 $1,200", "基北北桃跨城際 學生 $1,200", "基隆市都市內 $288"]  # 基北北桃生活圈的方案選擇平臺
TCCM_plan = ["桃竹竹苗跨城際 $1,200", "桃竹竹跨城際 $799", "竹竹苗跨城際 $699", "竹竹跨城際 $288"]  #桃竹竹苗生活圈 的方案選擇平臺
CCTM_plan = ["中彰投苗跨城際 臺中市民 $699", "中彰投苗跨城際 非臺中市民 $999", "臺中市都市內 臺中市民 $299",
             "臺中市都市內 非臺中市民 $599", "彰化縣都市內 $699", "南投縣都市內 $699"]  # 中彰投苗生活圈的方案選擇平臺
NKP_plan = ["南高屏跨城際 $999", "大臺南公車 $299", "大臺南公車+臺鐵 $399", "高雄市區 $399",
            "屏東縣公車暢行 $299", "屏東縣無限暢行 $399", "高雄市公車暢遊（MeNGo 非 TPASS） $199"]  # 南高屏生活圈的方案選擇平臺
BY_plan = ["北宜跨城際及雙北 $2,300", "北北宜跨城際通勤 $1,800", "宜蘭縣縣境內 $750"]  # 北宜生活圈的方案選擇平臺
HL_plan = ["花蓮縣都市內 $199", "花蓮縣都市內 含公路客運 $399"]  # 花蓮縣的方案選擇平臺
YL_plan = ["雲林縣都市內 $199", "雲林縣都市內 含臺鐵跨區7站 $399"]  # 雲林縣的方案選擇平臺
PH_plan = ["澎湖縣公車 $150", "澎湖縣車船 $400"]  # 澎湖縣的方案選擇平臺


class RangeError(ValueError):
    """
    例外類別：當數值超出自訂義的合理範圍時拋出的自訂例外，繼承自內建的數值錯誤
    """
    pass


if __name__ == "__main__":  # 如果使用者誤啟動本程式
    print("\033[38;5;197m這是 Main.py 呼叫的模組\n請改為運行 Main.py，而非直接運行本程式\n我們即將結束此模組的運行\033[0m")  # 輸出提示訊息提醒使用者正確使用方式
    exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"


def _plan_input(city, city_plan):
    """
    內部函數：用於詢問使用者特定生活圈可用月票方案的「方案選擇平臺」，並回傳在該生活圈下，最終選擇的月票方案編號

    參數：
        * city (int)：使用者先前輸入的生活圈變數，用於從 TPASS_city[] 中讀取生活圈的名稱
        * city_plan (list)：讓使用者選擇的生活圈可用月票方案列表

    回傳：
        * plan (int)：使用者最終選擇的月票方案編號，作為後續設定可用交通工具列表與月票購買金額時使用
        * name (str)：使用者最終選擇的月票方案名稱，作為後續輸出計算結果時使用

    拋出：
        * ValueError：如果輸入無法轉換為整數時自動拋出的內建例外（由 check_input() 傳播）
        * RangeError：如果輸入超出指定的範圍時手動拋出的自訂例外（由 check_input() 傳播）
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
        * offset (int, optional)：在印出數值時的偏移量，預設為 0 表示不偏移，「方案選擇平臺」為 1 以適應月票方案編號
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
    # 無窮迴圈，在必要時使用 return 離開迴圈或使用 sys.exit() 結束程式
    while True:
        city = -1
        try:
            print("\n這裡是「都會選擇平臺」，請選擇您經常通勤的 生活圈／縣市")  # 輸出「都會選擇平臺」的提示訊息
            print_list(TPASS_city)  # 呼叫列表印出函式，印出「都會選擇平臺」的選單列表
            city = check_input("--> \033[0m", 0, len(TPASS_city) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至生活圈變數，依序傳入 詢問內容、最小數值、最大數值

            match city:
                case 0:  # 城市0：顯示使用說明
                    print(analyze_manual)  # 印出「計算分析函式」的使用說明
                    continue  # 回到「都會選擇平臺」
                case 1:  # 城市1：基北北桃生活圈
                    plan, name = _plan_input(city, KPPT_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 基北北桃月票1：基北北桃跨城際 成人 $1,200
                            trans_list = ["輸入完成，開始計算", "臺北捷運+環狀線", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_price = [15, 7]
                        case 2:  # 基北北桃月票2：基北北桃跨城際 學生 $1,200
                            trans_list = ["輸入完成，開始計算", "臺北捷運+環狀線", "大臺北地區 市區公車", "新北捷運/輕軌", "臺灣鐵路", "桃園捷運", "桃園/基隆 市區公車", "公路客運", "結束程式運行"]
                            price = 1200
                            bus_price = [12, 6]
                        case 3:  # 基北北桃月票3：基隆市都市內 $288
                            trans_list = ["輸入完成，開始計算", "基隆市 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 288

                case 2:  # 城市2：桃竹竹苗生活圈
                    plan, name = _plan_input(city, TCCM_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 桃竹竹苗月票1：桃竹竹苗跨城際 $1,200
                            trans_list = ["輸入完成，開始計算", "桃園/新竹/苗栗 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 1200
                        case 2:  # 桃竹竹苗月票2：桃竹竹跨城際 $799
                            trans_list = ["輸入完成，開始計算", "桃園/新竹 市區公車", "桃園捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 799
                        case 3:  # 桃竹竹苗月票3：竹竹苗跨城際 $699
                            trans_list = ["輸入完成，開始計算", "新竹/苗栗 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 4:  # 桃竹竹苗月票4：竹竹跨城際 $288
                            trans_list = ["輸入完成，開始計算", "新竹（縣/市）市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 288
                case 3:  # 城市3：中彰投苗生活圈
                    plan, name = _plan_input(city, CCTM_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 中彰投苗月票1：中彰投苗跨城際 臺中市民 $699
                            trans_list = ["輸入完成，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 2:  # 中彰投苗月票2：中彰投苗跨城際 非臺中市民 $999
                            trans_list = ["輸入完成，開始計算", "臺中/彰化/南投/苗栗 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 999
                        case 3:  # 中彰投苗月票3：臺中市都市內 臺中市民 $299
                            trans_list = ["輸入完成，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 299
                        case 4:  # 中彰投苗月票4：臺中市都市內 非臺中市民 $599
                            trans_list = ["輸入完成，開始計算", "臺中市 市區公車", "臺中捷運", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 599
                        case 5:  # 中彰投苗月票5：彰化縣都市內 $699
                            trans_list = ["輸入完成，開始計算", "彰化縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                        case 6:  # 中彰投苗月票6：南投縣都市內 $699
                            trans_list = ["輸入完成，開始計算", "南投縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 699
                case 4:  # 城市4：南高屏生活圈
                    plan, name = _plan_input(city, NKP_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 南高屏月票1：南高屏跨城際 $999
                            trans_list = ["輸入完成，開始計算", "臺南/高雄/屏東 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 999
                        case 2:  # 南高屏月票2：大臺南公車 $299
                            trans_list = ["輸入完成，開始計算", "大臺南公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 299
                        case 3:  # 南高屏月票3：大臺南公車+臺鐵 $399
                            trans_list = ["輸入完成，開始計算", "大臺南公車", "臺灣鐵路", "結束程式運行"]
                            price = 399
                        case 4:  # 南高屏月票4：高雄市區 $399
                            trans_list = ["輸入完成，開始計算", "高雄市 市區公車", "高雄捷運", "高雄輕軌", "高雄渡輪", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                        case 5:  # 南高屏月票5：屏東縣公車暢行 $299
                            trans_list = ["輸入完成，開始計算", "屏東縣 市區公車", "公路客運", "結束程式運行"]
                            price = 299
                        case 6:  # 南高屏月票6：屏東縣無限暢行 $399
                            trans_list = ["輸入完成，開始計算", "屏東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                        case 7:  # 南高屏月票7：高雄市公車暢遊 MeNGo（非 TPASS） $199
                            trans_list = ["輸入完成，開始計算", "高雄市 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 399
                case 5:  # 城市5：北宜生活圈
                    plan, name = _plan_input(city, BY_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 北宜月票1：北宜跨城際及雙北 $2,300
                            trans_list = ["輸入完成，開始計算", "北宜通勤國道客運", "臺灣鐵路", "臺北捷運+環狀線", "大臺北地區 市區公車", "宜蘭縣 市區公車", "新北捷運/輕軌", "桃園捷運", "桃園/基隆 市區公車", "結束程式運行"]
                            price = 2300
                        case 2:  # 北宜月票2：北北宜跨城際通勤 $1,800
                            trans_list = ["輸入完成，開始計算", "臺灣鐵路", "公路客運", "宜蘭縣 市區公車", "結束程式運行"]
                            price = 1800
                        case 3:  # 北宜月票3：宜蘭縣縣境內 $750
                            trans_list = ["輸入完成，開始計算", "宜蘭縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 750
                case 6:  # 城市6：花蓮縣
                    plan, name = _plan_input(city, HL_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 花蓮縣月票1：花蓮縣都市內 $199
                            trans_list = ["輸入完成，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "結束程式運行"]
                            price = 199
                        case 2:  # 花蓮縣月票2：花蓮縣都市內 含公路客運 $399
                            trans_list = ["輸入完成，開始計算", "花蓮縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 399
                case 7:  # 城市7：雲林縣
                    plan, name = _plan_input(city, YL_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 雲林月票1：雲林縣都市內 $199
                            trans_list = ["輸入完成，開始計算", "雲林縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                            price = 199
                        case 2:  # 雲林月票2：雲林縣都市內 含臺鐵跨區7站 $399
                            trans_list = ["輸入完成，開始計算", "雲林縣 市區公車", "臺灣鐵路（含 彰化/嘉義 跨區 7 站）", "公路客運", "結束程式運行"]
                            price = 399
                case 8:  # 城市8：澎湖縣
                    plan, name = _plan_input(city, PH_plan)  # 呼叫 _plan_input() 函數取得月票方案與名稱，依序傳入生活圈編號與可用月票方案
                    match plan:
                        case 1:  # 澎湖縣月票1：澎湖縣公車 $150
                            trans_list = ["輸入完成，開始計算", "澎湖縣 市區公車", "結束程式運行"]  # TODO 僅一種交通選擇，可以簡化
                            price = 150
                        case 2:  # 澎湖縣月票2：澎湖縣車船 $400
                            trans_list = ["輸入完成，開始計算", "澎湖縣 市區公車", "馬公-望安-七美 交通船", "結束程式運行"]
                            price = 400
                case 9:  # 城市9：臺東縣：臺東縣都市內 $299
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    name = TPASS_city[city]
                    trans_list = ["輸入完成，開始計算", "臺東縣 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                    price = 299
                case 10:  # 城市10：大嘉義生活圈：嘉義縣市跨城際 $399
                    print("\n您選擇了 {} 月票方案".format(TPASS_city[city]))  # 輸出「通勤生活圈」的提示訊息
                    name = TPASS_city[city]
                    trans_list = ["輸入完成，開始計算", "嘉義縣/市 市區公車", "臺灣鐵路", "公路客運", "結束程式運行"]
                    price = 399
                case 11:  # 城市11：返回上層選單
                    print("\033[38;5;43m正在返回「功能選擇平臺」\033[0m\n\a")  # 輸出提示訊息與通知聲音
                    return  # 回到「功能選擇平臺」
                case 12:  # 城市12：結束程式運行
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
        tp_metro_original = 0  # 另外保留 臺北捷運+環狀線 的原始花費，避免因重複輸入與計算常客優惠後出現總金額錯誤的問題

        # 使用無窮迴圈，直到用戶選擇「輸入完成」或「結束程式」才能離開迴圈
        while True:
            try:
                print("\n這裡是「交通選擇平臺」，請選擇您要搭乘的大眾運輸工具")  # 輸出「交通選擇平臺」的提示訊息
                print_list(trans_list)  # 呼叫列表印出函式，印出「交通選擇平臺」的選單列表
                trans = check_input("--> \033[0m", 0, len(trans_list) - 1)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至交通工具變數，依序傳入 詢問內容、最小數值、最大數值

                match trans_list[trans]:
                    case "輸入完成，開始計算":
                        print("\033[38;5;111m收到您的指示，正在計算金額與分析結果\033[0m\n")  # 輸出提示訊息
                        break  # 離開「交通選擇平臺」的無窮迴圈，開始計算金額並輸出建議結果
                    case "結束程式運行":
                        print("\n\033[38;5;197m收到您的要求，正在結束程序\033[0m\a\n")  # 輸出提示訊息與通知聲音
                        sys.exit(0)  # 呼叫系統正常結束本程式運行
                    case "臺北捷運+環狀線":  # 呼叫 臺北捷運+環狀線 專用輸入函式
                        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「臺北捷運+環狀線」\033[38;5;111m的搭乘數據\033[0m")  # 輸出「數據輸入平臺」的提示訊息
                        print("\033[38;5;208m如果程式詢問金額沒有本月對應的搭乘次數，請輸入半形數字 0\033[0m")

                        # 使用 for 迴圈依序詢問從 $20 到 $65 捷運票價對應的搭乘次數
                        for m in range(20, 70, 5):
                            times = check_input("請輸入您本月搭乘「臺北捷運+環狀線」NT${} 元的次數 ---> ".format(m), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
                            times_list[trans] += times
                            tp_metro_original += times * m

                        # 計算 臺北捷運+環狀線 的常客優惠價格後存入列表中對應位置，避免修改原始票價數值
                        # 由 Gemini Code Assist 提供建議，使用數學技巧進行四捨五入的計算，避免 math.round() 或 numpy.round() 的「銀行家捨入法」問題
                        if 11 <= times_list[trans] <= 20:
                            amount[trans] = int(tp_metro_original * 0.95 + 0.5)
                        elif 21 <= times_list[trans] <= 40:
                            amount[trans] = int(tp_metro_original * 0.9 + 0.5)
                        elif 41 <= times_list[trans]:
                            amount[trans] = int(tp_metro_original * 0.85 + 0.5)
                        else:
                            amount[trans] = tp_metro_original

                        print("\033[38;5;45m程式已成功記下您本月共搭乘「臺北捷運+環狀線」NT$ {:,}（{:,} 次），常客優惠後為 NT$ {:,}\033[0m"
                              .format(tp_metro_original, times_list[trans], amount[trans]))  # 輸出小結與回應訊息
                        print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息
                    case "大臺北地區 市區公車":  # 呼叫 大臺北地區 市區公車 專用輸入函式
                        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「大臺北地區 市區公車」\033[38;5;111m的搭乘數據\033[0m")  # 輸出「數據輸入平臺」的提示訊息
                        print("\033[38;5;208m如果程式詢問金額沒有本月對應的搭乘次數，請輸入半形數字 0\033[0m")
                        for m in bus_price:
                            times = check_input("請輸入您本月搭乘「大臺北地區 市區公車」NT${} 元的次數 ---> ".format(m), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
                            times_list[trans] += times
                            amount[trans] += times * m
                        print("\033[38;5;45m程式已成功記下您本月共搭乘「大臺北地區 市區公車」NT$ {:,}（{:,} 次）\033[0m".format(amount[trans], times_list[trans]))  # 輸出小結與回應訊息
                        print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息
                    case _:  # 呼叫 一般輸入函式
                        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「{}」\033[38;5;111m的搭乘數據\033[0m".format(trans_list[trans]))  # 輸出「數據輸入平臺」的提示訊息
                        print("\033[38;5;208m如果您已完成本交通工具的輸入，請輸入半形數字 0 以回到「交通選擇平臺」\033[0m")

                        # 使用無窮迴圈，直到用戶輸入 0 才能離開迴圈，回到「交通選擇平臺」
                        while True:
                            money = check_input("請問您想要輸入票價多少元的數據 --> ", 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至金額變數，依序傳入 詢問內容、最小數值
                            if money == 0:
                                print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息
                                break  # 離開「數據輸入平臺」的無窮迴圈，回到「交通選擇平臺」
                            times = check_input("請輸入您本月搭乘「{}」NT${} 元的次數 ---> ".format(trans_list[trans], money), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
                            if times == 0:
                                print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息
                                break  # 離開「數據輸入平臺」的無窮迴圈，回到「交通選擇平臺」
                            times_list[trans] += times
                            amount[trans] += times * money

                        print("\033[38;5;45m程式已成功記下您本月搭乘「{}」NT$ {:,}（{:,} 次）\033[0m".format(trans_list[trans], amount[trans], times_list[trans]))  # 輸出小結與回應訊息

            except RangeError:  # 如果使用者輸入超出正常範圍的內容
                print("\033[38;5;197m您的輸入內容超出合理範圍，請檢查後輸入正確內容，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「交通選擇平臺」
            except ValueError:  # 如果使用者輸入無法轉換成整數的內容
                print("\033[38;5;197m您的輸入內容出現非整數的錯誤，請檢查後輸入正確選項，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「交通選擇平臺」
            except Exception:  # 例外處理，捕捉其他未預期的錯誤
                print("\033[38;5;197m您的輸入內容出現其他錯誤，請檢查後輸入正確選項，現正返回「交通選擇平臺」\033[0m\a\n")  # 輸出提示訊息與通知聲音，讓使用者重新輸入
                continue  # 回到「交通選擇平臺」

        # 直接將 calculate() 的邏輯接在這裡？使用參數 trans_list(list) price(int)
        total, result = 0, "本月共搭乘「{}」的：\n\t".format(TPASS_city[city])
        for m in amount:
            total += m

        if total:  # 如果總票價不為 0
            # 儲存各個交通工具詳細的搭乘次數與個別總和  # TODO 如果 amount[t]==0 時，則跳過不印出  # TODO more Pythonic?
            for t in range(1, len(trans_list) - 1):
                if t==len(trans_list) - 2:  # 如果是列表中的最後一項
                    result += "{}：{:,} 次，共 {:,} 元".format(trans_list[t], times_list[t], amount[t])  # 印出 名稱、次數、金額
                else:
                    result += "{}：{:,} 次，共 {:,} 元、".format(trans_list[t], times_list[t], amount[t])  # 印出 名稱、次數、金額，以頓號分隔元素

            # 比較通勤花費與月票金額，判斷是否建議購買 TPASS 通勤月票與最終花費後儲存在字串中，以供後續 CLI 輸出與檔案儲存使用
            if total < price:
                result += "\n本月無須另外購買「{}」方案的 TPASS 通勤月票，共計花費 {:,} 元".format(name, total)
            elif total == price:
                result += "\n本月無論是否購買「{}」方案的 TPASS 通勤月票，皆要花費 {:,} 元".format(name, price)
            elif total > price:
                result += "\n建議本月購買「{}」方案的 TPASS 通勤月票，可省下 {:,} 元".format(name, total - price)
        else:
            result = "本月沒有搭乘任何大眾運輸交通工具，不需要進行計算與分析"

        print("\033[38;5;45m{}\033[0m".format(result))  # 在 CLI 中印出最終的分析結果，包含各交通工具搭乘數據與購買建議


        # 直接將 output() 的邏輯接在這裡？
        # 嘗試開啟 TPASS_Result.txt 為 file 句柄後，將 時間戳記、計算結果、程式版本、分隔符號 寫入檔案中，方便使用者日後查詢
        try:
            # 由 Gemini Code Assist 提供可以在時間戳記的缺位中自動補 0 的方法
            # TODO: 改為將最新結果寫在檔案開頭，但不覆蓋原有資料與字元
            with open("TPASS_Result.txt", "a+", encoding="UTF-8") as file:
                stamp = time.localtime()
                file.write("{:04d}-{:02d}-{:02d} {:02d}:{:02d}\n".format(stamp.tm_year, stamp.tm_mon, stamp.tm_mday, stamp.tm_hour, stamp.tm_min))
                file.write("{}\n".format(result))
                file.write("「{}」Ver{}\n".format(program, ver))
                file.write("{}\n".format("=" * 36))
        # TODO 增加磁碟空間已滿，無法寫入的專用 except 提示
        except PermissionError:  # 如果文件系統的存取權限不足
            print("\033[38;5;197m因為程式對於文件系統的存取權限不足，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案權限不足訊息與通知聲音
        except Exception:
            print("\033[38;5;197m程式遇到不明原因的錯誤，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案無法寫入訊息與通知聲音
        else:
            print("\033[38;5;47m成功將計算結果寫入至 \"TPASS_Result.txt\"，可於日後開啟該檔案檢視結果\033[0m")  # 輸出檔案成功寫入訊息
        finally:
            print("\033[38;5;43m正在返回「都會選擇平臺」\033[0m\n\a")  # 輸出提示訊息與通知聲音


analyze_manual = ("\033[38;5;208m\n「計算分析函式」使用說明\n"
                  "都會選擇平臺：選擇您想要分析的通勤生活圈並輸入對應的半形數字\t0 顯示本則使用說明\t11 返回「功能選擇平臺」選單\t12 結束運行並退出程式\n"
                  "方案選擇平臺：在該通勤生活圈依據想要分析的月票方案輸入對應的半形數字\n"
                  "交通選擇平臺：依據想要搭乘的大眾運輸交通工具輸入對應的半形數字\t0 查看最終的計算結果\n"
                  "數據輸入平台：在此使用半形數字輸入該交通工具搭乘的票價與次數，程式會依照您的數據進行結果分析與購買推薦\n\033[0m")