from flask import Blueprint,render_template,request,flash, jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json

pages = Blueprint("pages",__name__)

#homepage routing
@pages.route('/',methods = ["GET","POST"])
@login_required
def home_page():
    if request.method=="POST":
        note = request.form.get("note")
        if len(note)<1:
            flash("Your note should contain atleast 1 character",category='error')
        else:
            new_note = Note(text=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            print(current_user.notes)
            flash("New note has been added!",category='success')
        
    return render_template("home.html",user=current_user)

#delete note routing
@pages.route('delete-note',methods = ["POST"])
def delete_Note():
    note_req_file = json.loads(request.data.decode('utf-8'))
    print(note_req_file)
    noteId = note_req_file['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})