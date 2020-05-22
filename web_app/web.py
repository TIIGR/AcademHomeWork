from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/prime', methods=['GET'])
def prime():
    n = int(request.args.get('n'))
    if n is None:
        n = 1
    if n <= 0:
        return render_template('prime.html', N="Число не является натуральным!", n=n)
    else:
        if n == 1:
            return render_template('prime.html', N="True", n=n)
        else:
            d = 2
            while n % d != 0:
                d += 1
            return render_template('prime.html', N=d == n, n=n)


if __name__ == '__main__':
    app.run(debug=True)
