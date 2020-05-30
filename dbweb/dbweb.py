from flask import Flask, render_template, request
from sqlite3 import connect

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/db')
def db_editor():
    command = request.args.get('command', '')
    con = connect('base.db')
    cur = con.cursor()
    if command == '':
        items = cur.execute('SELECT * FROM students').fetchall()
        cur.close()
        con.close()
        return render_template('db_web.html', items=items)
    else:
        cur.execute(command)
        con.commit()
        items = cur.execute('SELECT * FROM students').fetchall()
        cur.close()
        con.close()
        return render_template('db_web.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
