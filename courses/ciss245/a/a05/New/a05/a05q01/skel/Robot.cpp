/*********************************************************************
File : Robot.cpp
Author: smaug
Implementation of functions prototypes in Robot.h.
*********************************************************************/
#include <iostream>
#include "Robot.h"
void init(Robot & r, char name, int x, int y, int energylevel)
{
r.name = name;
r.x = x;
r.y = y;
r.energylevel = energylevel;
}
