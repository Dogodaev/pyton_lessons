import requests, json, turtle, time
from datetime import datetime

iss = turtle.Turtle()

def move_iss(lat, long):
    global iss
    print(iss.position())
    if(iss.position()==(0.00,0.00)):
        iss.penup()
    iss.goto(long, lat)
    iss.pendown()

def setup (window):
    global iss
    window.setup(1000, 500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')




def track_iis ():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)

    if (response.status_code == 200):
        response_dictionary = json.loads(response.text)
        position = response_dictionary['iss_position']
        lat = float(position['latitude'])
        long = float(position['longitude'])
        move_iss(lat,long)
    else:
        print('Хьюстон, у нас проблема:',requests.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iis)

def main():
    global iis
    screen = turtle.Screen()
    setup(screen)
    track_iis()
    
if __name__ == '__main__':
    main()
    turtle.mainloop()

