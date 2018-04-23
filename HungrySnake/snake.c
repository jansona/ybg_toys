#include "snake.h"
#include <stdlib.h>

int stop = 0;
int score = 0;

void initSnake(void)
{
    int i;
    pSnake = (snake * )malloc(sizeof(snake));
    pFood = (food * )malloc(sizeof(food));
    pSnake->len = 5;
    pSnake->dir = RIGHT;
    for(i = 2; i <= pSnake->len + 2; i++)
        addNode(i, 2);
}

void addNode(int x, int y)
{
    node * newnode = (node * )malloc(sizeof(node));
    node * p = pNode;
    newnode->pNext = pNode;
    newnode->x = x;
    newnode->y = y;
    pNode = newnode;
    if(x < 2 || x >= WIDTH || y < 2 || y >= HEIGH)
    {
        stop = 1;
        gotoXY(10, 19);
        printf("over\n");
        getch();
        free(pNode);
        free(pSnake);
        exit(0);
    }
    while( p != NULL)
    {
        if(p->pNext != NULL)
            if((p->x == x) && (p->y == y))
            {
                stop = 0;
                gotoXY(10, 19);
                printf("over!\n");
                _getch();
                free(pNode);
                free(pSnake);
                exit(0);
            }
        p = p->pNext;
    }
}

void initFood(void)
{
    node * p = pNode;
    int mark = 1;
    srand((unsigned)time(NULL));
    while(1)
    {
        pFood->x = rand()%(WIDTH - 2) + 2;
        pFood->y = rand()%(HEIGH - 2) + 2;
        while(p != NULL)
        {
            if((pFood->x == p->x) && (pFood->y == p->y))
            {
                mark = 0;
                break;
            }
            p = p->pNext;
        }
        if(mark == 1)
        {
            gotoXY(pFood->x, pFood->y);
            printf("%c", 3);
            break;
        }
        mark = 1;
        p = pNode;
    }
}

void addTail(void)
{
    node * newnode = (node * )malloc(sizeof(node));
    node * p = pNode;
    pTail->pNext = newnode;
    newnode->x = 50;
    newnode->y = 20;
    newnode->pNext = NULL;
    pTail = newnode;
}

void eatFood(void)
{
    addTail();
    score++;
}
