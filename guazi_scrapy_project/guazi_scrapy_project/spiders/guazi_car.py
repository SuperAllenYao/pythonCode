# -*- coding: utf-8 -*-
import scrapy
from guazi_scrapy_project.guazi_scrapy_project.mongo_db import mongo
import re
from guazi_scrapy_project.guazi_scrapy_project.items import GuaziScrapyProjectItem


class GuaziCarSpider(scrapy.Spider):
    name = 'guazi_car'
    allowed_domains = ['guazi.com']

    # 新方法
    def start_requests(self):
        while True:
            task = mongo.get_task('guazi_task')
            # task取空了就停下来
            if not task:
                break
            if '_id' in task:
                task.pop('_id')
            if task['item_type'] == 'list_item':
                # 这个request对象代表了一个http的请求
                # 会经由downloader去执行，从而产生一个response
                yield scrapy.Request(
                    # 发送请求的url
                    url=task['task_url'],
                    dont_filter=True,
                    callback=self.handle_car_item,
                    errback=self.handle_err,
                    meta=task
                    # method='GET',
                    # headers= 请求头信息
                    # body= 请求体
                    # cookies= 要携带的cookie信息
                    # meta= 是字典的格式，向其他方法里面传递信息
                    # encoding='utf-8'字符编码
                    # priority=0 请求的优先级
                    # errback= 当程序处理请求返回有错误的时候，使用这个参数
                )
                # 用于发送POST表单请求所使用的方法
                # yield scrapy.FormRequest()
            elif task['item_type'] == 'car_info_item':
                yield scrapy.Request(url=task['car_url'],
                                     callback=self.handle_car_info,
                                     dont_filter=True,
                                     meta=task,
                                     errback=self.handle_err)

    # 报错回调方法
    def handle_err(self, failure):
        # failure.request.meta,来获取失败的task
        # 把失败的请求扔回task
        mongo.save_task('guazi_task', failure.request.meta)

    # 自定义的解析方法
    def handle_car_item(self, response):
        if "中为您找到0辆好车" in response.text:
            return
        car_item_list = response.xpath(
            "//ul[@class='carlist clearfix js-top']/li")
        for car_item in car_item_list:
            # 创建一个字段用于存储二手车的名称和详情页的url
            car_list_info = {}
            # 在scrapy框架中使用xpath语句返回的是一个列表，可使用extract_first方法获取索引为0的值
            car_list_info['car_name'] = car_item.xpath(
                "./a/h2/text()").extract_first()
            car_list_info[
                'car_url'] = "https://www.guazi.com" + car_item.xpath(
                    "./a/@href").extract_first()
            car_list_info['item_type'] = 'car_info_item'
            yield scrapy.Request(url=car_list_info['car_url'],
                                 callback=self.handle_car_info,
                                 dont_filter=True,
                                 meta=car_list_info,
                                 errback=self.handle_err)
        # 写到for循环的外面去
        if response.xpath(
                "//ul[@class='pageLink clearfix']/li[last()]/a/span/text()"
        ).extract_first() == "下一页":
            value_search = re.compile(
                r"https://www.guazi.com/(.*?)/(.*?)/o(\d+)i7")
            # 返回的是列表，列表里面包含的是数组
            value = value_search.findall(response.url)[0]
            # 下一页的链接
            response.request.meta[
                'task_url'] = "https://www.guazi.com/%s/%s/o%si7" % (
                    value[0], value[1], str(int(value[2]) + 1))
            yield scrapy.Request(url=response.request.meta['task_url'],
                                 callback=self.handle_car_item,
                                 meta=response.request.meta,
                                 dont_filter=True,
                                 errback=self.handle_err)

    # 解析二手车详情页
    def handle_car_info(self, response):
        # 获取到列表里面的二手车名称，以及二手车的url
        # 通过车源号进行去重，通过正则表达式，车源号：HC-73829610
        car_id_search = re.compile(r"车源号：(.*?)\s+")
        # 创建items内部定义的字段的实例
        car_info = GuaziScrapyProjectItem()
        # car_id
        car_info['car_id'] = car_id_search.search(response.text).group(1)
        # 通过meta传递过来的car_name
        car_info['car_name'] = response.request.meta['car_name']
        # # 从哪个链接抓取过来的数据
        car_info['from_url'] = response.request.meta['car_url']
        car_info['car_price'] = response.xpath(
            "//span[@class='pricestype']/text()").extract_first().strip()
        car_info['license_time'] = response.xpath(
            "//ul[@class='assort clearfix']/li[@class='one']/span/text()"
        ).extract_first().strip()
        # 表显里程
        car_info['km_info'] = response.xpath(
            "//ul[@class='assort clearfix']/li[@class='two']/span/text()"
        ).extract_first().strip()
        # 上牌地
        liencse_location = response.xpath(
            "//ul[@class='assort clearfix']/li[@class='three']/span/text()"
        ).extract()[0].strip()

        try:
            # 排量信息
            car_info['desplacement_info'] = response.xpath(
                "//ul[@class='assort clearfix']/li[@class='three']/span/text()"
            ).extract()[1].strip()
        except:
            car_info['desplacement_info'] = '无'
        # 变速箱，手动挡还是自动挡
        car_info['transmission_case'] = response.xpath(
            "//ul[@class='assort clearfix']/li[@class='last']/span/text()"
        ).extract_first().strip()
        yield car_info
