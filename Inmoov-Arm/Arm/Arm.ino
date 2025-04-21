/******************************************************************************************/
/*********************** Project: Inmoov Arm                        ***********************/
/*********************** Version: 1.5                               ***********************/
/*********************** Authors: Yehia Ehab                        ***********************/
/*********************** Date : 03/12/2024                          ***********************/
/******************************************************************************************/

#include "inmoov.hpp"
#include "ServoEasing.hpp"

// Data recieved from serial
volatile char data=COMM_STOP;

void setup(void)
{
  InitArm();
  Serial.begin(COMM_BAUD_RATE);
}

void loop(void)
{
  switch(data)
  {
    case COMM_THUMB_CONTRACT:  MoveFinger(THUMB,CONTRACT);  data=COMM_STOP; break;
    case COMM_THUMB_RELAX:     MoveFinger(THUMB,RELAX);     data=COMM_STOP; break;
    case COMM_INDEX_CONTRACT:  MoveFinger(INDEX,CONTRACT);  data=COMM_STOP; break;
    case COMM_INDEX_RELAX:     MoveFinger(INDEX,RELAX);     data=COMM_STOP; break;
    case COMM_MIDDLE_CONTRACT: MoveFinger(MIDDLE,CONTRACT); data=COMM_STOP; break;
    case COMM_MIDDLE_RELAX:    MoveFinger(MIDDLE,RELAX);    data=COMM_STOP; break;
    case COMM_RING_CONTRACT:   MoveFinger(RING,CONTRACT);   data=COMM_STOP; break;
    case COMM_RING_RELAX:      MoveFinger(RING,RELAX);      data=COMM_STOP; break;
    case COMM_LITTLE_CONTRACT: MoveFinger(LITTLE,CONTRACT); data=COMM_STOP; break;
    case COMM_LITTLE_RELAX:    MoveFinger(LITTLE,RELAX);    data=COMM_STOP; break;
    case COMM_WRIST_CONTRACT:  MoveFinger(WRIST,CONTRACT);  data=COMM_STOP; break;
    case COMM_WRIST_RELAX:     MoveFinger(WRIST,RELAX);     data=COMM_STOP; break;
    case COMM_THUMB_MAX:       MoveFinger(THUMB,MAX);       data=COMM_STOP; break;
    case COMM_THUMB_MIN:       MoveFinger(THUMB,MIN);       data=COMM_STOP; break;
    case COMM_INDEX_MAX:       MoveFinger(INDEX,MAX);       data=COMM_STOP; break;
    case COMM_INDEX_MIN:       MoveFinger(INDEX,MIN);       data=COMM_STOP; break;
    case COMM_MIDDLE_MAX:      MoveFinger(MIDDLE,MAX);      data=COMM_STOP; break;
    case COMM_MIDDLE_MIN:      MoveFinger(MIDDLE,MIN);      data=COMM_STOP; break;
    case COMM_RING_MAX:        MoveFinger(RING,MAX);        data=COMM_STOP; break;
    case COMM_RING_MIN:        MoveFinger(RING,MIN);        data=COMM_STOP; break;
    case COMM_LITTLE_MAX:      MoveFinger(LITTLE,MAX);      data=COMM_STOP; break;
    case COMM_LITTLE_MIN:      MoveFinger(LITTLE,MIN);      data=COMM_STOP; break;
    case COMM_WRIST_MAX:       MoveFinger(WRIST,MAX);       data=COMM_STOP; break;
    case COMM_WRIST_MIN:       MoveFinger(WRIST,MIN);       data=COMM_STOP; break;
  }
}

// Serial Interrupt
void serialEvent(void)
{
  data = (char)Serial.read();  // Read data
  Serial.print(data);
}
