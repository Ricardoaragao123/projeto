from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')  # Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  # Providing the schema for the note 
            db.session.add(new_note)  # Adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)  # This function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/regras.html')
def regras():
    return render_template('regras.html')

@views.route('/perfil.html')
def perfil():
    return render_template('perfil.html')

@views.route('/jogos.html')
def jogos():
    return render_template('jogos.html')

@views.route('/facil.html')
def facil():
    return render_template('facil.html', user=current_user)

@views.route('/medio.html')
def medio():
    return render_template('medio.html', user=current_user)

@views.route('/dificil.html')
def dificil():
    return render_template('dificil.html', user=current_user)

@views.route('/dificil1.html')
def dificil1():
    return render_template('dificil1.html', user=current_user)

@views.route('/dificil2.html')
def dificil2():
    return render_template('dificil2.html', user=current_user)

@views.route('/dificil3.html')
def dificil3():
    return render_template('dificil3.html', user=current_user)

