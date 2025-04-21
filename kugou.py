# 爬取酷狗音乐top前500的歌曲
# 要求:爬取歌曲排名,歌曲名,歌手名,歌曲时长
from time import sleep
import requests as re
from bs4 import BeautifulSoup
import pandas as pd

# 请求头伪装
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

dict_list=[]
# 定义获取信息的函数
def get_info(url):
    # 请求url
    res = re.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    ranks = soup.select('span.pc_temp_num')      # 获取排名
    titles = soup.select('a.pc_temp_songname')      #获取歌曲名and歌手名
    times = soup.select('span.pc_temp_time')        #获取歌曲时长
    for rank,title,time in zip(ranks,titles,times):
        data = {
            # 取出文本内容
            'rank' : rank.get_text().strip(),
            'singer' : title.get_text().split('-')[1].strip(),
            'music' : title.get_text().split('-')[0].strip(),
            'time' : time.get_text().strip()
        }
        dict_list.append(data)
    # print(f'第{i}页')

# 主函数
if __name__ == "__main__" :
    # http://www.kugou.com/yy/rank/home/1-8888.html
    for i in range(1,24):
        url = f'http://www.kugou.com/yy/rank/home/{i}-8888.html'
        get_info(url)
        print(f"第{i}页")
        # 程序停止三秒再继续爬取以防访问频率过高
        sleep(3)
    # 使用pandas库对数据进行合并成表格形式
    df = pd.DataFrame(dict_list)
    print(df)
    df.to_csv('Top500.csv',index=False)





















