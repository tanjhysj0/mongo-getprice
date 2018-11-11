from pymongo import MongoClient
conn = MongoClient('localhost',27017)

db = conn.testdb
db.col.insert({"name":'yanying','province':'江苏','age':25})

db.col.insert([
    {"name":'yanying','province':'江苏','age':25},
    {"name":'张三','province':'浙江','age':24},
    {"name":'张三1','province':'浙江1','age':25},
    {"name":'张三2','province':'浙江2','age':26},
    {"name":'张三3','province':'浙江3','age':28},
])