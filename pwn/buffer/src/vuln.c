#include <stdio.h>

int main(){
	char a=0;
	char buf[10];
	printf("What's your name: ");
	fgets(buf,20,stdin);
	if(a!=0){
		system("/bin/sh");		
	}
	printf("HELLO CTF!, %s\n",buf);
	return 0;
}