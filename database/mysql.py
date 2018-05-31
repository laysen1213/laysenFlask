#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
class MysqlHelper:
    def db_conn(ref):
        return pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'ngwse9d2FH12412fsFd',
            db = 'laysen',
            charset = 'utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    # 查询单条数据
    def db_fetch_info(ref,sql):
        db = ref.db_conn()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
        except:
            row = False
        cursor.close()
        db.close()
        return row

    # 查询所有数据
    def db_fetch_all(ref,sql):
        db = ref.db_conn()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            result = False
        cursor.close()
        db.close()
        return result

    # 修改数据
    def db_update(ref,sql):
        db = ref.db_conn()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            res = True
        except:
            db.rollback()
            res = False
        cursor.close()
        db.close()
        return res

    def set_fun(ref,params):
        _fields = ''
        for i,k in enumerate(params):
            if i == 0:
                _fields += k + ' = "' + str(params[k]) + '"'
            else:
                _fields += ',' + k + ' = "' + str(params[k]) + '"'
        return _fields

    def params_fun(ref,params):
        _fields = ''
        _values = ''
        for i,k in enumerate(params):
            if i == 0:
                _fields += k
                _values += '"'+str(params[k])+'"'
            else:
                _fields +=  ',' + k
                _values += ',"' + str(params[k]) + '"'
        return {"fields":_fields , "values":_values}

    def where_fun(ref,where):
        _where = ''
        for i,k in enumerate(where):
            if i == 0:
                _where += ' where ' + k + ' = "' + str(where[k]) + '"'
            else:
                _where += ' and '  + k + ' = "' + str(where[k]) + '"'
        return _where

preb = ''
db = MysqlHelper()
# 查询sql
def db_sql(sql):
    res = db.db_fetch_all(sql)
    return res

# 查询单条
def db_info(table , where):
    _where = db.where_fun(where)
    sql = "select * from " + preb + table + _where + " limit 1"
    res = db.db_fetch_info(sql)
    return res

# 查询全部
def db_all(table , where):
    _where = db.where_fun(where)
    sql = "select * from " + preb + table + _where
    res = db.db_fetch_all(sql)
    return res

# 添加数据
def db_add(table , params):
    res = db.params_fun(params)
    sql = "insert into " + preb + table + " ("+res['fields']+") values ("+res['values']+")"
    res = db.db_update(sql)
    return res

# 修改数据
def db_update(table , where , params):
    _where = db.where_fun(where)
    _set = db.set_fun(params)
    sql = "update " + preb + table + " set " + _set + _where
    res = db.db_update(sql)
    return res

# 删除
def db_del(table , where):
    _where = db.where_fun(where)
    sql = "delete from " + preb + table + " " + _where
    res = db.db_update(sql)
    return res

# db_info("user",{"account":'22'})
# db_add("user",{"account":'aa','password':313131})
# db_update("user",{"id":37},{"account":'dada','password':313131})
# db_del("user",{"id":36})