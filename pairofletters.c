/*How many pairs of letters are there in the word HYPERTHYROIDISM which have the same
number of letters between them as in English alphabet*/

#include <stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
int main()
{
    char str[80]="HYPERTHYROIDISM";
    int i,j,p=0,q=0,count=0,k;
    int a[50],b[50];
    for(i=0;i<strlen(str);i++)
    {
        for(j=0;j<strlen(str);j++)
        {
            for(k=0;k<p;k++){
            if((i-j-1==abs((str[i]+65)-(str[j]+65)))&&(i!=j)&&(a[k]!=b[k]))
            count++;
            a[p++]=i;
            b[q++]=j;}
        }
    }
    printf("%d",count);
    return 0;
}
