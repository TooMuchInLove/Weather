# Тёмная тема
DARK_THEME = """
QWidget {\n
    background: #232323;\n
    color: #FFFFFF;\n
}\n
QComboBox, QLabel {\n
    padding: 0 10px;\n
}\n
#lHumidity, #lWindSpeed, #lSunrise, #lSunset {\n
    padding: 0 30px;\n
}\n
#lDataNow {\n
    color: #E66038;\n
}\n
#lTemperature {\n
    color: #12A7E7;\n
}\n
#lError {\n
    background: #D72323;\n
    color: #EEEEEE;\n
}\n
#bRequest {\n
    background: #E66038;\n
}\n
#bRequest:hover {\n
    background: #D05532;\n
}\n
#bSettings, #bClose {\n
    background: #3B3B3B;\n
}\n
QComboBox, QLabel, #bSettings:hover, #bClose:hover {\n
    background: #2A2A2A;\n
}\n
QComboBox, QLabel, #bRequest, #bSettings, #bClose {\n
    border-radius: 5px;\n
}\n
"""
