from flask import Flask, render_template, request, redirect
import json
import csv
from translate import Translator

flashcards= {}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",flashcards= flashcards) #passes in the flashcard dictionary

@app.route("/add_flashcard", methods=["POST", "GET"])
def add():
    eng_word = request.form.get("english") #gets entered by user
    translator= Translator(to_lang="ko") #to korean
    translation = translator.translate(eng_word) #translate to english
    flashcards[eng_word]= translation #add to dictionary
    
    return redirect("/")

@app.route("/remove", methods=["POST"])
def remove():
    word= request.form.get("word")
    print(f"Word received by request: {word}")
    if word in flashcards:
        del flashcards[word]
    return redirect("/")

if __name__== '__main__':
    app.run(debug=True)

    
    
    