import sqlite3

# Flaskからimportしてflaskを使えるようにする
from flask import Flask, session, render_template, request, redirect
import datetime
import json

# appという名前でFlaskアプリを作っていく！
app = Flask(__name__)

# シークレットキーの設定 sessionを使えるようにする
app.secret_key = "sunabaco"

# ルートの挙動調べる


@app.route("/")
def top_html():
    return render_template("top.html")


# 新規登録


@app.route("/signup", methods=["GET"])
def signup_get():
    # データベースと合わせる
    # if "user_id" in session:
    #     return redirect("/main")
    # else:
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    # if "user_id" in session:
    #     return redirect("/main")
    # else:
    # 入力フォームから値を取ってくる
    name = request.form.get("name")
    password = request.form.get("password")
    email = request.form.get("email")

    conn = sqlite3.connect("notbose.db")
    c = conn.cursor()
    c.execute("insert into user values(null,?,?,?)",
              (name, email, password))
    conn.commit()
    c.execute("select userid from user where email=? and password=?",
              (email, password))
    # もってきたデータを入れるための変数
    user_id = c.fetchone()
    c.close()
    print(user_id)

    session["user_id"] = user_id[0]
    return render_template("/add_newhabits.html")


# ログイン
@app.route("/login", methods=["GET"])
def login_get():
    if "user_id" in session:
        return redirect("/main")
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    # login.htmlに入力した名前とパスワードを取ってくる
    email = request.form.get("email")
    password = request.form.get("password")
    # データベースに接続
    conn = sqlite3.connect("notbose.db")
    c = conn.cursor()
    # 名前、パスワードと一致するIDを取得
    c.execute("select userid from user where email=? and password=?",
              (email, password))
    # もってきたデータを入れるための変数
    user_id = c.fetchone()
    c.close()
    print(user_id)

    # IDが存在しなかった時
    if user_id is None:
        return render_template("login.html")

    # 見つかった時はsessionを利用
    else:
        # fetchoneで取ってきたデータは（1,）となっているので、値だけを取り出す
        session["user_id"] = user_id[0]
        return redirect("/main")


# 習慣の追加add_newhabits
@app.route("/add_newhabits", methods=["GET"])
def add_newhabits_get():
    # if "user_id" in session:
    #     return render_template("add_newhabits.html",)
    # else:
    #     return redirect("/login")
    return render_template("/add_newhabits.html")


@app.route("/add_newhabits", methods=["POST"])
def add_newhabits():
    # if "user_id" in session:
    #

    # 入力フォームから値を取ってくる
    user_id = session["user_id"]
    task = request.form.get("task")
    days = request.form.get("days")

    conn = sqlite3.connect("notbose.db")
    c = conn.cursor()

    c.execute("insert into task (taskid,userid,task,days) values(null,?,?,?)",
              (user_id, task, days))


    #calendarテーブルに新しいtaskを追加する
    c.execute("insert into calendar (taskid,day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25,day26,day27,day28,day29,day30,day31) values(null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")


    conn.commit()
    c.close()

    return redirect("/main")


@app.route("/edit/<int:id>")
def edit(id):
    if "user_id" in session:
        conn = sqlite3.connect("notbose.db")
        c = conn.cursor()
        c.execute("select task from task where taskid= ?", (id,))
        task = c.fetchone()
        c.close()

        if task is not None:
            # タプル（’を外すため･
            task = task[0]
        else:
            return "タスクがありません"

        item = {"id": taskid, "task": task}
        return render_template("change_habits.html", task=item)
    else:
        return redirect("/main")
# 編集ボタンを押したら追加されてしまうのを、編集出来るようにする
# 新しくルートを作るaddのところを参考に


@app.route("/edit", methods=["POST"])
def edit_task():
    user_id = session["user_id"]
    task = request.form.get("task")
    time = request.form.get("time")
    days = request.form.get("days")

    conn = sqlite3.connect("notbose.db")
    c = conn.cursor()

    c.execute("insert into task (taskid,userid,task,time,days) values(null,?,?,?,?)",
              (user_id, task, time, days))
    conn.commit()
    c.close()

    return redirect("/main")


