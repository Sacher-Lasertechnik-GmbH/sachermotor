from sachermotor import motor
#import class motor from sachermotor
from time import sleep

MC = motor()
#creates a instance of the class motor

MC.connect()
#connects the Motor

maxWl = MC.getWavelengthMinMax()[1]
minWl = MC.getWavelengthMinMax()[0]
#getting the max and min wavelength

#MC.reverseMotionTrigger()
#could be used to switch the trigger from 5V while moving 0V standing to 5V while standing 0V moving

for x in range(11):
    stops = (maxWl-minWl)*x/10 + minWl
    MC.moveToWavelength(stops,1,2)
    sleep(1)
#moves to the minimum wavelenght first and than starts to move 10 times 1/10 of the wavelength range up waiting at every stop
#while using the movement trigger and highpresionmode

MC.disconnect()
#disconnects the motor
