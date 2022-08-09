# command_modem
Command_modem gives an example how to command your modem by WebDriver/Python. 
It could be helpful if you wish to restart or toggle wi-fi by one click on shortcut on your desktop.

The code is working for D-Link Dir 651.

Parameters:

-r - restart modem

-w - toggle wi-fi

In order to use the code with other modem models it is necessary to  customize config.py:

  -change XPATHs  to login/password fields and confirm button in login screen

  -change login and password values
 
  -change URLs to restart and WI-FI pages

  -change XPATHs to correspnding checkboxes and buttons
 
