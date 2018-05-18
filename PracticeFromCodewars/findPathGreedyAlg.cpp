#include <string>
#include <cmath>

using namespace std;

inline int distance(int, int, int);

bool path_finder(string maze)
{
    // TODO: Determine whether one can reach the exit at (n - 1, n - 1)
    // starting from (0, 0) in a n × n maze (represented as a string)
    // and return a boolean value accordingly

    // cout << maze << endl;
    int n(0);
    for (n = 0; maze[n] != '\n' && maze[n] != '\0'; ++n)
    {
    }
    int **aMaze = new int *[n];
    int **aMark = new int *[n];
    for (int i = 0; i < n; ++i)
    {
        aMaze[i] = new int[n];
        aMark[i] = new int[n];
    }
    for (int i = 0, j = 0, k = 0; maze[i] != '\0'; ++i)
    {
        if (maze[i] == '\n')
        {
            ++j;
            k = 0;
            continue;
        }
        if (maze[i] == '.')
        {
            aMaze[j][k] = 0;
            aMark[j][k] = -1;
            k++;
        }
        else
        {
            aMaze[j][k] = 1;
            aMark[j][k] = -1;
            k++;
        }
    }
    aMark[0][0] = n * n;
    int flag = 0;
    // cout << n << endl;
    // for (int i = 0; i < n; ++i)
    // {
    //     for (int j = 0; j < n; ++j)
    //     {
    //         cout << aMaze[i][j];
    //     }
    //     cout << endl;
    // }
    while (flag >= 0)
    {
        if (flag / n == n - 1 && flag % n == n - 1)
        {
            return true;
        }
        int y = flag % n;
        int x = flag / n;
        int min = n * n;
        int nt(0);
        int ty(0), tx(0);
        // cout << x << '\t' << y << '\t' << flag << endl;
        if (y - 1 >= 0 && aMaze[x][y - 1] != 1 && aMark[x][y - 1] < 0)
        {
            // cout << "left" << endl;
            nt = distance(n, x, y - 1);
            if (nt < min)
            {
                min = nt;
                tx = x;
                ty = y - 1;
            }
        }
        if (x - 1 >= 0 && aMaze[x - 1][y] != 1 && aMark[x - 1][y] < 0)
        {
            // cout << "up" << endl;
            nt = distance(n, x - 1, y);
            if (nt < min)
            {
                min = nt;
                tx = x - 1;
                ty = y;
            }
        }
        if (y + 1 <= n - 1 && aMaze[x][y + 1] != 1 && aMark[x][y + 1] < 0)
        {
            // cout << "right" << endl;
            nt = distance(n, x, y + 1);
            if (nt < min)
            {
                min = nt;
                tx = x;
                ty = y + 1;
            }
            // cout << tx * n + ty << endl;
        }
        if (x + 1 <= n - 1 && aMaze[x + 1][y] != 1 && aMark[x + 1][y] < 0)
        {
            // cout << "low" << endl;
            nt = distance(n, x + 1, y);
            if (nt < min)
            {
                min = nt;
                tx = x + 1;
                ty = y;
            }
        }
        if (min != n * n)
        {
            aMark[tx][ty] = flag;
            flag = tx * n + ty;
        }
        else if(flag != 0)
        {
            flag = aMark[flag / n][flag % n];
        }
        else
        {
            return false;
        }
    }
    return false;
}

inline int distance(int n, int x, int y)
{
    return (abs(n - 1 - x) + abs(n - 1 - y));
}
