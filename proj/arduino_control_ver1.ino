
#include <Servo.h>

// 서보모터의 제어핀이 연결되는 핀번호입니다.
#define   PIN_SERVO_1   5
#define   PIN_SERVO_2   3


// 서보모터의 각도변화를 천천히주기위해 감속개념을 사용해요. 감속개념을 구현한 부분에 사용되는 값입니다.
#define   CONST_MAX_SERVOGEAR    20000


Servo servo1 = Servo(PIN_SERVO_1);  // 세타 값
Servo servo2 = Servo(PIN_SERVO_2);  // r 값

String line;
float data1;
float data2;

void setup() {
    Serial.begin(9600);
  // 서보모터의 제어신호를 생성하는 핀을 정의해요.
    servo1.attach(PIN_SERVO_1);
    servo1.attach(PIN_SERVO_2);

  
}

void loop() {
    while(Serial.available()){
        line = Serial.read();

        int first = line.indexOf(",");// 첫 번째 콤마 위치
        int length = line.length(); // 문자열 길이
        
        data1 = line.substring(0, first).toFloat(); 
        data2 = line.substring(first+1, length).toFloat();
        
        servo1.write(data1);
        servo2.write(data2);

        delay(20);
    }



    
}
