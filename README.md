# sachermotor

**sachermotor** is a Python module for controlling Sacher laser systems.

Important: The module requires **EposCMD64.dll**, which must be downloaded separately from Maxon (https://www.maxongroup.com/).
If the DLL is not found, a dialog window will appear asking for its location.

---

## Installation

1. Download the appropriate `.whl` or `.pyd` file for your Python version.
2. Install using pip:

    pip install sachermotor-1.0.0-cp310-cp310-win_amd64.whl

   example for Python 3.10

   or copy the `.pyd` file directly into your project directory.

   Make sure EposCMD64.dll is either in the same folder or select it via the dialog when prompted.

---

## Quick Start

### Description

Connect to your Sacher motor and move to the center wavelength of your system’s range.

```python
from sachermotor import motor
# Import class Motor from SacherMotorControl

MC = motor()
# Create an instance of the motor class

MC.connect("USB0")
# Connects the motor

# Get wavelength limits and calculate the center wavelength
minWl, maxWl = MC.getWavelengthMinMax()
centerWl = (maxWl - minWl) / 2 + minWl

# Move to the center wavelength
MC.moveToWavelength(centerWl)

# Disconnect the motor
MC.disconnect()
```

---

## GUI Version

The GUI allows full motor control without writing Python code and is provided as sachermotorGUI_setup.exe.
During installation, you will be asked to provide the required but not included EposCMD64.dll.

---

## Key Methods

### Connection

#### `connect(usb)`
Tries to establish a connection to the EPOS.

**Parameters:**
- `usb` (str): The USB port on which the connection should be established. Default = `'USB0'`.

**Returns:**  
- `bool`: `True` if successful.

#### `disconnect()`
Disconnects from the motor and saves parameters.

---

### Configuration

#### `setVelocityParameter(velocity, acceleration, deceleration)`
Converts the given parameters from nm/s to revolutions per minute (rpm) and nm/s² to rpm/s,  
then stores them on the EPOS.

**Parameters:**
- `velocity` (int): Given in nm/s.  
- `acceleration` (int): Given in nm/s².  
- `deceleration` (int): Given in nm/s².  

If the given values aren't within the allowed range, they are set to the possible maximum or minimum.

#### `getVelocityParameter()`
Returns velocity, acceleration, and deceleration in nm/s or nm/s².  

**Returns:**  
- `(float, float, float)`

---

### Trigger

#### `triggerParameter(intervalWidth)`
Sets the parameters for the Position Compare Trigger.

**Parameters:**
- `intervalWidth` (float): Interval width for the trigger signal in nm.

#### `reverseMotionTrigger()`
Reverses the digital output for the Motion Trigger.

---

### Movement

#### `moveToWavelength(wavelength, highPrecision, trigger)`
Moves the motor to a given wavelength.

**Parameters:**
- `wavelength` (float): Target wavelength in nm.  
- `highPrecision` (bool):  
  - `True` → High Precision Mode activated.  
    When the relative movement is negative, the motor drives 3000 or 10000 steps below the goal  
    to always approach it with a positive movement (step count depends on the motor screw used).  
  - Default = `False`.  
- `trigger` (int):  
  - `0` → No trigger.  
  - `1` → Position Compare Trigger (signal every ? nm).  
  - `2` → Movement Trigger.  
  - Default = `0`.

**Returns:**  
- Current wavelength.

#### `moveSteps(steps, trigger=0)`
Moves a certain number of steps (up to 5000) in either direction.

**Parameters:**
- `steps` (int): Number of steps to move.  
- `trigger` (int):  
  - `0` → No trigger.  
  - `1` → Position Compare Trigger.  
  - `2` → Movement Trigger.  
  - Default = `0`.

**Returns:**  
- Current wavelength.

#### `stopMovement()`
Stops the current motor movement.

---

### Status

#### `getWavelengthMinMax()`
Returns an array with `[Minimum Wavelength, Maximum Wavelength]`.

**Returns:**  
- `(float, float)`

#### `getMoving()`
Returns whether the system is currently moving.

**Returns:**  
- `True` if moving / `False` if stationary.

#### `getWavelength()`
Returns the current wavelength.

---

### Support

#### `generateSupportData()`
Generates a support `.txt` file to be sent to us for technical support.

---

## Examples

Full example scripts are available in the [`examples/`](./examples) folder:

| Example | Description |
|---------|-------------|
| `exampleCode_1.py` | Basic connection, velocity setup, step movements, move to center wavelength. |
| `exampleCode_2.py` | Stepwise wavelength scan using Movement Trigger with high precision. |
| `exampleCode_3.py` | Use Position Compare Trigger to generate pulses every 0.1 nm during motion. |


---

## Notes

- Designed specifically for Sacher laser systems.
- The EposCMD64.dll is required for communication.
- If the DLL is missing, a dialog window will allow manual selection.

---

## Contact

If there are any issues, please feel free to contact us:
contact@sacher-laser.com

---

## License

© 2025 Sacher Lasertechnik GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to use it
exclusively in conjunction with Sacher Lasertechnik GmbH hardware and systems, including commercial applications.

Redistribution, sublicensing, or inclusion of this Software in other products or software packages
is not permitted without prior written permission from Sacher Lasertechnik GmbH.

---

Note:
The software requires EposCMD64.dll, which is not included in this repository and must be obtained separately from Maxon (https://www.maxongroup.com/).
Usage of the DLL is subject to Maxon’s licensing terms.
