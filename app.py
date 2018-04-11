from flask import Flask,url_for,request,render_template,redirect,flash,session,jsonify
from model.blog import blogList,tjList,blogInfo
from base.fun import timeDate

app = Flask(__name__)

# config
app.secret_key = 'my precious'
h = 'http://m.91laysen.cn'

# 首页
@app.route("/")
def index():
	blog = blogList()
	for k,v in enumerate(blog):
		blog[k]['ctime'] = timeDate(v['ctime'])
	url_for('static', filename='*')
	return render_template('index.html',blog=blog,h=h,nav=1)

# 列表页
@app.route("/blog")
def blog():
	search = request.args.get('search')
	if not search:
		search = ''
	blog = blogList(search)
	for k,v in enumerate(blog):
		blog[k]['ctime'] = timeDate(v['ctime'])

	tj = tjList()
	for k,v in enumerate(tj):
		tj[k]['ctime'] = timeDate(v['ctime'])
	return render_template('blog.html',blog=blog,tj=tj,h=h,nav=2,search=search)

# 详情页
@app.route("/detail")
def detail():
	_id = request.args.get('id')
	info = blogInfo(_id)
	tj = tjList()
	for k,v in enumerate(tj):
		tj[k]['ctime'] = timeDate(v['ctime'])
	info['ctime'] = timeDate(info['ctime'])
	return render_template('detail.html',info=info,tj=tj,h=h,nav=2)

if __name__ == '__main__':
	#调试模式
	app.debug = False
	app.run()