"""
Trans.py
此模組提供 Fucn.py 中，大眾交通運輸工具所需的類別定義與實作（由 Gemini Code Assist 提供相關建議，符合 DRY 原則）
"""


if __name__ == "__main__":  # 如果使用者誤啟動本程式
    print("\033[38;5;197m這是 Func.py 呼叫的類別模組\n請改為運行 Main.py，而非直接運行本程式\n我們即將結束此模組的運行\033[0m")  # 輸出提示訊息提醒使用者正確使用方式
    exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"


class Transportation():
    # TODO: 所有交通工具的總類
    # TODO: 依據傳入名稱設定交通工具名稱
    # TODO: 初始化時若傳入 最小/最大 值，則「數據輸入平臺」依據傳入值檢查，否則以 0~1000 為預設檢查範圍
    def __init__(self, name, range_min=0, range_max=1000):
        self.name = name
        self.range_min = range_min
        self.range_max = range_max

    # TODO: 實作通用的「有檢查的數據輸入平臺」邏輯

    # TODO: 實作「通用」的計算總金額邏輯


class TaipeiMetro(Transportation):
    # TODO: 使用名稱 "臺北捷運+環狀線" 進行初始化
    def __init__(self):
        super().__init__("臺北捷運+環狀線")

    # TODO: 使用多態方式替代父類的「數據輸入平臺」邏輯

    # TODO: 實作「常客回饋方案」的計算總金額邏輯


class TaipeiBus(Transportation):
    # TODO: 使用名稱 "大臺北地區 市區公車" 進行初始化
    def __init__(self):
        super().__init__("大臺北地區 市區公車")

    # TODO: 使用多態方式替代父類的「數據輸入平臺」邏輯


class TaiwanRailway(Transportation):
    # TODO: 傳入名稱 "臺灣鐵路（含 彰化/嘉義 跨區 7 站）" 時，使用傳入名稱，否則預設為 "臺灣鐵路"
    def __init__(self, name="臺灣鐵路"):
        super().__init__(name)

    # TODO: 使用父類的「有檢查的數據輸入平臺」邏輯

    # TODO: 實作「常客回饋方案」的計算總金額邏輯