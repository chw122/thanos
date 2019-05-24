#include <SoftwareSerial.h>
 
int blueTx=10;
int blueRx=11;
SoftwareSerial mySerial(blueTx, blueRx);
 
void setup() 
{
  Serial.begin(9600);
  mySerial.begin(9600);
}
void loop()
{
  if (mySerial.available()) {       
    Serial.write(mySerial.read());
  }
  if (Serial.available()) {         
    mySerial.write(Serial.read());
  }
}
