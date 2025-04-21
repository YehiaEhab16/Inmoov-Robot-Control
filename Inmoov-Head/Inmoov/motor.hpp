/******************************************************************************************/
/*********************** Project: Inmoov Head                       ***********************/
/*********************** Version: 1.7                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 11/01/2025                          ***********************/
/******************************************************************************************/

#ifndef MOTOR_H_
#define MOTOR_H_

#include <Arduino.h>
#include "ServoEasing.h"
#include "config.h"

class InmoovServo 
{
  int pin;             // Servo Pin
  int position;        // Servo Postion
  int minAngle;        // Minimum angle
  int maxAngle;        // Maximum angle
  bool isReversed;     // is reversed
  bool easing;         // Easing type
  ServoEasing servo;   // Servo object  

  public:
    /**
    *@def inmoov servo class constructor
    */ 
    InmoovServo(int pin, int position, int minAngle, int maxAngle, bool isReversed, bool easing);
    
    /**
    *@def initialize servos
    */ 
    void init(void);

    /**
    *@def move servos to specific angle
    */ 
    void moveServo(int targetAngle);

    /**
    *@def increment / decrement servo angle
    *@return if step is valid
    */ 
    bool moveServo(bool increment);

};

#endif