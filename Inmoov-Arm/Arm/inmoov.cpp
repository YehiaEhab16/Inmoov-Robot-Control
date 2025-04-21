/******************************************************************************************/
/*********************** Project: Inmoov Arm                        ***********************/
/*********************** Version: 1.5                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 03/12/2024                          ***********************/
/******************************************************************************************/

#include "inmoov.hpp"
#include <Arduino.h>

// Motors Initialization
void InitArm(void)
{
  // Attach Servos
  servoThumb.attach(SERVO_THUMB, thumbPos);
  servoThumb.setEasingType(EASE_TYPE);
  

  servoIndex.attach(SERVO_INDEX, indexPos);
  servoIndex.setEasingType(EASE_TYPE);

  servoMiddle.attach(SERVO_MIDDLE, middlePos);
  servoMiddle.setEasingType(EASE_TYPE);


  servoRing.attach(SERVO_RING, ringPos);
  servoRing.setEasingType(EASE_TYPE);

  servoLittle.attach(SERVO_LITTLE, littlePos);
  servoLittle.setEasingType(EASE_TYPE);

  servoWrist.attach(SERVO_WRIST, wristPos);
  servoWrist.setEasingType(EASE_TYPE);

  setSpeedForAllServos(EASE_SPEED);
}

// Move Fingers
void MoveFinger(int finger,int dir)
{
  switch(finger)
  {
    case THUMB:   if(dir==CONTRACT)   {if(thumbPos<MAX_POS_THUMB)   {thumbPos+=SERVO_STEP;servoThumb.write(thumbPos);}}
                  else if(dir==RELAX) {if(thumbPos>MIN_POS_THUMB)   {thumbPos-=SERVO_STEP;servoThumb.write(thumbPos);}}
                  else if(dir==MAX)   {thumbPos=MAX_POS_THUMB; servoThumb.startEaseTo(thumbPos);}
                  else if(dir==MIN)   {thumbPos=MIN_POS_THUMB; servoThumb.startEaseTo(thumbPos);}  break;

    case INDEX:   if(dir==CONTRACT)   {if(indexPos<MAX_POS_INDEX)   {indexPos+=SERVO_STEP;servoIndex.write(indexPos);}}
                  else if(dir==RELAX) {if(indexPos>MIN_POS_INDEX)   {indexPos-=SERVO_STEP;servoIndex.write(indexPos);}} 
                  else if(dir==MAX)   {indexPos=MAX_POS_INDEX; servoIndex.startEaseTo(indexPos);}
                  else if(dir==MIN)   {indexPos=MIN_POS_INDEX; servoIndex.startEaseTo(indexPos);}  break;

    case MIDDLE:  if(dir==CONTRACT)   {if(middlePos<MAX_POS_MIDDLE) {middlePos+=SERVO_STEP;servoMiddle.write(middlePos);}}
                  else if(dir==RELAX) {if(middlePos>MIN_POS_MIDDLE) {middlePos-=SERVO_STEP;servoMiddle.write(middlePos);}}
                  else if(dir==MAX)   {middlePos=MAX_POS_MIDDLE; servoMiddle.startEaseTo(middlePos);}
                  else if(dir==MIN)   {middlePos=MIN_POS_MIDDLE; servoMiddle.startEaseTo(middlePos);}  break;

    case RING:    if(dir==CONTRACT)   {if(ringPos<MAX_POS_RING)     {ringPos+=SERVO_STEP;  servoRing.write(ringPos);}} 
                  else if(dir==RELAX) {if(ringPos>MIN_POS_RING)     {ringPos-=SERVO_STEP;  servoRing.write(ringPos);}} 
                  else if(dir==MAX)   {ringPos=MAX_POS_RING; servoRing.startEaseTo(ringPos);}
                  else if(dir==MIN)   {ringPos=MIN_POS_RING; servoRing.startEaseTo(ringPos);}  break;

    case LITTLE:  if(dir==CONTRACT)   {if(littlePos<MAX_POS_LITTLE) {littlePos+=SERVO_STEP;servoLittle.write(littlePos);}}
                  else if(dir==RELAX) {if(littlePos>MIN_POS_LITTLE) {littlePos-=SERVO_STEP;servoLittle.write(littlePos);}}
                  else if(dir==MAX)   {littlePos=MAX_POS_LITTLE; servoLittle.startEaseTo(littlePos);}
                  else if(dir==MIN)   {littlePos=MIN_POS_LITTLE; servoLittle.startEaseTo(littlePos);}  break;

    case WRIST :  if(dir==CONTRACT)   {if(wristPos<MAX_POS_WRIST) {wristPos+=SERVO_STEP;servoWrist.write(wristPos);}}
                  else if(dir==RELAX) {if(wristPos>MIN_POS_WRIST) {wristPos-=SERVO_STEP;servoWrist.write(wristPos);}}
                  else if(dir==MAX)   {wristPos=MAX_POS_WRIST; servoWrist.startEaseTo(wristPos);}
                  else if(dir==MIN)   {wristPos=MIN_POS_WRIST; servoWrist.startEaseTo(wristPos);}  break;
  }
}