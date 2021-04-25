//www.elegoo.com
//2016.12.08
#include "SR04.h"

#include "pin_configuration.h"

#define NUMMBER_SENSOR 2
#define FREQ 40 //Hz 

SR04 sensor[NUMMBER_SENSOR] = { SR04(ECHO_PIN1, TRIG_PIN1), SR04(ECHO_PIN2, TRIG_PIN2) };
double distance[NUMMBER_SENSOR] = {0.0 };

void setup() {
   Serial.begin(9600);
   delay(100);
}

int x = 0;
String inputString = "";     // a String to hold incoming data
bool stringComplete = false; // whether the string is complete

void loop() {
   // Sav sensor data in the table
   distance[x] = sensor[x].Distance();
   x = (x + 1) % NUMMBER_SENSOR;

   // Serial read
   if (stringComplete)
   {
      // Serial.println(inputString);
      if (inputString[0] == 'S')
      {
         if (inputString[1] == 'A')
         {
            // Print all data
            for (int x = 0; x < NUMMBER_SENSOR; x++)
            {
               Serial.print(distance[x]);
               if (x != NUMMBER_SENSOR - 1)
                  Serial.print("; "); // Delete ; at end of the line
            }
            Serial.println();
         }
         else
         {
            int index = inputString.substring(1).toInt();
            if (-1 < index && index < NUMMBER_SENSOR)
            {
               Serial.println(distance[index]);
            }
         }
      }
      // clear the string:
      inputString = "";
      stringComplete = false;
      Serial.flush();
   }
   // Delay for all sensor
   delay(1 / (NUMMBER_SENSOR * FREQ));
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent()
{
   while (Serial.available())
   {
      // get the new byte:
      char inChar = (char)Serial.read();
      // add it to the inputString:
      if (isPrintable(inChar))
         inputString += inChar;
      // if the incoming character is a newline, set a flag so the main loop can
      // do something about it:
      if (inChar == '\n')
      {
         stringComplete = true;
      }
   }
}