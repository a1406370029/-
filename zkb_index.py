import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Server import *
def main():
    dt = ''
    # # 页面范围1—5，但是只提取第一页的信息
    # add = '&page=' + str(1)
    # html = requests.get('https://www.52pojie.cn/forum.php?mod=guide&view=hot'+add)
    Headers = {
            'Cookie': '_uab_collina=163097711814240481079388; ki1e_2132_connect_is_bind=1; ki1e_2132_connect_uin=66BB3D6D4AFEB40B3B9CB8A7E2181F4C; ki1e_2132_smile=1D1; __gads=ID=f8c68eb1dc8baae9-221e3f6b8ccb00ec:T=1630983370:RT=1630983370:S=ALNI_MaQtK1_wKhONTNnuvyAbeajG_qNjw; UM_distinctid=17bdd5fa8a71d8-0c9b1de0d9ec3e-3e604809-144000-17bdd5fa8a891e; ki1e_2132_client_token=66BB3D6D4AFEB40B3B9CB8A7E2181F4C; ki1e_2132_connect_login=1; ki1e_2132_atlist=730672%2C1024007; ki1e_2132_saltkey=FQxF3F00; ki1e_2132_lastvisit=1638749968; ki1e_2132_client_created=1638753607; ki1e_2132_auth=c668taqoemnSVBfHiJFmaTnGGa4VF7Pgf1zYVrB2p%2Bb4a4qtCTNA9WSDLONTnvpXTIfcYrsDPoQphXn6ODhqJHSSuWU; ki1e_2132_pc_size_c=0; ki1e_2132_atarget=1; ki1e_2132_connect_last_report_time=2021-12-09; timestamp=1639053159000; sign=DB5786478B0A95834A3F63DA6B7EAA9C; ki1e_2132_ulastactivity=1639059590%7C0; CNZZDATA1280316138=1829848941-1631505333-%7C1639055912; ki1e_2132_forum_lastvisit=D_11_1634349507D_31_1638782071D_15_1639059597; ki1e_2132_viewid=tid_8433356; ki1e_2132_lastcheckfeed=394035%7C1639060165; ki1e_2132_checkfollow=1; ki1e_2132_checkpm=1; ki1e_2132_sendmail=1; ki1e_2132_lastact=1639060165%09connect.php%09check',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'www.zuanke8.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept-Language': 'zh-cn'
        }
    html = requests.get('http://www.zuanke8.com/zuixin.php',headers=Headers)
    sever = 'http://www.zuanke8.com/'
    soup = BeautifulSoup(html.text, 'html.parser')
    # geta = soup.find_all('a', class_='xst')   
    geta = soup.find_all('a') 
    geta2 = []
    for i in range(len(geta)):
        if '赚客大家谈' in str(geta[i]):
            geta2.append(geta[i + 1])
    
    # 返回信息封装组合
    count = 1
    for x in geta2:
        # dt = dt + str(count) +'. ##### ['+x.string+']('+sever+x.get('href')+')\n'
        dt = dt + str(count) + '. ##### ['+x.string+']('+x.get('href')+')\n'
        count = count + 1
    # 微信推送信息
    se = Server()
    se.push(dt)
if __name__ == "__main__":
    main()
main()
