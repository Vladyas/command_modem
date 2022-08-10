"""
web interface automatization constants for D-Link DIR-651 web manager application
For more info, look directly to config.py code. All constants names are intuitive.
Don't forget to change login and password!
"""

# All settings are done for D-Link Dir-651
# MODEM ADMIN LOGIN DIALOG
# login and password fields full XPATHs. Could be found by Chrome DevTool.
FIELD_LOGIN_NAME = "A1"
FIELD_LOGIN_PWD = "A2"
# login and password
LOGIN_NAME = "admin"
LOGIN_PWD = "**************"

#RESTART MODEM page and button
# Modem restart page address
URL_RESTART_MODEM = "http://192.168.0.1/#system/sysconf"
# Restart button full XPATH. Could be found by Chrome DevTool.
BUTTON_RESTART = "/html/body/div[5]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]"

#WI-FI settings page
# Wi-Fi settings page address
URL_TOGGLE_WIFI = "http://192.168.0.1/#wifi/basic"
# Wi-Fi checkbox and Apply controls full XPATHs. Could be found by Chrome DevTool.
CHECKBOX_WIFI = "/html/body/div[5]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input"
BUTTON_APPLY_WIFI = "/html/body/div[5]/div[2]/div[2]/div[2]/div[3]/div[3]/div[3]/div/div/div[1]"

# START PARAMETERS
PARAM_RESTART = '-r'
PARAM_TOGGLE_WIFI = '-w'
