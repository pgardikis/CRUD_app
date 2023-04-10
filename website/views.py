from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
    return render_template("add_person.html")

@views.route('/edit_person')
def edit_person():
    return render_template("edit_person.html")

@views.route('/delete_person')
def delete_person():
    return render_template("delete_person.html")