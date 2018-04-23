#include <stdio.h>
#include <stdlib.h>
#include "xor.h"

int main()
{
    char key = '&';
    int ctrl = 0;
    wchar_t safety = '0';
    //scanf("%c", &key);

    /**********************************************************
    出于某种未知的原因，或许是位宽的差异，每次将符合要求
    的字符safety转换为整形ctrl时，会产生两个数进入输入流。
    如，safety若为‘2’，则会产生0 2两个数，但低位2在前，先
    进入scanf（）语句。若要观察此现象，可将自注释段上的语
    句 fflush(stdin) 屏蔽。
    ***********************************************************/
    printf("欢迎使用XOR型数据加密/解密软件Console版，此版本仅支持对应于ASCII表中元素的操作，建议不要使用其他\
\文字系统，否则将数据错乱或无法实现加密。\n");
    printf("请输入加密/解密时使用的密钥（单字符）：");
    scanf("%c", &key);
    MARK:
    fflush(stdin);
    printf("此软件具有四种工作模式:\n");
    printf("1. c2c \n2. c2f(newdata.txt) \n3. f2c(origindata.txt) \n4. f2f \n5. 退出\n");
    printf("请输入对应编号并以回车键(\\n)结束：");
    scanf("%c", &safety);
    if((safety<='z' && safety>='a') || (safety<='Z' && safety>='A'))
    {
        printf("\nfuck off\n");
        exit(0);
    }
    ctrl = (long)_wtoi(&safety);
    //printf("%d\n", ctrl);
    switch(ctrl)
    {
        case 1: xor_c2c(key); goto MARK;
        case 2: xor_c2f(key); goto MARK;
        case 3: xor_f2c(key); goto MARK;
        case 4: xor_f2f(key); goto MARK;
        case 5: break;
        default : printf("\n输入项与选项不匹配，请重新输入。\n\n"); goto MARK;
    }
    return 0;
}
