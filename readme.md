# Important Information about Mouse(Logitec) Configarator

### Install python 
`` pip install python3 ``

### Gonna get the communication to the device throught this api
`` pip install hidapi pynput ``

### Gives us the access to the keyboard
`` pip install keyboard ``

## To change configarion or add more profiles you will edit profile/ folder as you see fit
``` json 
{
    {
    "mouse_speed": 13,
    "macros": {
               "x1_hold": "ctrl+c",
               "x2_hold": "ctrl+v",
               "middle": "win+shift+s"
    }
}
```
### Run on start up
- Click "win + r" 
- enter "shell:startup" and put your "mouse_macros_startup.bat" in the folder
- The above will automatically run your script for you when you turn on your pc 
- Open the script first and update the path\to\project into the right one for you


by @realtriumphndlovu@gmail.com with love and KAre enjoy
