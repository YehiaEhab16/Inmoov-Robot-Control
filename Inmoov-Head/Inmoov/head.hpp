/******************************************************************************************/
/*********************** Project: Inmoov Head                       ***********************/
/*********************** Version: 1.7                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 11/01/2025                          ***********************/
/******************************************************************************************/

#ifndef HEAD_H_
#define HEAD_H_

#include "motor.hpp"
#include "config.h"

class InmoovHead
{
    bool jawDir = true;
    int prevX, prevY, prevPot;

    InmoovServo servoNeck         = { SERVO_NECK_PIN,           NECK_INIT_POS,   NECK_MIN,   NECK_MAX,   SERVO_NECK_DIR,           SERVO_NECK_EASE     };
    InmoovServo servoJaw          = { SERVO_JAW_PIN,            JAW_INIT_POS,    JAW_MIN,    JAW_MAX,    SERVO_JAW_DIR,            SERVO_JAW_EASE      };
    InmoovServo servoEyesHor      = { SERVO_EYES_HOR_PIN,       EYES_H_INIT_POS, EYES_H_MIN, EYES_H_MAX, SERVO_EYES_VER_DIR,       SERVO_EYES_VER_EASE };
    InmoovServo servoEyesVer      = { SERVO_EYES_VER_PIN,       EYES_V_INIT_POS, EYES_V_MIN, EYES_V_MAX, SERVO_EYES_HOR_DIR,       SERVO_EYES_HOR_EASE };
    InmoovServo servoLidRightUp   = { SERVO_LID_RIGHT_UP_PIN,   LID_INIT_POS,    LID_MIN,    LID_MAX,    SERVO_LID_RIGHT_UP_DIR,   SERVO_LID_EASE      };
    InmoovServo servoLidRightDown = { SERVO_LID_RIGHT_DOWN_PIN, LID_INIT_POS,    LID_MIN,    LID_MAX,    SERVO_LID_RIGHT_DOWN_DIR, SERVO_LID_EASE      };
    InmoovServo servoLidLeftUp    = { SERVO_LID_LEFT_UP_PIN,    LID_INIT_POS,    LID_MIN,    LID_MAX,    SERVO_LID_LEFT_UP_DIR,    SERVO_LID_EASE      };
    InmoovServo servoLidLeftDown  = { SERVO_LID_LEFT_DOWN_PIN,  LID_INIT_POS,    LID_MIN,    LID_MAX,    SERVO_LID_LEFT_DOWN_DIR,  SERVO_LID_EASE      };

    public:
        /**
        *@def init head
        */
        void init(void);

        /**
        *@def move neck servo
        *@param dir required direction
        *@param angle required angle
        */ 
        void moveNeck(char dir, int angle);

        /**
        *@def move jaw servo
        *@param dir required direction
        *@param angle required angle
        */ 
        void moveJaw(char dir, int angle);

        /**
        *@def move eye lids
        *@param dir required direction
        *@param angle required angle
        */ 
        void moveLid(char dir, int angle);

        /**
        *@def move eyes servos
        *@param dir required direction
        *@param angle required angle
        */ 
        void moveEyes(char dir, int angle);

        /**
        *@def sweep eyes servos
        */ 
        void sweepEyes(void);

        /**
        *@def sweep jaw servo
        *@param dir required direction
        */ 
        void speak(bool dir = true);

        /**
        *@def eye mechanism function
        */
        bool eyeMechanism(void);
};

#endif 