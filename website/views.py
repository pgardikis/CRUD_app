from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Person
from . import db
from .forms import AddPersonForm, EditPersonForm, SearchPersonForm

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    form = SearchPersonForm()
    people = []

    if form.validate_on_submit():
        search_person = form.search_person.data
        people = Person.query.filter(Person.firstname.ilike(f'%{search_person}%') | Person.lastname.ilike(f'%{search_person}%')).all()
    else:
        people = Person.query.all()
    return render_template("home.html", form=form, people=people)

@views.route('/add_person', methods=['GET', 'POST'])
def add_person():
    form = AddPersonForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        new_person = Person(firstname=firstname, lastname=lastname)
        db.session.add(new_person)
        db.session.commit()
        flash('Person added!', 'success')
        return redirect(url_for("views.home"))
    return render_template("add_person.html", form=form)

@views.route('/edit_person', methods=['GET', 'POST'])
def edit_person():
    form = EditPersonForm()

    if form.validate_on_submit():
        person_id = form.id.data
        person = Person.query.filter_by(id=person_id).first()
        if person:
            person.firstname = form.firstname.data
            person.lastname = form.lastname.data
            db.session.commit()
            flash('Person details updated successfully!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash(f'Person with ID {person_id} does not exist.', 'error')
    return render_template("edit_person.html", form=form)

@views.route('/delete_person', methods=['POST'])
def delete_person():
    person_id = request.form['id']
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    flash(f'Person with ID: {person_id} deleted successfully!', 'success')
    return redirect(url_for('views.home'))