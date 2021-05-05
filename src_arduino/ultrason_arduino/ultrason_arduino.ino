//www.elegoo.com
//2016.12.08
#include "Ultrasonic.h"
#include "Adafruit_VL53L0X.h"

#include "pin_configuration.h"
#include "gcode_interpreter.h"

#define FREQ 40 //Hz

// TimeOut = Max.Distance(mm) * 5,88
int TimeOut = 2000 * 5.8; // 1 m de distance max

// Changer le nombre de capteur et les ajouter dans la liste suivante
const int NUMBER_ULTRASON = 2;
const int NUMBER_LASER = 1;
Ultrasonic Usensor[NUMBER_ULTRASON] = {Ultrasonic(TRIG_PIN1, ECHO_PIN1, TimeOut),
                                       Ultrasonic(TRIG_PIN2, ECHO_PIN2, TimeOut)};

Adafruit_VL53L0X Lsensor = Adafruit_VL53L0X();



// Début du programme de récupération des distances
const int number_sensor = NUMBER_ULTRASON + NUMBER_LASER;
double distance[number_sensor] = {0.0};

void setup() {
   Serial.begin(115200);
   // wait until serial port opens for native USB devices
   while (!Serial)
   {
      delay(1);
   }

   if (!Lsensor.begin())
      {
         Serial.println(F("Failed to boot VL53L0X"));
         while (1)
         ;
      }
}

int x = 0;
String inputString = "";     // a String to hold incoming data
bool stringComplete = false; // whether the string is complete

void loop() {
   // Save sensor data in a table
   if (x < NUMBER_ULTRASON)
   {
      distance[x] = Usensor[x].Distance();
   }
   else if (x < NUMBER_ULTRASON + NUMBER_LASER)
   {
      VL53L0X_RangingMeasurementData_t measure;
      Lsensor.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
      if (measure.RangeStatus != 4)
      {
         distance[x] = measure.RangeMilliMeter;
      }
   }
   x = (x + 1) % number_sensor;

   // Serial read
   if (stringComplete)
   {
      print_gcode2serial(inputString, distance, number_sensor);
      // clear the string:
      inputString = "";
      stringComplete = false;
      Serial.flush();
   }
   // Delay for all sensor
   delay(1 / (number_sensor * FREQ));
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