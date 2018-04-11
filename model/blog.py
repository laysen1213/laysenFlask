from database.mysql import *

def blogList(search = ''):
	sql = 'select a.*,b.name from pt_blog a LEFT JOIN pt_blog_cate b on a.cid = b.id where a.status = 1 '
	if(search):
		sql += 'and a.title like "%'+search+'%" '
	sql += 'limit 8'
	res = db_sql(sql)
	return res

def tjList():
	sql = 'select * from pt_blog where status = 1 and is_recommend = 1 limit 8'
	res = db_sql(sql)
	return res

def blogInfo(_id):
	sql = 'select a.*,b.name from pt_blog a LEFT JOIN pt_blog_cate b on a.cid = b.id where a.status = 1 and a.id = ' + str(_id) + ' limit 1'
	res = db_sql(sql)
	return res[0]