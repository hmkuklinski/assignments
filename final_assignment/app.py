from flask import Flask, render_template, request, redirect
import json
import csv
from translate import Translator

flashcards= {}

app = Flask(__name__)

@app.route("/")
def index():
    json_file = 'words.json'
    try:
        with open(json_file, 'r') as file:
            data= json.load(file)
    except json.decoder.JSONDecodeError:
        data= {}
    return render_template("index.html",flashcards= data) #passes in the flashcard dictionary

@app.route("/add_flashcard", methods=["POST", "GET"])
def add():
    eng_word = request.form.get("english") #gets entered by user
    translator= Translator(to_lang="ko") #to korean
    translation = translator.translate(eng_word) #translate to english
    flashcards[eng_word]= translation #add to dictionary
    
    json_file = 'words.json'
    with open(json_file, 'w') as file:
        json.dump(flashcards, file)
    
    return redirect("/")


@app.route("/remove", methods=["POST"])
def remove():
    word= request.form.get("word")
    print(f"Word received by request: {word}")
    if word in flashcards:
        print(f"Removing flashcard: {flashcards[word]}")
        del flashcards[word]
        print(f"Flashcards after removal: {flashcards}")
        #need to edit the json file with the removal
        json_file = 'words.json'
        with open(json_file, 'w') as file:
            json.dump(flashcards, file)
    else:
        print(f"Flashcard with word '{word}' is not found.")
            
    return redirect(request.referrer)

if __name__== '__main__':
    app.run(debug=True)

    
    
    