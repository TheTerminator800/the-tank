# The Tank

Code repository and demo videos for The Tank. The Tank was a final engineering project built during the Georgia Governor's Honors Program.

## Team Members:
- Aryan Mittal (Software)
- Jeffrey Chen (Electrical)
- Jace Whatley (Design)

## Description
The Tank was a remote-controlled vehicle that was modeled after an M4 Sherman. A large console (surrounded the base of a chair) with two levers and two foot pedals was constructed to remotely control The Tank using real-life tank controls as opposed to a handheld remote. The Tank mimicked the driving capability of a real tank, fired a 1 mW laser beam, and sent live video feed from an onboard camera to a publically-accessible web server.

### Tank
- Dimensions: 18in length x 9in width x 14in height
- Materials: wood, sheet metal, plastic continuous track, 3D-printed 12-tooth sprockets
- Raspberry Pi: received data sent from laptop, controlled motors, managed live video feed
- Vex motors: powered the tank by turning the sprockets

### Controls
- Levers: PVC pipes that turned potentiometers
- Pedals: throttle pedal that served as a binary on-off switch for Tank motion, firing pedal that controlled Tank laser beam
- Body: 3-sided U-shaped apparatus constructed from wood that surrounded a chair
- Arduino: read values from potentiometers and sent them via serial communication to laptop

## How It Worked
1. Arduino (mounted on underside of controls) reads values from laser pedal, throttle pedal, and potentiometers. Potentiometer data is only read if the throttle is pressed down. (`lever_steering.ino`)
2. Arduino sends data via USB serial connection to laptop. (`lever_steering.ino`)
3. Python script on laptop parses the data, encodes it, and sends it via UDP connection to the mounted Raspberry Pi (`client.py`)
4. Onboard Raspberry Pi receives the data and controls the tank accordingly. It will fire the laser based on the boolean sent for the laser value. The Pi also controls the motors based on the ranges in which the two potentiometer values fall. (`server.py`)
5. During all of this, the Pi also records live feed from an onboard camera and uploads it to a web server. (`feed.py`)