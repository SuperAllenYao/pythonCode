import pymongo


class HandleMongoDB(object):
	def __init__(self):
		client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
		self.db = client['db_guazi']

	# 存储task逻辑
	def save_task(self, collection_name, task):
		print('当前存储的task为：%s' % task)
		collection = self.db[collection_name]
		task = dict(task)
		collection.insert_one(task)

	def get_task(self, collection_name):
		collection = self.db[collection_name]
		# 找到一个task并删除，取出的task不重复
		task = collection.find_one_and_delete({})
		return task


mongo = HandleMongoDB()
