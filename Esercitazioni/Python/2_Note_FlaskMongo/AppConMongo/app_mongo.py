from flask import Flask, request
from db.mongo import myClient
import json


app = Flask("__main__")


db = myClient()

@app.get('/')
def main():
    return "<h1>Prova</h1>"


# curl --json '{"title":"Prova","text":"testo di prova", "tag":"casa"}' localhost:3000/note
@app.post('/note')
def addNote():
    try:
        title = request.get_json()['title']
        txt = request.get_json()['text']
        tag = request.get_json()['tag']
    except KeyError:
        return {'result':'key error bad format', 'id':-1}, 400
    
    print(f"reciveNote - title {title} - txt {txt} - tag {tag} ")

    note = request.get_json()
    print('pri')
    id = db.insertNote(dict(request.get_json()))

    return {"result":'note added', 'id': str(id.inserted_id)}
    #return "<h1>Prova</h1>"

# curl localhost:3000/notes
@app.get('/notes')
def get_notes():
    notes = db.notes()
    response_notes = [str(n) for n in notes]
    return {"result":'note', 'data': response_notes}
    # return "<h1>Prova</h1>" 

# curl localhost:3000/notes/id

@app.get('/note/<title>')
def get_note(title):
    
    result = db.note_by_name(title)
    response_notes = [str(n) for n in result]
    print(result)
    return {"result":'note', 'data': response_notes}
    

@app.delete('/note/<id>')
def delete_note(id):
    try:
        notes.pop(id)
        return {'result':' Note Deleted', 'id':id}, 200
    except KeyError:
        return {'result':'No Note', 'id':id}, 400




if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)
