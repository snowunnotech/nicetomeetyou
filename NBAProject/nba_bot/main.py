import argparse
import time
import sys
from multiprocessing import Process
from scrapy import cmdline


def start_job(job_name, frequency):
    args = ["scrapy", "crawl", job_name, "--nolog"]
    num = 1
    while True:
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        print(f"Round: {num}, Spend: {time.time() - start:.2f}/sec")
        print(f"Sleep: {frequency}/sec")
        time.sleep(int(frequency))
        num += 1

if __name__ == '__main__':
    # 獲取參數
    parser = argparse.ArgumentParser(description='Code for start Scrapy.')
    parser.add_argument('--job', help='Please input the job name. ex: --job nba', default='')
    parser.add_argument('--freq', help='Please input the interval for job.(Unit of seconds) ex: --freq 10', default='')
    args = parser.parse_args()
    
    # 判斷參數不足結束程式
    if args.job=="" or args.freq=="":
        if args.job=="":
            print("Please input the job name. ex: --job nba")
        if args.freq=="":
            print("Please input the interval for job.(Unit of seconds) ex: --freq 10")
        sys.exit(0)
    
    print("start job:", args.job)
    process = Process(target=start_job, args=(args.job, args.freq))
    process.start()