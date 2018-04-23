#include "control.h"
#include "snake.h"
#include <stdio.h>

int speed = 200;
int smark = 20;
extern int score;

void keybordHit(void)
{
    char ch;
    if(_kbhit())
    {
        ch = getch();
        switch(ch)
        {
            case 'W':
            case 'w':
                if(pSnake->dir == DOWN)
                    break;
                else
                    pSnake->dir = UP;
                break;
            case 'A':
            case 'a':
                if(pSnake->dir == RIGHT)
                    break;
                else
                    pSnake->dir = LEFT;
                break;
            case 'S':
            case 's':
                if(pSnake->dir == UP)
                    break;
                else
                    pSnake->dir = DOWN;
                break;
            case 'D':
            case 'd':
                if(pSnake->dir == LEFT)
                    break;
                else
                    pSnake->dir = RIGHT;
                break;
            case 'O':
            case 'o':
                if(speed >= 150)
                    speed -= 50;
                break;
            case 'P':
            case 'p':
                if(speed <= 400)
                    speed += 50;
                break;
            case ' ':
                gotoXY(15, 18);
                printf("pause");
                system("pause>nul");
                gotoXY(15, 18);
                printf("                                        ");
                break;
            default:
                break;
        }
    }
}

void go(void)
{
    node * q, * p = pNode;
    if(pSnake->dir == RIGHT)
    {
        addNode(p->x + 1, p->y);
        if(smark == 0)
        {
            while(p->pNext != NULL)
            {
                q = p;
                p=p->pNext;
            }
            q->pNext = NULL;
            free(p);
        }
    }
    if(pSnake->dir == LEFT)
    {
        addNode(p->x - 1, p->y);
        if(smark == 0)
        {
            while(p->pNext != NULL)
            {
                q = p;
                p=p->pNext;
            }
            q->pNext = NULL;
            free(p);
        }
    }
    if(pSnake->dir == UP)
    {
        addNode(p->x, p->y - 1);
        if(smark == 0)
        {
            while(p->pNext != NULL)
            {
                q = p;
                p=p->pNext;
            }
            q->pNext = NULL;
            free(p);
        }
    }
    if(pSnake->dir == DOWN)
    {
        addNode(p->x, p->y + 1);
        if(smark == 0)
        {
            while(p->pNext != NULL)
            {
                q = p;
                p=p->pNext;
            }
            q->pNext = NULL;
            free(p);
        }
    }
}

void drawSnake(void)
{
    node * p = pNode;
    while(p != NULL)
    {
        gotoXY(p->x, p->y);
        printf("%c", 2);
        pTail = p;
        p = p->pNext;
    }
    if(pNode->x == pFood->x && pNode->y == pFood->y)
    {
        smark = 1;
        eatFood();
        initFood();
    }
    if(smark == 0)
    {
        gotoXY(pTail->x, pTail->y);
        printf("%c", ' ');
    }
    else
    {
        gotoXY(pTail->x, pTail->y);
        printf("%c", ' ');
        smark = 0;
    }
    gotoXY(50, 20);
    printf("食物: %d, %d", pFood->x, pFood->y);
    gotoXY(50, 5);
    printf("分数: %d", score);
    gotoXY(50, 7);
    printf("速度: %d", speed);
    gotoXY(15, 14);
    printf("按o键加速");
    gotoXY(15, 15);
    printf("按p键减速");
    gotoXY(15, 16);
    printf("按空格键暂停");
}













