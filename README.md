# Arduino Volume Control 

This is an Arduino programme + python script to change the volume on a Mac using an Arduino and a rotary sensor. It can also control the brightness of a light depending on the volume (higher volume -> brighter light).

It has one command line argument:
`--force` makes it force the volume to correspond to the angle on the rotary sensor, running the script with it makes it impossible to change the volume using other means (using the computer itself).

Future work could be to make this run wirelessly. The Arduino's bluetooth is BLE (Bluetooth Low Energy), which cannot send information to laptops, but can send information to Android/iOS devices, so a mobile app can be made for this.
Otherwise, a regular Bluetooth 4.0 can be hooked up to the Arduino circuit to make it connect to computers. 
