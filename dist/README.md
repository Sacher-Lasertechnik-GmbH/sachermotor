# sachermotor - Distribution Folder

## CONTENTS

### /pyd
    Contains the precompiled .pyd extension modules for:
    - Python 3.9 (x64)
    - Python 3.10 (x64)
    - Python 3.11 (x64)
    - Python 3.12 (x64)
    - Python 3.13 (x64)

    These files can be copied directly into your project folder
    and imported as a standard Python module:
        import sachermotor

### /whl
    Contains the corresponding .whl (wheel) packages for each
    supported Python version. These can be installed using pip:
        pip install sachermotor-1.0.0-cp<pythonversion>-cp<pythonversion>-win_amd64.whl

### /GUI
    Contains the standalone Windows GUI installer:
        sachermotorGUI_setup.exe
    This allows full motor control without writing Python code.


## NOTES
- **Windows-only** due to dependency on
  the EposCMD64.dll from Maxon.
- Ensure the DLL is available in the same directory or select it manually when prompted.
- Compatible with Python 3.9 – 3.13 (64-bit).