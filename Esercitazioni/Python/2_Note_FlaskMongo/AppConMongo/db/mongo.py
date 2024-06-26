from pymongo import MongoClient
import json

class myClient:
    def __init__(self):
        self.url = "mongodb://127.0.0.1:27017"
        self.conn = MongoClient(self.url)
        self.db = self.conn['notes']
        self.collection = self.db.all
    
    def insertNote(self,note):
        print(note)
        id = self.collection.insert_one(note)
        return id

    def deleteNote(self,id):
        return self.collection.find_one_and_delete({'id': id})
    
    def notes(self):
        notes = self.collection.find()
        return notes
    
    def note_by_id(self,id):
        return self.collection.find_one({'id':id})
    
    def note_by_name(self,nome):
        return self.collection.find({'title':nome})