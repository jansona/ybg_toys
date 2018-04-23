#ifndef SNAKE_H_INCLUDED
#define SNAKE_H_INCLUDED

#define WIDTH 40
#define HEIGH 12



enum direction {LEFT, RIGHT, UP, DOWN};
struct structFood
{
    int x;
    int y;
};
typedef struct structFood food;
struct structNode       //…ﬂ…Ì
{
    int x;
    int y;
    struct structNode * pNext;
};
typedef struct structNode node;
struct structSnake
{
    int len;
    enum direction dir;
};
typedef struct structSnake snake;

food * pFood;
snake * pSnake;
node * pNode, * pTail;

void initSnake(void);
void addNode(int x, int y);
void initFood(void);
void addTail(void);
void eatFood(void);

#endif // SNAKE_H_INCLUDED
