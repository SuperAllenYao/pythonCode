# -*- coding: utf-8 -*-
import scrapy


class GuaziCarSpider(scrapy.Spider):
	name = 'guazi_car'
	allowed_domains = ['guazi.com']

	# start_urls = ['http://guazi.com/']

	# 新方法
	def start_requests(self):
		pass

	def parse(self, response):
		pass
