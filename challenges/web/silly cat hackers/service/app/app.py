from flask import Flask, request, redirect, url_for, render_template, session, make_response

app = Flask(__name__)
app.secret_key = 'wowowoowowwoowwwwww'

@app.route('/')
def index():
    print("success")
    return render_template('index.html')

@app.route('/login')
def login_page():
    print("success")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template("dashboard.html")
    else:
        return "you're not an admin!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'HorsesAndCows':
            session['logged_in'] = True
            return render_template("dashboard.html")
        else:
            return "Invalid credentials"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1337)
