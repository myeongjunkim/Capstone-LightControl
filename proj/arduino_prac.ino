#include <Servo.h>


Servo servo;
Servo servo2;

int value = 0;
int value2 = 0;
int data;



void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  servo.attach(5);
  servo2.attach(3);



}

void loop() {
  // put your main code here, to run repeatedly:

  while(Serial.available()) {
    data = Serial.read();
  }

  if (data == '1'){
    value = 45;
    servo.write(value);
    delay(500);

    value2 = 45;
    servo2.write(value2);
    delay(500);
    
  }
  if (data== '0') {
    value = 135;
    servo.write(value);
    delay(500);

    value2 = 135;
    servo2.write(value2);
    delay(500);
  }

 


}

 
 
