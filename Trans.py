"""
Trans.py
此模組提供 Fucn.py 中，大眾交通運輸工具所需的類別定義與實作（由 Gemini Code Assist 提供相關建議，符合 DRY 原則）
"""

from Util import *


if __name__ == "__main__":  # 如果使用者誤啟動本程式
    print("\033[38;5;197m這是 Func.py 呼叫的交通類別模組\n請依照 README.md 的指示改為運行 Main.py，而非直接運行本程式\n我們即將結束此模組的運行\033[0m")  # 輸出提示訊息提醒使用者正確使用方式
    exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"


class Transportation():
    # TODO: 所有交通工具的總類，依據傳入名稱設定交通工具名稱
    # TODO: 初始化時若傳入 最小/最大 值，則「數據輸入平臺」依據傳入值檢查，否則以 0~1000 為預設檢查範圍
    def __init__(self, name, range_min=0, range_max=1000):
        self.__name = name
        self.__range_min = range_min
        self.__range_max = range_max
        self.__times = self.__orignal = self.__total = 0

    def name(self):
        return self.__name

    def query(self):
        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「{}」\033[38;5;111m的搭乘數據\033[0m".format(self.__name))  # 輸出「數據輸入平臺」的提示訊息
        print("\033[38;5;208m如果您已完成本交通工具的輸入，請輸入半形數字 0 以回到「交通選擇平臺」\033[0m")
        # 使用無窮迴圈，直到用戶輸入 0 才能離開迴圈，回到「交通選擇平臺」
        while True:
            money = check_input("請問您想要輸入票價多少元的數據 --> ", self.__range_min, self.__range_max)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至金額變數，依序傳入 詢問內容、最小數值、最大數值
            if money == 0:
                break  # 離開「數據輸入平臺」的無窮迴圈，準備回到「交通選擇平臺」
            times = check_input("請輸入您本月搭乘「{}」NT${} 元的次數 ---> ".format(self.__name, money), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
            if times == 0:
                break  # 離開「數據輸入平臺」的無窮迴圈，準備回到「交通選擇平臺」
            self.__times += times
            self.__orignal += times * money
        self._respond()

    def _respond(self):
        print("\033[38;5;45m程式已成功記下您本月共搭乘「{}」NT$ {:,}（{:,} 次）\033[0m".format(self.__name, self.__orignal, self.__times))  # 輸出小結與回應訊息
        print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息

    def calculate(self):
        self.__total = self.__orignal
        return self.__times, self.__total


class TaipeiMetro(Transportation):
    def __init__(self):
        super().__init__("臺北捷運+環狀線")

    # 使用多態方式替代父類的「數據輸入平臺」邏輯
    def query(self):
        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「臺北捷運+環狀線」\033[38;5;111m的搭乘數據\033[0m")  # 輸出「數據輸入平臺」的提示訊息
        print("\033[38;5;208m如果程式詢問金額沒有本月對應的搭乘次數，請輸入半形數字 0\033[0m")

        # 使用 for 迴圈依序詢問從 $20 到 $65 捷運票價對應的搭乘次數
        for m in range(20, 70, 5):
            times = check_input("請輸入您本月搭乘「臺北捷運+環狀線」NT${} 元的次數 ---> ".format(m), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
            self.__times += times
            self.__orignal += times * m

        # 計算 臺北捷運+環狀線 的常客優惠價格後存入總金額位置，避免修改原始票價數值
        # 由 Gemini Code Assist 提供建議，使用數學技巧進行四捨五入的計算，避免 math.round() 或 numpy.round() 的「銀行家捨入法」問題
        if 11 <= self.__times <= 20:
            self.__total = int(self.__orignal * 0.95 + 0.5)
        elif 21 <= self.__times <= 40:
            self.__total = int(self.__orignal * 0.9 + 0.5)
        elif 41 <= self.__times:
            self.__total = int(self.__orignal * 0.85 + 0.5)
        else:
            self.__total = self.__orignal

        print("\033[38;5;45m程式已成功記下您本月共搭乘「臺北捷運+環狀線」NT$ {:,}（{:,} 次），常客優惠後為 NT$ {:,}\033[0m".format(self.__orignal, self.__times, self.__total))  # 輸出小結與回應訊息
        print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息

    def calculate(self):
        return self.__times, self.__total


class TaipeiBus(Transportation):
    def __init__(self, price):
        super().__init__("大臺北地區 市區公車")
        self.__price = price

    # TODO: 使用多態方式替代父類的「數據輸入平臺」邏輯
    def query(self):
        print("\033[38;5;111m這裡是「數據輸入平臺」，請輸入您本月\033[38;5;43m「大臺北地區 市區公車」\033[38;5;111m的搭乘數據\033[0m")  # 輸出「數據輸入平臺」的提示訊息
        print("\033[38;5;208m如果程式詢問金額沒有本月對應的搭乘次數，請輸入半形數字 0\033[0m")
        for m in self.__price:
            times = check_input("請輸入您本月搭乘「大臺北地區 市區公車」NT${} 元的次數 ---> ".format(m), 0)  # 呼叫 check_input() 函數讀取與檢查使用者輸入後存放至次數變數，依序傳入 詢問內容、最小數值
            self.__times += times
            self.__orignal += times * m
        super()._respond()


class TaiwanRailway(Transportation):
    # TODO: 傳入名稱 "臺灣鐵路（含 彰化/嘉義 跨區 7 站）" 時，使用傳入名稱，否則預設為 "臺灣鐵路"
    def __init__(self, name="臺灣鐵路"):
        super().__init__(name)

    # TODO: 使用父類的「有檢查的數據輸入平臺」邏輯，實作「常客回饋方案」的計算總金額邏輯
    def query(self):
        super().query()
        # 計算 臺灣鐵路 的常客優惠價格後存入總金額位置，避免修改原始票價數值
        # 由 Gemini Code Assist 提供建議，使用數學技巧進行四捨五入的計算，避免 math.round() 或 numpy.round() 的「銀行家捨入法」問題
        if 11 <= self.__times <= 20:
            self.__total = int(self.__orignal * 0.9 + 0.5)
        elif 21 <= self.__times <= 40:
            self.__total = int(self.__orignal * 0.85 + 0.5)
        elif 41 <= self.__times:
            self.__total = int(self.__orignal * 0.8 + 0.5)
        else:
            self.__total = self.__orignal
        print("\033[38;5;45m程式已成功記下您本月共搭乘「{}」NT$ {:,}（{:,} 次），常客優惠後為 NT$ {:,}\033[0m".format(self.__name, self.__orignal, self.__times, self.__total))  # 輸出小結與回應訊息
        print("\033[38;5;43m正在返回「交通選擇平臺」\033[0m\n")  # 輸出提示訊息

    def calculate(self):
        return self.__times, self.__total
