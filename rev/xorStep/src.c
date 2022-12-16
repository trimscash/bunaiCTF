#include <stdio.h>
#include <string.h>

//char encycripted=[]={0xa,0x14,0x1e,0x11,0x10,0x63,0x37,0x2e,0x9,0x21,0x47,0x24,0x3d,0x38,0x2c,0x79,0x58,0x33,0x2f,0x33,0x49,0x64,0x26,0x37,0x20,0x2c,0x47,0x30,0x24,0x2f,0x34,0x5c};
char encycripted[]="\xa\x14\x17\x8\x1\x2a\x2d\x27\x13\x29\x4d\x39\x38\x30\x26\x39\x58\x33\x26\x2a\x58\x2d\x3c\x3e\x3a\x24\x4d\x2d\x21\x27\x3e\x1c";

int main(){
//	char flag[100]="bunaiCTF{H4PPY_X0R_C0DE_RE4DING}";
	char key[100]="happy christmas!";
	char d[100]="";
	char e[100]="";
	int len=strlen(encycripted);
//	for(int i=0;i<len;i++){
//		e[i]=key[(i*i)%strlen(key)]^flag[i];
//		printf("\\x%x",e[i]);
//	}
	
	for(int i=0;i<len;i++){
		d[i]=key[(i*i)%strlen(key)]^encycripted[i];
	}
	
//	printf("%s",d);
	return 0;
}
