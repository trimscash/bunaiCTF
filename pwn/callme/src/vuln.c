#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>

__attribute__((constructor)) void setup() {
	alarm(60);
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
}

void callme(){
	system("/bin/sh");
}

int main(){
	char buf[10];
	puts("Hi! Whats up:");
	fgets(buf,199,stdin);
	printf("if you have any question, pls call me! %s!",buf);
	return 0;
}


