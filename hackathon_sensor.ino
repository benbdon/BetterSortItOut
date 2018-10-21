/*  This sketch monitors a digital hall sensor that returns high 
 *  when a trash can lid is closed. The script should monitor for
 *  changes in the state and signal over serial when the trash
 *  can is opened, then closed again.
 */

// TODO
// switch Serial.print to Serial.write
 

// Global Variables
int Led=13;         //define LED port
int buttonpin=3;    //define switch port
;int  reading;    //define digital variable reading
int last_reading;
int last_lid_state;

// Timer Globals
unsigned long lastDebounceTime = 0;   // the last time the output pin was toggled
unsigned long debounceDelay = 50;     // the debounce time; increase if the output flickers
unsigned long lastTransmitTime = 0;   // The last time a serial transmission was sent
unsigned long transmitDelay = 100;


void setup() {
  // Start serial line at 9600
  Serial.begin(9600);

  // Set pins 13 and 3 as output and input, respectively
  pinMode(Led,OUTPUT);
  pinMode(buttonpin,INPUT);

  // Initialize the lid
  // Debounce the hall sensor on pin 3
  reading = digitalRead(buttonpin);
  last_lid_state = reading;
//  lastDebounceTime = millis();

//  //This will not work
//  while((millis()-lastDebounceTime) < debounceDelay)
//  {
//    reading = digitalRead(buttonpin);
//    if(reading != last_lid_state)
//      lastDebounceTime = millis();
//  }
//
//  // Adopt
//  last_lid_state = reading;

  // Set the LED
  digitalWrite(Led, last_lid_state);
  
  if(last_lid_state)
    Serial.print("c\n");
  else
    Serial.print("o\n");


}


void loop() {
  // Debounce the hall sensor on pin 3
  reading = digitalRead(buttonpin);
  
  if(reading != last_reading)
    lastDebounceTime = millis();

  // If debounce delay has passed
  if((millis() - lastDebounceTime) > debounceDelay)
  {
    // And the states still disagree
    if(reading != last_lid_state)
      // Adopt the new state
      last_lid_state = reading;
      //Set the LED
      digitalWrite(Led, last_lid_state);
  }

  // If the transmission delay has passed
  if((millis() - lastTransmitTime) > transmitDelay)
  {
    // Send the established state
    if(last_lid_state)
      Serial.print("c\n");
    else
      Serial.print("o\n");

    // Reset the last send time
    lastTransmitTime = millis();
  }

  last_reading = reading;
}
