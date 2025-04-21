/******************************************************************************************/
/*********************** Project: Inmoov Head                       ***********************/
/*********************** Version: 1.7                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 11/01/2025                          ***********************/
/******************************************************************************************/

#include "ServoEasing.hpp"
#include "head.hpp"

bool speakFlag;              // Speak flag
volatile char data;          // Recieved data from serial
volatile String angle;       // Recieved angle from serial
volatile int targetAngle;     // Recieved angles from serial
unsigned long currentTime;   // Time for sleep mode

InmoovHead inmoov;

void setup(void)
{
  // Initialization
  Serial.begin(COMM_BAUD_RATE);
  inmoov.init();
  currentTime = millis();
}

void loop(void)
{
  // Sleep Mode (Take Action every SLEEP_TIME (50s))
  if(millis()-currentTime>SLEEP_TIME) {inmoov.sweepEyes(); currentTime = millis();}
  // Speak if flag is set
  if(speakFlag) inmoov.speak();
  // Eye mechanism
  if(inmoov.eyeMechanism()) currentTime = millis();
	// Communication States
  switch (data) 
  {
    case COMM_END_SPEAK:  speakFlag=false; inmoov.speak(speakFlag);  currentTime = millis(); data=COMM_STOP; break;
    case COMM_SPEAK:      speakFlag=true;                            currentTime = millis(); data=COMM_STOP; break;
    case COMM_JAW_UP:     case COMM_JAW_DOWN:                        inmoov.moveJaw(data, targetAngle);  currentTime = millis(); data=COMM_STOP; break;
    case COMM_NECK_RIGHT: case COMM_NECK_LEFT: case COMM_NECK_ANGLE: inmoov.moveNeck(data, targetAngle); currentTime = millis(); data=COMM_STOP; break;
    case COMM_LID_OPEN:   case COMM_LID_CLOSE: case COMM_LID_ANGLE:  inmoov.moveLid(data, targetAngle);  currentTime = millis(); data=COMM_STOP; break;
    case COMM_EYES_RIGHT: case COMM_EYES_LEFT: case COMM_EYES_UP: case COMM_EYES_DOWN: case COMM_EYES_HOR_ANGLE: case COMM_EYES_VER_ANGLE: inmoov.moveEyes(data, targetAngle); currentTime = millis(); data=COMM_STOP; break;
  }
}

// Serial Interrupt
void serialEvent()
{
  char recieved = Serial.read();
  if(recieved >= '0' && recieved <= '9') angle += recieved;
  else {targetAngle = atoi(angle.c_str()); angle=""; data = recieved;}                                   
}