from flask import Flask, render_template, request
import json
from model.smart_devices import Home
from model.smart_devices import SmartDevice
from model.smart_devices import LightBulb

app = Flask(__name__)

@app.route("/")
def index():
    #add new home object and lightbulb object, add lightbulb object to home
    home= Home("Home Away from Home") #only parameter is address
    
    #want to access info in our json file:
    with open('light.json', 'r') as file: #will automatically close if we call it this way
        lb_data= json.load(file) #light bulb data from file
        for light in lb_data: #iterate through light bulbs in json 
            light_bulb= LightBulb(light['name'], light['manufacturer', light['brightness']]) 
            home.add_device(light_bulb) #add new device to home object
    return render_template('home.html', home=home) #want to display home.html, want home arguments to be passed in home template

@app.route("/add_lighbulb", methods=["POST"])
def add_lightbulb():
    #need to first get the json data and store in variable
    data= request.json
    #can get name, manufacturer, and brightness from dict 
    name= data.get('name')
    manufacturer = data.get('manufacturer')
    brightness = data.get('brightness')
    
    #want to see if all three are established and present in dict:
    if name and manufacturer and brightness is not None:
        lightbulb = LightBulb(name, manufacturer, brightness)
        new_lb_json= lightbulb.to_json()
    
    with open('light.json', 'r') as file:
        light_bulbs = json.load(file)
    light_bulbs.append(json.loads(new_lb_json))
    
    with open('light.json', 'w') as file:
        json.dump(light_bulbs, file)
        
   

if __name__== '__main__':
    app.run(debug=True)