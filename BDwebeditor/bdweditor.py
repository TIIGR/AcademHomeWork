from flask import Flask, render_template, request
from sqlite3 import connect

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/db')
def db_editor():
    lst = request.args.get('command', '').split()
    con = connect('base.db')
    cur = con.cursor()
    if len(lst) != 3 or len(lst[2]) != 1:
        items = cur.execute('SELECT * FROM students').fetchall()
        cur.close()
        con.close()
        return render_template('db_editor.html', items=items)
    else:
        cur.execute('UPDATE students SET "' + lst[0] + '" = "' + lst[2] + '" WHERE Z = "' + lst[1] + '"')
        con.commit()
        items = cur.execute('SELECT * FROM students').fetchall()
        cur.close()
        con.close()
        return render_template('db_editor.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
