//www.elegoo.com
//2016.12.08
#include "Ultrasonic.h"

#include "pin_configuration.h"
#include "gcode_interpreter.h"
#include "serial_utils.h"

TaskHandle_t Read_sensor_task;
TaskHandle_t Serial_event_task;

#define FREQ 40 //Hz

// TimeOut = Max.Distance(mm) * 5,88
int TimeOut = 2000 * 5.8; // 1 m de distance max

// Changer le nombre de capteur et les ajouter dans la liste suivante
#define NUMBER_SENSOR 11
Ultrasonic sensor[NUMBER_SENSOR] = {
    Ultrasonic(TRIG_PIN1, ECHO_PIN1, TimeOut),
    Ultrasonic(TRIG_PIN2, ECHO_PIN2, TimeOut),
    Ultrasonic(TRIG_PIN3, ECHO_PIN3, TimeOut),
    Ultrasonic(TRIG_PIN4, ECHO_PIN4, TimeOut),
    Ultrasonic(TRIG_PIN5, ECHO_PIN5, TimeOut),
    Ultrasonic(TRIG_PIN6, ECHO_PIN6, TimeOut),
    Ultrasonic(TRIG_PIN7, ECHO_PIN7, TimeOut),
    Ultrasonic(TRIG_PIN8, ECHO_PIN8, TimeOut),
    Ultrasonic(TRIG_PIN9, ECHO_PIN9, TimeOut),
    Ultrasonic(TRIG_PIN10, ECHO_PIN10, TimeOut),
    Ultrasonic(TRIG_PIN11, ECHO_PIN11, TimeOut)
};

// Début du programme de récupération des distances
double distance[NUMBER_SENSOR] = {0.0 };

void setup() {
   Serial.begin(115200);

   //create a task that will be executed in the Read_sensor() function, with priority 1 and executed on core 0
   xTaskCreatePinnedToCore(
       Read_sensor,           /* Task function. */
       "Read sensor task",    /* name of task. */
       10000,                 /* Stack size of task */
       (void *)&distance, /* parameter of the task */
       2,                     /* priority of the task */
       &Read_sensor_task,     /* Task handle to keep track of created task */
       0);                    /* pin task to core 0 */
   delay(500);

   //create a task that will be executed in the Serial_event() function, with priority 1 and executed on core 1
   xTaskCreatePinnedToCore(
       Serial_event,        /* Task function. */
       "Serial event task", /* name of task. */
       10000,               /* Stack size of task */
       (void *)&distance,   /* parameter of the task */
       1,                   /* priority of the task */
       &Serial_event_task,  /* Task handle to keep track of created task */
       1);                  /* pin task to core 1 */
   delay(500);
}

int x = 0;

void loop() 
{
   
}

// Fonction thread sur le core 0 pour lire les valeurs des capteurs et les stoquer dans le tableau distance.
// Cette fonction a la priorité sur l'autre fonction. La priorité est données à la récupération des informations capteurs
void Read_sensor(void * ptable_dist)
{
   double * table_dist = (double*)ptable_dist;
   while (true)
   {
      // Serial.print("Task running on core ");
      // Serial.println(xPortGetCoreID());
      // Save sensor data in a table
      table_dist[x] = sensor[x].Distance();
      x = (x + 1) % NUMBER_SENSOR;
      // Delay for all sensor
      delay( 3 );
   }
}

// Thread fonction sur le core 1 pour lire et interpréter le gcode transmis.
void Serial_event(void * ptable_dist)
{
   double *table_dist = (double *)ptable_dist;
   while (true)
   {
      // Serial.print("Task running on core ");
      // Serial.println(xPortGetCoreID());
      // Serial read
      if (Serial.available() > 2)
      {
         String input_string = serial_event();
         print_gcode2serial(input_string, table_dist, NUMBER_SENSOR);
      }
      delay(1);
   }
}