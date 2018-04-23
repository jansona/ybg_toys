#include <stdio.h>
#include <stdlib.h>
#include <process.h>
#include <windows.h>
#include "snake.h"
#include "gameUI.h"
#include "control.h"


int main()
{
    extern int stop;
    extern int speed;
    homePage();
    while(!stop)
    {
        keybordHit();
        go();
        drawSnake();
        Sleep(speed);
    }
    return 0;
}
