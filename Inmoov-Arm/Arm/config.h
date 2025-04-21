/******************************************************************************************/
/*********************** Project: Inmoov Arm                        ***********************/
/*********************** Version: 1.5                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 03/12/2024                          ***********************/
/******************************************************************************************/

#ifndef CONFIG_H_
#define CONFIG_H_

//Servo Pins
#define SERVO_THUMB_PIN       4
#define SERVO_INDEX_PIN       5
#define SERVO_MIDDLE_PIN      6
#define SERVO_RING_PIN        7
#define SERVO_LITTLE_PIN      8
#define SERVO_WRIST_PIN       9

//Servo Minimum Positions
#define MIN_POS_THUMB         0
#define MIN_POS_INDEX         0
#define MIN_POS_MIDDLE        0
#define MIN_POS_RING          0
#define MIN_POS_LITTLE        0
#define MIN_POS_WRIST         0

//Servo Maximum Positions
#define MAX_POS_THUMB         90
#define MAX_POS_INDEX         90
#define MAX_POS_MIDDLE        90
#define MAX_POS_RING          90
#define MAX_POS_LITTLE        90
#define MAX_POS_WRIST         90

//Servo Initial Positions
#define INIT_POS_THUMB        MIN_POS_THUMB
#define INIT_POS_INDEX        MIN_POS_INDEX
#define INIT_POS_MIDDLE       MIN_POS_MIDDLE
#define INIT_POS_RING         MIN_POS_RING
#define INIT_POS_LITTLE       MIN_POS_LITTLE
#define INIT_POS_WRIST        MIN_POS_WRIST

// Servo Directions
#define SERVO_THUMB_DIR       NORMAL
#define SERVO_INDEX_DIR       NORMAL
#define SERVO_MIDDLE_DIR      NORMAL
#define SERVO_RING_DIR        NORMAL
#define SERVO_LITTLE_DIR      NORMAL
#define SERVO_WRIST_DIR       NORMAL

// Servo Step     
#define SERVO_STEP            1

// Servo Easing Configuration
#define SERVO_MOTORS_EASE     true
#define ENABLE_EASE_QUADRATIC                           
#define EASE_TYPE             EASE_QUADRATIC_OUT      
#define EASE_SPEED            150                       
     
//Communication Baud Rate    
#define COMM_BAUD_RATE        115200
     
// Servo direction constants
#define NORMAL                false
#define REVERSED              true
#define DECREMENT             false
#define INCREMENT             true
     
//Communication Parameters
#define COMM_STOP             'Z'
#define COMM_THUMB_CONTRACT   'T'
#define COMM_THUMB_RELAX      't' 
#define COMM_INDEX_CONTRACT   'I'
#define COMM_INDEX_RELAX      'i'
#define COMM_MIDDLE_CONTRACT  'M'
#define COMM_MIDDLE_RELAX     'm'
#define COMM_RING_CONTRACT    'R'
#define COMM_RING_RELAX       'r'
#define COMM_LITTLE_CONTRACT  'L'
#define COMM_LITTLE_RELAX     'l'
#define COMM_WRIST_CONTRACT   'Y'
#define COMM_WRIST_RELAX      'y'
#define COMM_THUMB_MAX        'A'
#define COMM_THUMB_MIN        'a' 
#define COMM_INDEX_MAX        'B'
#define COMM_INDEX_MIN        'b'
#define COMM_MIDDLE_MAX       'C'
#define COMM_MIDDLE_MIN       'c'
#define COMM_RING_MAX         'D'
#define COMM_RING_MIN         'd'
#define COMM_LITTLE_MAX       'E'
#define COMM_LITTLE_MIN       'e'
#define COMM_WRIST_MAX        'F'
#define COMM_WRIST_MIN        'f'

#endif