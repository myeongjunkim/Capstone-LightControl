#include <Servo.h>


Servo servo1;
Servo servo2;

int value = 0;
int value2 = 0;
int data;

String line;
float data1 = 90;
float data2 = 170;

int Laser_pin = 7;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  servo1.attach(5);
  servo2.attach(3);
  pinMode(Laser_pin, OUTPUT); 

  digitalWrite(Laser_pin, HIGH);


}

void loop() {
  // put your main code here, to run repeatedly:
  
  while(Serial.available()) {
    line = Serial.readStringUntil('\n');
  }
  
  int first = line.indexOf(",");// 첫 번째 콤마 위치
  int len = line.length(); // 문자열 길이
  
  data1 = line.substring(0, first).toFloat(); 
  data2 = line.substring(first+1, len).toFloat();
    
  if (data1>170){
    data1 = 170;
  } else if (data1<0){
    data1 = 0;
  }

  if (data2>170){
    data2 = 170;
  } else if (data2<0){
    data2 = 0;
  }

  // 분기 처리 한번 진행
  
  servo1.write(data1);
  servo2.write(data2);
    
  
  


}

 
 
