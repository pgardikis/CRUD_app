from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Person
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

@views.route('/search_person', methods=['GET'])
def search_person():
    query = request.args.get('search', '')
    people = Person.query.filter(Person.firstname.ilike(f'%{query}%') | Person.lastname.ilike(f'%{query}%')).all()
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

@views.route('/edit_person', methods=['GET', 'POST'])
def edit_person():
    if request.method == 'POST':
        person_id = request.form['id']
        person = Person.query.filter_by(id=person_id).first()

        if person:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            person.firstname = firstname
            person.lastname = lastname
            db.session.commit()
            flash('Person details updated successfully!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash(f'Person with ID {person_id} does not exist.', 'error')
    return render_template("edit_person.html")

@views.route('/delete_person', methods=['POST'])
def delete_person():
    person_id = request.form['id']
    person = Person.query.get(person_id)
    
    if person:
        db.session.delete(person)
        db.session.commit()
        flash(f'Person with ID: {person_id} deleted successfully!', 'success')
        return redirect(url_for("views.home"))
    else:
        flash(f'Person with ID: {person_id} does not exist.', 'error')
    return redirect(url_for('views.home'))