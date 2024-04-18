from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        # Redirect to admin dashboard if credentials are valid
        return redirect(url_for('admin_dashboard'))
    return render_template('login_admin.html')

@app.route('/employee/login', methods=['GET', 'POST'])
def employee_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        # Redirect to employee dashboard if credentials are valid
        return redirect(url_for('employee_dashboard'))
    return render_template('login_employee.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/employee/dashboard')
def employee_dashboard():
    return render_template('employee_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
