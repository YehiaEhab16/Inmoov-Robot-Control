/******************************************************************************************/
/*********************** Project: Inmoov Arm                        ***********************/
/*********************** Version: 1.5                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 03/12/2024                          ***********************/
/******************************************************************************************/

#include "motor.hpp"

InmoovServo::InmoovServo(int pin, int position, int minAngle, int maxAngle, bool isReversed, bool easing) : pin(pin), position(position), minAngle(minAngle), maxAngle(maxAngle), isReversed(isReversed), easing(easing) {}

// Init Motor
void InmoovServo::init(void)
{
  if(isReversed) position = 180 - position;
  servo.attach(pin, position); 
  servo.setEasingType(EASE_TYPE);          
  servo.setSpeed(EASE_SPEED);
}

// Move servo to specific angle
void InmoovServo::moveServo(int targetAngle)
{
  if(targetAngle < minAngle) targetAngle = minAngle; else if(targetAngle > maxAngle) targetAngle = maxAngle;
  if(isReversed) position = 180 - targetAngle; else position = targetAngle;
  if(easing) servo.startEaseTo(position); else servo.write(position);
}

// Increment / decrement servo angle
bool InmoovServo::moveServo(bool increment)
{
  if((increment && isReversed && 180-position<maxAngle) || (!increment && !isReversed && position>minAngle)) 
    {servo.write(--position); return true;}

  else if((increment && !isReversed && position<maxAngle) || (!increment && isReversed && 180-position>minAngle)) 
    {servo.write(++position); return true;}

  else return false;
}