@app.route("/main")
def main_task():
    # user_idがsessionに入っているかどうか
    if "user_id" in session:
        # sessionからIDを取ってくる
        user_id = session["user_id"]
        conn = sqlite3.connect("notbose.db")
        c = conn.cursor()
        # ユーザーの名前を表示する
        c.execute("select name from user where userid=?", (user_id,))
        user_info = c.fetchone()
        print(user_info)
        # 現在のタスクを表示
        c.execute(
            "select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
        task_now = c.fetchone()
        print(task_now)
        # user_idが登録しているタスクで終了しているものを取る
        c.execute(
            "select taskid,task,days from task where userid = ? and end=1", (user_id,))
        task_list = []
        # 値を入れるコード fetchallをrow に入れるのよ！データがある分だけ繰り返しますよ！
        for row in c.fetchall():
            task_list.append({"id": row[0], "task": row[1], "days": row[2]})


        #ここにカレンダーのコードを挿入
        # c.execute("select taskid from task where userid=?", (user_id,))
        # task_now = c.fetchone()

        c.execute('SELECT day1 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success1=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day2 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success2=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day3 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success3=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day4 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success4=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day5 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success5=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day6 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success6=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day7 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success7=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day8 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success8=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day9 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success9=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day10 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success10=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day11 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success11=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day12 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success12=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day13 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success13=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day14 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success14=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day15 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success15=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day16 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success16=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day17 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success17=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day18 FROM calendar where taskid = ?',(task_now[0],))#列名の頭に数字は使えない
        succeess_failed=c.fetchone()[0]
        conn.commit()

        c.execute('SELECT day19 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success19=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day20 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success20=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day21 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success21=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day22 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success22=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day23 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success23=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day24 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success24=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day25 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success25=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day26 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success26=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day27 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success27=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day28 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success28=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day29 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success29=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day30 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success30=c.fetchone()[0]
        print(task_now[0])

        c.execute('SELECT day31 FROM calendar where taskid = ?',(task_now[0],))#これを31日分コピペ
        success31=c.fetchone()[0]
        print(task_now[0])

        
        #ここにカレンダーのコードを挿入
        #これを1～31日までコピペしてそれぞれ別の変数で定義


        c.close()

        print(task_list)
        return render_template("/main.html", task_list=task_list, user_info=user_info, task_now=task_now, success1 = success1, success2 = success2, success3 = success3, success4 = success4, success5 = success5, success6 = success6, success7 = success7, success8 = success8, success9 = success9, success10 = success10, success11 = success11, success12 = success12, success13 = success13, success14 = success14, success15 = success15, success16 = success16, success17 = success17, succeess_failed = succeess_failed, success19 = success19, success20 = success20, success21 = success21, success22 = success22, success23 = success23, success24 = success24, success25 = success25, success26 = success26, success27 = success27, success28 = success28, success29 = success29, success30 = success30, success31 = success31,)
    else:
        return redirect("/login")


#青山追加
# これをコピペで1～31日まで作る
# サイトからdbに成果を反映するコード
now = datetime.datetime.now()
today='day'+str(now.day)
# today='day2'#後で消す
@app.route("/succeess", methods=["POST"])
def succeess():
    if "user_id" in session:

        if today == "day1":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day1 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day2":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day2 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day3":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day3 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day4":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day4 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day5":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day5 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day6":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day6 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day7":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day7 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day8":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day8 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day9":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day9 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day10":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day10 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day11":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day11 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day12":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day12 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day13":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day13 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day14":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day14 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day15":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day15 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day16":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day16 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day17":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day17 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day18":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            # c.execute("select taskid from calendar")
            c.execute('update calendar set day18 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()
            #else ifで1～31日まで作成

        elif today == "day19":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day19 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day20":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day20 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day21":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day21 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day22":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day22 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day23":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day23 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day24":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day24 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day25":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day25 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day26":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day26 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day27":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day27 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day28":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day28 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day29":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day29 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day30":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day30 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        elif today == "day31":
            user_id = session["user_id"]
            conn = sqlite3.connect('notbose.db')
            c = conn.cursor()
            c.execute("select taskid,task,time,days from task where userid=? and end is null order by taskid", (user_id,))
            task_now = c.fetchone()
            c.execute('update calendar set day31 = 1 where taskid = ?',(task_now[0],))
            conn.commit()
            conn.close()

        else:
            return render_template('login.html')
    else:
        return render_template("login.html")
    return redirect("/main")
#青山追加


@app.route("/del/<int:id>")
def delete_task(id):
    if "user_id" in session:
        conn = sqlite3.connect("notbose.db")
        c = conn.cursor()
        # dbを削除する時
        c.execute("delete from task where taskid=?", (id,))
        # dbの書き換えをしたので、ライトチェンジズする
        conn.commit()
        c.close()

        return redirect("/add_newhabits")
    else:
        return redirect("/login")


@app.route("/end/<int:id>")
def end_task(id):
    if "user_id" in session:
        conn = sqlite3.connect("notbose.db")
        c = conn.cursor()
        # dbのendカラムに1を入れる
        c.execute("update task set end=1 where taskid=?", (id,))
        # dbの書き換えをしたので、ライトチェンジズする
        conn.commit()
        c.close()

        return redirect("/add_newhabits")
    else:
        return redirect("/login")


@app.route("/logout")
# sessionの中の値を出す（空っぽにする）＝ログアウト
def logout():
    session.pop("user_id", None)
    return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
