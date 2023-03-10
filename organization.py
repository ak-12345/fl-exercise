from flask import Flask, request, redirect, render_template

app = Flask(__name__)

orgs = ['Organization 1', 'Organization 2', 'Organization 3', 'Organization 4', 'Organization 5']
students = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        org = request.form['org']
        students[name] = org
        return redirect('/students')
    return render_template('home.html', orgs=orgs)

@app.route('/students')
def students_page():
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)