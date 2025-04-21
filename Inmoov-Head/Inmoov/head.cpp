/******************************************************************************************/
/*********************** Project: Inmoov Head                       ***********************/
/*********************** Version: 1.7                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 11/01/2025                          ***********************/
/******************************************************************************************/

#include "head.hpp"


// Move Neck Servo
void InmoovHead::init(void)
{
  // Initialize previous readings
  prevX = map(analogRead(ANALOG_X), ANALOG_MIN, ANALOG_MAX, EYES_H_MIN, EYES_H_MAX);
  prevY = map(analogRead(ANALOG_Y), ANALOG_MIN, ANALOG_MAX, EYES_V_MIN, EYES_V_MAX);
  prevPot = constrain(map(analogRead(ANALOG_TRIM), POT_MIN, POT_MAX, POT_SENS_MIN, POT_SENS_MAX), POT_SENS_MIN, POT_SENS_MAX);
  
  // Initialize Servos
  servoNeck.init();       servoJaw.init();           servoEyesHor.init();   servoEyesVer.init();
  servoLidRightUp.init(); servoLidRightDown.init();  servoLidLeftUp.init(); servoLidLeftDown.init();
}

// Move Neck Servo
void InmoovHead::moveNeck(char dir, int angle)
{
  if(dir==COMM_NECK_RIGHT)      servoNeck.moveServo(INCREMENT);
  else if(dir==COMM_NECK_LEFT)  servoNeck.moveServo(DECREMENT);
  else if(dir==COMM_NECK_ANGLE) servoNeck.moveServo(angle);
}

// Move Jaw Servo
void InmoovHead::moveJaw(char dir, int angle)
{
  if(dir==COMM_JAW_UP)         servoJaw.moveServo(INCREMENT);
  else if(dir==COMM_JAW_DOWN)  servoJaw.moveServo(DECREMENT);
  else if(dir==COMM_JAW_ANGLE) servoJaw.moveServo(angle);
}

// Move 3 servo lids
void InmoovHead::moveLid(char dir, int angle)
{
  if(dir==COMM_LID_OPEN)       {servoLidRightUp.moveServo(DECREMENT); servoLidRightDown.moveServo(DECREMENT); servoLidLeftUp.moveServo(DECREMENT); servoLidLeftDown.moveServo(DECREMENT);}
  else if(dir==COMM_LID_CLOSE) {servoLidRightUp.moveServo(INCREMENT); servoLidRightDown.moveServo(INCREMENT); servoLidLeftUp.moveServo(INCREMENT); servoLidLeftDown.moveServo(INCREMENT);}
  else if(dir==COMM_LID_ANGLE) {servoLidRightUp.moveServo(angle);     servoLidRightDown.moveServo(angle);     servoLidLeftUp.moveServo(angle);     servoLidLeftDown.moveServo(angle);}
}

// Move Eyes Servos
void InmoovHead::moveEyes(char dir, int angle)
{
  if(dir==COMM_EYES_UP)             servoEyesVer.moveServo(INCREMENT);
  else if(dir==COMM_EYES_DOWN)      servoEyesVer.moveServo(DECREMENT);
  else if(dir==COMM_EYES_RIGHT)     servoEyesHor.moveServo(DECREMENT);
  else if(dir==COMM_EYES_LEFT)      servoEyesHor.moveServo(INCREMENT);
  else if(dir==COMM_EYES_HOR_ANGLE) servoEyesHor.moveServo(angle);    
  else if(dir==COMM_EYES_VER_ANGLE) servoEyesVer.moveServo(angle);    
}

// Sweep Eyes Servos
void InmoovHead::sweepEyes(void)
{
  // Right and left sweep
  for(int i=EYES_H_INIT_POS;i<=EYES_H_MAX;i++) {servoEyesHor.moveServo(i); delay(STEP_DELAY);}
  delay(EYES_DELAY);
  for(int i=EYES_H_MAX;i>=EYES_H_MIN;i--)      {servoEyesHor.moveServo(i); delay(STEP_DELAY);}
  delay(EYES_DELAY);
  for(int i=EYES_H_MIN;i<=EYES_H_INIT_POS;i++) {servoEyesHor.moveServo(i); delay(STEP_DELAY);}
}

// Sweep Jaw servos
void InmoovHead::speak(bool dir = true)
{
    if(!dir) servoJaw.moveServo(JAW_MIN);
    else {if(jawDir && !servoJaw.moveServo(INCREMENT)) jawDir=false;  else if(!servoJaw.moveServo(DECREMENT)) jawDir=true;}
}

// Eye mechanism function
bool InmoovHead::eyeMechanism(void)
{
  // Read Horizontal - Vertical - Potentiometer values 
  int eyesAngleHor = map(analogRead(ANALOG_X), ANALOG_MIN, ANALOG_MAX, EYES_H_MIN, EYES_H_MAX);
  int eyesAngleVer = map(analogRead(ANALOG_Y), ANALOG_MIN, ANALOG_MAX, EYES_V_MIN, EYES_V_MAX);
  int trimMapped = constrain(map(analogRead(ANALOG_TRIM), POT_MIN, POT_MAX, POT_SENS_MIN, POT_SENS_MAX), POT_SENS_MIN, POT_SENS_MAX);

  // Check if values is above threshold
  if(abs(prevX-eyesAngleHor)>THRESHOLD || abs(prevY-eyesAngleVer)>THRESHOLD || abs(prevPot-trimMapped)>THRESHOLD) 
  {
    // Move to desired angles
    servoEyesHor.moveServo(eyesAngleHor);
    servoEyesVer.moveServo(eyesAngleVer);
    moveLid(COMM_LID_ANGLE, trimMapped - map(eyesAngleVer, EYES_V_MIN, EYES_V_MAX, -POT_SENS, POT_SENS));
    prevX = eyesAngleHor; prevY = eyesAngleVer; prevPot = trimMapped; 
    return true;
  }

  else return false;
}
