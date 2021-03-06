import sqlite3

# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('SELECT day13 FROM calendar where taskid = 1')#列名の頭に数字は使えない
# print(c.fetchone()[0])
# conn.commit()
# conn.close()

# print(1)


# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('update calendar set day13 = 1 where taskid = 1')
# conn.commit()
# conn.close()



# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('update calendar set @day text ; = 0 where taskid = 1')
# conn.commit()
# conn.close()


#日付だけ取得してSQLにデータを書き込むコード
# import datetime
# now = datetime.datetime.now()
# today='day'+str(now.day)
# if today == "day16":
#     conn = sqlite3.connect('notbose.db')
#     c = conn.cursor()
#     c.execute('update calendar set day16 = 1 where taskid = 1')#setの後ろをtodayにしたい
#     conn.commit()
#     conn.close()
# else:
#     print("fail")


# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('update calendar set ? = 1 where taskid = 1', ((today(),))#setの後ろをtodayにしたい
# conn.commit()
# conn.close()

# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.executescript('update calendar set ('%') = 1 where taskid = 1'%(today,))#setの後ろをtodayにしたい
# conn.commit()
# conn.close()

# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('update calendar set {0} = 1 where taskid = 1', ((today(),))#setの後ろをtodayにしたい
# conn.commit()
# conn.close()


#pythonでtaskidを取得してSQLに渡すコード
# taskid=1
# conn = sqlite3.connect('notbose.db')
# c = conn.cursor()
# c.execute('update calendar set day16 = 0 where taskid = ?',(taskid,))#setの後ろをtodayにしたい
# conn.commit()
# conn.close()



conn = sqlite3.connect('notbose.db')
c = conn.cursor()
print(c.execute('select taskid from calendar'))
conn.close()