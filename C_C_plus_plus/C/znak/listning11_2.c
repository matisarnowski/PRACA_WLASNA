#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define TRUE  1

int main(){
	char buf[1];
	scanf("%s", buf);

	while(TRUE){
		if (isdigit(buf[0])>=TRUE){
			printf("To jest cyfra.");
			if (isxdigit(buf[0])>=TRUE){
				printf("To jest być może liczba szensastkowa...");
				break;
			}
			break;
		}
		else if (isalpha(buf[0])>=TRUE){
			printf("To jest litera");
			if (isxdigit(buf[0])>=TRUE){
				printf("To jest być może liczba szensastkowa...");
				break;
			}
			break;
		}	
		else if (isupper(buf[0])>=TRUE){
			printf("To jest wielka litera...");
			if (isxdigit(buf[0])>=TRUE){
				printf("To jest być może liczba szensastkowa...");
				break;
			}
			break;
		}
		
		else {
			printf("Nierozponano...");
			break;
		}
	}
	return 0;
}
