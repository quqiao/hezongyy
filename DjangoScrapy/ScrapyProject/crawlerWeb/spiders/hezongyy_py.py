# -*- coding: utf-8 -*-
import scrapy
from crawlerWeb.items import CrawlerwebItem

class hezongyy_py(scrapy.Spider):
  name='hezongyy_py'
  allowed_domains = ['hezongyy.com']
  #1. 登录页面
  start_urls = ['https://www.hezongyy.com/puyao.html']
  def parse(self, response):
    #2. 代码登录
    login_url = 'https://www.hezongyy.com/auth/login'
    formdata={
      "username": "测试06",
      "pwd": "123456"
    }
    #3. 发送登录请求post
    yield scrapy.FormRequest.from_response(
      response,
      formxpath="//*[@id='right_1']/a",
      formdata=formdata,
      method="POST", #覆盖之前的get请求
      callback=self.parse_login
    )

  def parse_login(self, response):
    #4.访问目标页面
    member_url = "https://www.hezongyy.com/"
    yield scrapy.Request(member_url, callback=self.parse_member)

  def parse_member(self, response):
    with open("puyao.html", 'wb') as f:
      f.write(response.body)
      item = CrawlerwebItem()
      # quotes = response.xpath('//*[@id="datu"]/div/ul')
      for i in range(1, 41):
          name = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-mingzi::text' % i).extract_first()
          cj = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-compamy::text' % i).extract_first()
          gg = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-guige > span::text' % i).extract()
          xq = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-xiaoqi > span:nth-child(1)::text' % i).extract()
          price = response.css('#datu > div > ul > li:nth-child(%d) > div.datu-jiage::text' % i).extract()
          item['name'] = name
          item['compony'] = cj
          item['gg'] = gg
          item['xq'] = xq
          item['price'] = price
          yield item
      # next = response.css('.pager .next a::attr(href)').extract_first()
      # url = response.urljoin(next)
      # yield scrapy.Request(url=url, callback=self.parse)


