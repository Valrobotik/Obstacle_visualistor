/**
 * \file serial_utils.h
 * \brief Functions to read serial
 * \author Cyril Tessier
 * \version 0.1
 *
 * \details
 * This file contains useful functions for reading the serial port and then converting the received data.
 */

#include "Arduino.h"

#ifndef SERIAL_UTILS
#define SERIAL_UTILS


/**
 * @brief      Serial event function.
 * Function enable to read serial port.
 *
 * @return     string read from serial
 */
String serial_event();

#endif