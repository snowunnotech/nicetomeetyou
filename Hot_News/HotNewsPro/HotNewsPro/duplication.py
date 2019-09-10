# 使用自定義去重時，要先去 setting 那邊設定
    # DUPEFILTER_CLASS = "scy.duplication.RepeatFilter"   #設定連結自己 自定義的 去重方式
    #  變數名固定不可變 = scy下 的 duplication檔案 的 RepeatFilter 函式

#  創建自定義的檔案名字可以自己定義
#  裡面的涵式方法名固定，不可變更
#  記錄方式可以改成數據庫，或者 緩存  也可以
    #PS .  from scrapy.dupefilters import RFPDupeFilter  #去重方式在裡面，參考裡面的方式，自己去寫一個自定義的去重
from scrapy.dupefilters import RFPDupeFilter
class RepeatFilter(object):   #名字可以自己定義

# 下面 五個函數的名字固定，不可變動
#執行時，順序為
    # from_settings    先創建對象
    # __init__         執行init
    # open             開始爬
    # request_seen     不斷訪問，檢查是否訪問過
    # close            結束爬
        # log              log無順序  一直都在記錄

    def __init__(self,conn_str):
        self.visited_set = set()    # 存放 已去過的URL
        self.conn_str = conn_str   # 這裡就儲存 連接位置
        self.conn = None           # 存放 資料庫連接
        self.cursor = None

    @classmethod
    def from_settings(cls, settings):     # 這個函數負責創建對象
        conn_str = settings.get('DB')  # 會去 setting那邊尋找 DB的資料庫設定，儲存方式，這個DB必須大寫
        return cls(conn_str)  # 創建對象，傳入 儲存位置

    def request_seen(self, request):
        # print("這是當前訪問的URL=",request.url)   #這是當前訪問的URL

        # self.cursor.execute("select * from hotnews where url=request.url;")
        # if request.url in self.visited_set:     # 判斷當前訪問RUL 是否已經存在 訪問過的集合內
        #     return True
        # else:
        #     print(request.url)  # 這是當前訪問的URL
        #     self.visited_set.add(request.url)   # 如果還沒存在，則先加入清單
        #     return False
        pass

    def open(self):  # can return deferred
        # print("open==")   #這是當前訪問的URL

        # self.conn = sqlite3.connect('test.db')      # 打開資料庫
        # self.cursor = conn.cursor()
        pass
    def close(self, reason):  # can return a deferred
        # self.cursor.close()
        # self.conn.close()             # 關閉資料庫
        pass
    def log(self, request, spider):  # log that a request has been filtered
        pass