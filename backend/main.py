from fastapi import FastAPI, Request
from supabase import create_client, Client
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import json
import yaml

import random
import string

app = FastAPI()
config = yaml.safe_load(open('backend/config.yml'))

url = config['SUPABASE_URL']
key = config['SUPABASE_KEY']

supabase: Client = create_client(url, key)


origins = [
    "http://localhost:3400",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Note(BaseModel):
    cave_key: str
    data: str


@app.get("/")
async def home():
    data = {
        "page": "Home Page"
    }
    return data


@app.post("/addnote/")
async def save_name(note: Note):
    note_dict = {
        'cave_key': note.cave_key,
        'data': note.data
    }
    supabase.table("Notes").insert(note_dict).execute()
    return note


# sending list with GET
@app.get("/notes/{key}")
async def send_notes(key: str):
    notes = supabase.table("Notes").select("id", "created", "data").eq('cave_key', key).execute()
    print(notes)
    return {json.dumps(notes.data)}


@app.get("/check/{key}")
async def check(key: str):
    res = supabase.table("Caves").select("*", count="estimated").eq('cave_key', key).execute()
    print(res.count)
    if res.count:
        board_name = res.data[0]['cave_name']
        return {'state': 'true',
                'name': board_name}
    return {'state': 'false',
            'name': ''}


# delete note
@app.delete("/delete_note/{cave_key}/{note_id}")
async def delete_note(cave_key: str, note_id: int):
    supabase.table("Notes").delete().eq("id", note_id).eq("cave_key", cave_key).execute()
    return {
        "ok": True
    }


def random_key(n):
    # get random password pf length 8 with letters, digits, (+ string.punctuation)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(n))


class Cave(BaseModel):
    creator_name: str
    cave_name: str


# create cave
@app.post("/createcave/")
async def save_name(cave: Cave):
    print(cave)
    #  generate random cave_key with 8 letters/digits
    key = random_key(8)
    cave_dict = {
        'cave_name': cave.cave_name,
        'creator_name': cave.creator_name,
        'cave_key': key
    }
    supabase.table("Caves").insert(cave_dict).execute()
    return {"key": key}


class Feedback(BaseModel):
    email: str
    text: str


# save feedback
@app.post("/feedback/")
async def get_feedback(feedback: Feedback):
    print(feedback)
    feedback_dict = {
        'email': feedback.email,
        'text': feedback.text,
    }
    supabase.table("Feedback").insert(feedback_dict).execute()
    return {"ok": True}
