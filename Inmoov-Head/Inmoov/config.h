/******************************************************************************************/
/*********************** Project: Inmoov Head                       ***********************/
/*********************** Version: 1.7                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 11/01/2025                          ***********************/
/******************************************************************************************/

#ifndef CONFIG_H_
#define CONFIG_H_

// Servo Pins
#define SERVO_NECK_PIN             4
#define SERVO_JAW_PIN              5
#define SERVO_EYES_VER_PIN         6
#define SERVO_EYES_HOR_PIN         7
#define SERVO_LID_RIGHT_UP_PIN     8
#define SERVO_LID_RIGHT_DOWN_PIN   9
#define SERVO_LID_LEFT_UP_PIN      10
#define SERVO_LID_LEFT_DOWN_PIN    11

// Analog Pins
#define ANALOG_X                   A0
#define ANALOG_Y                   A1
#define ANALOG_TRIM                A2

// Servo Minimum Positions  
#define NECK_MIN                   0                          
#define JAW_MIN                    0                           
#define LID_MIN                    0
#define EYES_H_MIN                 30                           
#define EYES_V_MIN                 60
    
// Servo Maximum Positions     
#define NECK_MAX                   180                         
#define JAW_MAX                    90                           
#define LID_MAX                    80
#define EYES_H_MAX                 150                           
#define EYES_V_MAX                 120

// Servo Initial Position (All servos are mounted at minimum except for: NECK, EYES_HORIZONTAL, EYES_VERTCIAL -> Mounted at middle) 
#define JAW_INIT_POS               JAW_MIN           
#define LID_INIT_POS               LID_MIN  
#define NECK_INIT_POS              ( NECK_MIN   + NECK_MAX   ) / 2
#define EYES_H_INIT_POS            ( EYES_H_MIN + EYES_H_MAX ) / 2
#define EYES_V_INIT_POS            ( EYES_V_MIN + EYES_V_MAX ) / 2

// Servo Direction
#define SERVO_NECK_DIR             NORMAL
#define SERVO_JAW_DIR              NORMAL
#define SERVO_EYES_VER_DIR         NORMAL
#define SERVO_EYES_HOR_DIR         NORMAL
#define SERVO_LID_RIGHT_UP_DIR     REVERSED
#define SERVO_LID_RIGHT_DOWN_DIR   NORMAL
#define SERVO_LID_LEFT_UP_DIR      NORMAL
#define SERVO_LID_LEFT_DOWN_DIR    REVERSED

// Servo Easing Configuration
#define SERVO_JAW_EASE             true
#define SERVO_NECK_EASE            true
#define SERVO_LID_EASE             true
#define SERVO_EYES_VER_EASE        true
#define SERVO_EYES_HOR_EASE        true

//Servo Step     
#define SERVO_STEP                 1

//Servo Easing Paramaters
#define ENABLE_EASE_QUADRATIC                           
#define EASE_TYPE                  EASE_QUADRATIC_OUT      
#define EASE_SPEED                 150                       
    
// Analog & Potentiometer Limits
#define POT_MIN                    0
#define POT_MAX                    200
#define POT_SENS                   10
#define POT_SENS_MIN               LID_MIN + POT_SENS
#define POT_SENS_MAX               LID_MAX - POT_SENS
#define ANALOG_MIN                 0
#define ANALOG_MAX                 1023
#define THRESHOLD                  5
     
//Communication Baud Rate    
#define COMM_BAUD_RATE             115200
     
//Duration     
#define SLEEP_TIME                 50000
#define EYES_DELAY                 500
#define STEP_DELAY                 5

// Servo direction constants
#define NORMAL                     false
#define REVERSED                   true
#define DECREMENT                  false
#define INCREMENT                  true
     
//Communication Parameters     
#define COMM_STOP                  'A'
#define COMM_NECK_RIGHT            'r'
#define COMM_NECK_LEFT             'l'
#define COMM_NECK_ANGLE            'N'
#define COMM_JAW_UP                'u'
#define COMM_JAW_DOWN              'd'
#define COMM_JAW_ANGLE             'J'
#define COMM_LID_OPEN              'O'
#define COMM_LID_CLOSE             'C'
#define COMM_LID_ANGLE             'a'
#define COMM_EYES_RIGHT            'R'
#define COMM_EYES_LEFT             'L'
#define COMM_EYES_HOR_ANGLE        'E'
#define COMM_EYES_UP               'U'
#define COMM_EYES_DOWN             'D'
#define COMM_EYES_VER_ANGLE        'e'
#define COMM_SPEAK                 'S'
#define COMM_END_SPEAK             's'

#endif