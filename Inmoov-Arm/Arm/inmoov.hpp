/******************************************************************************************/
/*********************** Project: Inmoov Arm                        ***********************/
/*********************** Version: 1.5                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 03/12/2024                          ***********************/
/******************************************************************************************/

#ifndef INMOOV_H_
#define INMOOV_H_

#include "motor.hpp"
#include "config.h"

class InmoovArm
{
    InmoovServo servoThumb  = { SERVO_THUMB_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };
    InmoovServo servoIndex  = { SERVO_INDEX_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };
    InmoovServo servoMiddle = { SERVO_MIDDLE_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };
    InmoovServo servoRing   = { SERVO_RING_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };
    InmoovServo servoLittle = { SERVO_INDEX_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };
    InmoovServo servoWrist  = { SERVO_WRIST_PIN, NECK_INIT_POS, NECK_MIN, NECK_MAX, SERVO_NECK_DIR, SERVO_NECK_EASE };

    public:
        /**
         *@def motors initiaization
        */ 
        void init(void);

        /**
         *@def move finger 
        *@param movement required motion
        */ 
        void moveFinger(char movement);
}


#endif 
