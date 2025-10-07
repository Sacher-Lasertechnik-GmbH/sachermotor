from sachermotor import motor
#import class motor from sachermotor

MC = motor()
#creates a instance of the class motor

MC.connect()
#connects the Motor

maxWl = MC.getWavelengthMinMax()[1]
minWl = MC.getWavelengthMinMax()[0]
#getting the max and min wavelength

MC.triggerParameter(0.1)
#setting the trigger to activate a triggerpulse every 0.1nm when position trigger is choosen at the movement function

MC.moveToWavelength(minWl,1,0)
#moves to the minimun Wavelength using the highprecisionmode and no trigger

MC.moveToWavelength(maxWl,0,1)
#moves to maximum wavelength using position trigger

MC.disconnect()
#disconnects the motor