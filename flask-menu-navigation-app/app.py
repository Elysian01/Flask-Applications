from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        select = request.form.get('select_operation')
        if(select == 'add'):
            # return render_template('operation.html', op="Addition")
            return redirect(url_for('operation', op="add"))
        elif(select == 'subtract'):
            return redirect(url_for('operation', op="subtract"))
        elif(select == 'multiply'):
            return redirect(url_for('operation', op="multiply"))

    return render_template("home.html")


@app.route('/operation', methods=['GET', 'POST'])
def operation():
    if request.method == 'POST':
        first_number = request.form.get('first_number')
        second_number = request.form.get('second_number')
        op = request.args.get('op')
        if op == "add":
            result = float(first_number) + float(second_number)
            return render_template("result.html", result=result)
        elif op == "subtract":
            result = float(first_number) - float(second_number)
            return render_template("result.html", result=result)
        elif op == "multiply":
            result = float(first_number) * float(second_number)
            return render_template("result.html", result=result)
    return render_template("operation.html")


@app.route('/result', methods=['POST'])
def result():
    return render_template("result.html")


# other request: put and delete
if __name__ == '__main__':
    app.run(debug=True)
