#include <windows.h>
#include <conio.h>
#include "gameUI.h"

void homePage(void)
{
    int i = 0;
    hideCursor();
    printf("----------------------------------------\n");
    for(i = 0; i < 10; i++)
    {
        printf("|\t\t\t\t       |\n");
    }
    printf("----------------------------------------\n");
    gotoXY(5, 13);
    printf("任意键开始");
    _getch();         //这里的使用不是很确定，标记一下。已确定，不可用getchar（）
    initSnake();
    initFood();
    gotoXY(5, 13);
    printf("                                        ");
}

void hideCursor(void)
{
    CONSOLE_CURSOR_INFO cursorInfo = {1, 0};
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
}

void gotoXY(int x, int y)
{
    COORD pos;
    pos.X = x - 1;
    pos.Y = y - 1;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}
