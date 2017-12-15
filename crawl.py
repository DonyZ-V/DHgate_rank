import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import os


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'authority': 'www.dhgate.com',
        'cookie': '__cfduid=da097958450ecb4fdca3dc6c79ed938001513151118; vid=rBUUxFow2o55LCd3A8iEAg==; yjs_id=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYxLjAuMzE2My4xMDAgU2FmYXJpLzUzNy4zNnx3d3cuZGhnYXRlLmNvbXwxNTEzMTUxMTI4NDkwfA; B2BCookie=09b28651-5400-421e-8412-9f4f0a153190; __sonar=17580002178263456593; b2b_cart_sid=f0a186af-6a2d-4d44-a575-4a4f8dfdb47f; suship=CN; b_u_cc=ucc=CN; searchinfo=pagesize%3D24%3Bviewtype%3D1%3B; _pk_ref..c028=%5B%22%22%2C%22%22%2C1513171386%2C%22https%3A%2F%2Factivity.dhgate.com%2Fcoupons.html%22%5D; session=U1bvmU6zugeSBV1K5MPHIg; ctrl_time=1; __utmt=1; __utma=251624089.1306435726.1513151129.1513176814.1513242064.5; __utmb=251624089.1.10.1513242064; __utmc=251624089; __utmz=251624089.1513242064.5.5.utmcsr=dhgate.com|utmccn=(referral)|utmcmd=referral|utmcct=/w/x96%20mini/1.html; intl_locale=en; JSESSIONID=14y50iiquyn811wma16wvwgu0g; language=en; nTalk_CACHE_DATA={uid:dh_1000_ISME9754_guestTEMP4AD3-D634-46,tid:1513171079245594}; NTKF_T2D_CLIENTID=guestTEMP4AD3-D634-468C-8D8D-4EDB74C02E9A; pvn=28; lastvisittime=1513242064536; vnum=1; b2b_ip_country=CN; _uetsid=_uet34036095; gaVisitorEmail=; gaVisitorId=; _pk_ref..fe71=%5B%22%22%2C%22%22%2C1513242069%2C%22https%3A%2F%2Fwww.dhgate.com%2Fw%2Fx96%2Bmini%2F1.html%22%5D; _pk_ses..fe71=*'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return '未找到商品'
    except RequestException:
        return '请求错误'


def parse_one_page(html):
    ranks = {}

    doc = pq(html)
    page = doc('#MainContent > div > div.page > span > b').text()
    company_name = doc('div.secattr > ul > li.pro-seller > span.seller > a').text().split(' ')
    # return company_name
    if page:
        ranks[page] = company_name
    return ranks

def check_rank(ranks):
    company = 'flysharkteam'
    for k in ranks:
        print(ranks[k])
        for x in ranks[k]:
            if x == company:
                r = ranks[k].index(x) + 1
                return (k, r)

