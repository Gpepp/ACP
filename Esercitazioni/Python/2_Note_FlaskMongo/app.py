from flask import Flask, request
import uuid

app = Flask("__main__")


notes = {}

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

    id = uuid.uuid4().hex
    notes[id] = request.get_json()
    return {"result":'note added', 'id':id}


@app.get('/notes')
def get_notes():
    return notes

@app.get('/note/<id>')
def get_note(id):
    try:
        return notes[id]
    except KeyError:
        return {'result':'No Note', 'id':id}, 400

@app.delete('/note/<id>')
def delete_note(id):
    try:
        notes.pop(id)
        return {'result':' Note Deleted', 'id':id}, 200
    except KeyError:
        return {'result':'No Note', 'id':id}, 400







if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)