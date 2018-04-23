#include "xor.h"
#include <stdio.h>
#include <string.h>

#define SIZE 1000000

//function 1
void xor_c2c(char key)
{
    char ctrl = 'r';
    char c_ori, c_new;
    while(ctrl != 'x')
    {
        fflush(stdin);  //进入此函数时遗留了main函数中在选择工作模式时键入的回车键
        printf("请输入待加密/解密的字符串，并以回车键(\\n)结束：");
        while((c_ori = getchar()) != '\n')
        {
            c_new = c_ori ^ key;
            if(isprint(c_new) && isprint(c_ori))
                putchar(c_new);
            else
                putchar(c_ori);
        }
        printf("\n");
        printf("\n完成!\n按x退出或将继续在此模式下工作\n");
        scanf("%c",&ctrl);
        printf("\n");
    }
}

//function 2
void xor_c2f(char key)
{
    char c_ori, c_new;
    FILE * fp_new;
    fp_new = fopen(".\\newdata.txt", "w");
    fflush(stdin);
    printf("请输入待加密/解密的字符串，并以回车键(\\n)结束：");
    while((c_ori = getchar()) != '\n')
        {
            c_new = c_ori ^ key;
            if(isprint(c_new) && isprint(c_ori))
                fputc(c_new, fp_new);
            else
                fputc(c_ori, fp_new);
        }
    fclose(fp_new);
    printf("\n完成!\n\n");
}

//function 3
void xor_f2c(char key)
{
    char c_ori, c_new;
    FILE * fp_ori;
    fp_ori = fopen(".\\origindata.txt", "r");
    c_ori = fgetc(fp_ori);
    while(c_ori != EOF)
    {
        c_new = c_ori ^ key;
        if(isprint(c_new) && isprint(c_ori))
            putchar(c_new);
        else
            putchar(c_ori);
        c_ori = fgetc(fp_ori);
    }
    printf("\n");
    fclose(fp_ori);
    printf("\n完成!\n\n");
}

//function 4
void xor_f2f(char key)
{
    //char str_ori[SIZE], str_new[SIZE];
    char c_ori, c_new;
    //int i = 0;
    //int j = 0;
    //int flag = 0;
    FILE * fp_ori, * fp_new;
    fp_ori = fopen(".\\origindata.txt", "r");
    fp_new = fopen(".\\newdata.txt", "w");
//    fgets(str_ori, SIZE, fp_ori);         //失败，应当反思，不懂数据流造成的
//    printf("%s %c", str_ori, str_ori[1]);
//    char ch;
//    ch = fgetc(fp_ori);
//    while(ch!=EOF)
//    {
//        //putchar(ch);
//        ch = fgetc(fp_ori);
//    }
//    fread(str_ori, sizeof(char), SIZE, fp_ori);
//    for(i = 0; i < strlen(str_ori); i++)
//        if(str_ori[i] == '\n' && flag <= 2)
//        {
//            j++;
//            flag++;
//        }
//        else if(str_ori[i] == '\n')
//            flag++;
//        else
//            flag = 0;
//    str_ori[strlen(str_ori)-j] = '\0';
//    //printf("%s",str_ori);
//    for(i = 0; i < strlen(str_ori); i++)
//    {
//        if((c_ori = str_ori[i]) != EOF)
//            c_new = c_ori ^ key;
//        if(isprint(c_new) && isprint(c_ori))
//            str_new[i] = c_new;
//        else
//            str_new[i] = c_ori;
//    }
//    fp_ori++;
//    fscanf(fp_ori, "%c", &c_ori);
//    printf("wtf%c", c_ori);
//    str_new[i] = '\0';
//    fprintf(fp_new, "%s", str_new);
    c_ori = fgetc(fp_ori);
    while(c_ori != EOF)
    {
        c_new = c_ori ^ key;
        if(isprint(c_new) && isprint(c_ori))
            fputc(c_new, fp_new);
        else
            fputc(c_ori, fp_new);
        c_ori = fgetc(fp_ori);
    }
    fclose(fp_ori);
    fclose(fp_new);
    printf("\n完成!\n\n");
}
