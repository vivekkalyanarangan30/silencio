#include <Keyboard.h>

//Pin 3 for input button
//Pin 2 output for controlling LED
int ButtonValue = 0;
int LEDValue = 0;
int Button = 3;
int LED = 2;
int x;
int meeting_id = 2;
void setup() {
  Keyboard.begin();
  
  // put your setup code here, to run once:
  pinMode(Button, INPUT);
  pinMode(LED, OUTPUT);

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  ButtonValue = digitalRead(Button);

  if(ButtonValue != 0){
    LEDValue = digitalRead(LED);

    if(meeting_id == 0){
      gmeetMute();
      }
    else if(meeting_id == 2){
      teamsMute();
      }
    else if(meeting_id == 4){
      zoomMute();
      }

    if(LEDValue == LOW){
        digitalWrite(LED, HIGH);
        Serial.print("On");
        delay(500); 
      }else{
        digitalWrite(LED, LOW);
        Serial.print("Off");
        delay(500);
      }
  }

  if(Serial.available()){
    switch(Serial.read()){
      case '0': digitalWrite(LED, LOW); meeting_id = 0;
                break;
      case '1': digitalWrite(LED, HIGH); meeting_id = 0;
                break;

      case '2': digitalWrite(LED, LOW);  meeting_id = 2;
                break;
      case '3': digitalWrite(LED, HIGH);  meeting_id = 2;
                break;

      case '4': digitalWrite(LED, LOW);  meeting_id = 4;
                break;
      case '5': digitalWrite(LED, HIGH);  meeting_id = 4;
                break;
    }
  }

}

void zoomMute()
{
  Keyboard.press(KEY_LEFT_GUI);     
  Keyboard.press(KEY_LEFT_SHIFT);
  Keyboard.press('a');
  delay(100);
  Keyboard.releaseAll();
}

void teamsMute()
{
  Keyboard.press(KEY_LEFT_GUI);     
  Keyboard.press(KEY_LEFT_SHIFT);
  Keyboard.press('m');
  delay(100);
  Keyboard.releaseAll();
}

void gmeetMute()
{
  Keyboard.press(KEY_LEFT_GUI);     
  Keyboard.press('d');
  delay(100);
  Keyboard.releaseAll();
}
