from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/add_person')
def add_person():
    return "<h1> Add Person Page </h1>"

@views.route('/edit_person')
def edit_person():
    return "<h1> Edit Person Page </h1>"

@views.route('/delete_person')
def delete_person():
    return "<h1> Delete Person Page </h1>"