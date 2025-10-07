from sachermotor import motor
#import class motor from sachermotor

MC = motor()
#creates a instance of the class motor

MC.connect("USB0")
#connects the Motor

MC.setVelocityParameter(2,MC.getVelocityParameter()[1],MC.getVelocityParameter()[2])
#changing the velocity of the system and leaving the acceleration and decceleration the same

MC.moveSteps(-300)
#moves 300 steps down
MC.moveSteps(300)
#moves 300 steps up

maxWl = MC.getWavelengthMinMax()[1]
minWl = MC.getWavelengthMinMax()[0]
centerWl = (maxWl - minWl)/2 + minWl
#getting the center wavelength

MC.moveToWavelength(centerWl)
#moves to the center wavelength

MC.disconnect()
#disconnects the motor