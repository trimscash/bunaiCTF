#include <stdio.h>
#include <string.h>

char encycripted[]="\xa\x14\x17\x8\x1\x2a\x2d\x27\x13\x29\x4d\x39\x38\x30\x26\x22\x58\x25\x3c\x36\x3a\x2c\x4d\x25\x21\x2f\x3e\x48\x49\x14\x79\x61";


int main(){
        //char flag[100]="bunaiCTF{H4PPY_C0DE_RE4DING!!}";
        char key[100]="happy christmas!";
        char d[100]="";
        char e[100]="";
        int len=30;
//      for(int i=0;i<len;i++){
//              e[i]=key[(i*i)%strlen(key)]^flag[i];
//              printf("\\x%x",e[i]);
//      }

        for(int i=0;i<len;i++){
                d[i]=key[(i*i)%strlen(key)]^encycripted[i];
        }

//      printf("%s",d);
        return 0;
}
