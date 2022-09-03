import re
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




@app.route("/",methods=["GET", "POST"])
@app.route("/home",methods=["GET", "POST"])
def homePage():
    if request.method == "POST":
        day = request.form["day"]

        dataObject = {
            "avoid": ["Squats with dumbbells or weights", "Bench press", "Leg press", "Long-distance running", "Abdominal crunches", "Upright row", "Deadlift", "High-intensity interval training", "Rock climbing", "Power clean"],
            "imagename": "../static/images/" + day + ".png"
            }
        if day == "1":
            dataObject["name"] = "Water Aerobics"
            dataObject["categories"] = ["Aqua jogging","Flutter kicking","Leg lifts","Standing water push-ups","Arm curls"]
        elif day == "2":
            dataObject["name"] = "Chair Yoga"
            dataObject["categories"] = ["Overhead stretch","Seated cow stretch","Seated cat stretch","Seated mountain pose","Seated twist"]
        elif day == "3":
            dataObject["name"] = "Resistance band workouts"
            dataObject["categories"] = ["Leg press", "Triceps press", "Lateral raise", "Bicep curl", "Band pull apart"]
        elif day == "4":
            dataObject["name"] = "Pilates"
            dataObject["categories"] = ["Mermaid movement", "Side circles", "Food slides", "Step ups", "Leg circle"]
        elif day == "5":
            dataObject["name"] = "Walking"
            dataObject["categories"] = ["Find a moderate trail through a park", "Find a walk-friendly race to train for", 
            "Walk the perimeter of a familiar building", "Find an audiobook or a playlist for stimulation during your walk"]
        elif day == "6":
            dataObject["name"] = "Body weight workouts"
            dataObject["categories"] = ["Squats to chair", "Stepup", "Bird dog", "Lying hip bridges", "Side lying circles"]
        elif day == "7":
            dataObject["name"] = "Dumbbell strength training"
            dataObject["categories"] = ["Bent-over row", "Tricep extension", "Bicep curl", "Overhead press", "Front raise"]
        
        return render_template("exercise.html", data=dataObject)


    return render_template("index.html")


@app.route("/contact")
def contactDoctor():
    return render_template("contact.html")



if __name__=="__main__":
    app.run(debug=True)