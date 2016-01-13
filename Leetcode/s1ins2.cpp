#include <stdio.h>
#include <string.h>

int main(){
	int i = 0; j = 0, position = 0;
	char s1[100], s2[50], s3[50];
	scanf(%s, s1);
	scanf(%s, s2);

	while(s1[j] != '\0'){
		if ((s1[j] == s2[i]) && (s2[i] != '\0')){
			i ++;
			j ++;
		} else {
			j++;
		}
		if(s2[i] == '\0'){
			occur ++;
			i = 0;
		}
	}
}