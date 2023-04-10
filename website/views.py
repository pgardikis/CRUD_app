from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Person
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

@views.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        new_person = Person(firstname=firstname, lastname=lastname)
        db.session.add(new_person)
        db.session.commit()
        flash('Person added!', 'success')
        return redirect(url_for("views.home"))

    return render_template("add_person.html")

@views.route('/edit_person')
def edit_person():
    return render_template("edit_person.html")

@views.route('/delete_person')
def delete_person():
    return render_template("delete_person.html")