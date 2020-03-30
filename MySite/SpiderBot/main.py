from multiprocessing import Process
from scrapy import cmdline
import argparse
import sys
import time

def Job(frequence):
    Args = ["scrapy", "crawl", 'NBANews']
    while True:
        p = Process(target=cmdline.execute, args=(Args,))
        p.start()
        p.join()
        print('完成爬蟲')
        print(f'等待: {frequence} 秒')
        time.sleep(int(frequence))

if __name__ == '__main__':
    Parser = argparse.ArgumentParser(description='啟動爬蟲')
    Parser.add_argument('--freq', help='定時爬蟲的時間間隔(秒) ex: --freq 10')
    Args = Parser.parse_args()
    if Args.freq == None:
        print('請輸入定時器的時間間隔(秒)')
        sys.exit(0)

    process = Process(target=Job, args=(Args.freq,))
    process.start()