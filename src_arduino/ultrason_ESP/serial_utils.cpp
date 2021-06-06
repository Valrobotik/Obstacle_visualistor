#include "serial_utils.h"


String serial_event()
{
    // For test; reading serial
    String inputString = "";     // a String to hold incoming data
    char inChar = '0';
    while(inChar != '\n')
    {
        if (Serial.available())
        {
            // get the new byte:
            inChar = (char)Serial.read();
            // add it to the inputString:
            if (isPrintable(inChar) || inChar == '\n') inputString += inChar;
            // if the incoming character is a newline, set a flag so the main loop can
            // do something about it:
        }
    }
    // Serial.println(inputString);
    // clear the string:
    Serial.flush();
    return inputString;
}
