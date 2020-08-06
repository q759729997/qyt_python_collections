from tinydb import TinyDB, Query
db = TinyDB('./temp/TinyDB.json')
User = Query()
db.insert({'name': 'John', 'age': 22})
print(db.search(User.name == 'John'))
db.insert({'name': '约翰', '年龄': 22, 'sex': '男'})
print(db.search(User.name == '约翰'))
