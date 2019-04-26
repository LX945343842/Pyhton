from urllib import request
from lxml import etree
from . import models


# 获取数据
def get_data():
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(25 * i)
        html=request.urlopen(url).read().decode('utf-8')
        html = etree.HTML(html)
        datas = html.xpath('//ol[@class="grid_view"]/li')

        for data in datas:
            movieName = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')[0]
            info = data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
            movieDirectors = str(info[0].strip())
            movieScore = data.xpath('div/div[2]/div[@class="bd"]/div/span[@class="rating_num"]/text()')[0]
            movieQuote = data.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')[0]
            movie = models.movieinfo()
            movie.mName = movieName
            movie.mDirectors = movieDirectors
            movie.mScore = movieScore
            if movieQuote:
                movie.mQuote = movieQuote
            movie.save()







