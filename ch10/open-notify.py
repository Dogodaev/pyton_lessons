import requests, json, turtle, time
from datetime import datetime



def move_iss(lat, long):
    global iss
    print(iss.position())
    if(iss.position()==(0.00,0.00)):
        iss.penup()
    iss.goto(long, lat)
    iss.pendown()

def settings (screen):
    global iss
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    iss.pencolor('red')




def track_iis ():
    while True:
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
        time.sleep(5)
        
def main():
    global iis
    screen = turtle.Screen()
    settings(screen)
    track_iis()

iss = turtle.Turtle()
if __name__ == '__main__':
    main()
    turtle.mainloop()

