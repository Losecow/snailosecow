// #include <stdio.h>
// #include <string.h>

// int main(){
	
// 	int n;
// 	char a[51];
// 	int num = 0;
	
// 	scanf("%d",&n);
	
// 	for(int i = 0; i < n; i++){
// 		scanf("%s", a);
// 		num = 0;
		
// 		for(int j = 0; j < strlen(a); j++){
// 			if(num < 0) break;
			
// 			if(a[j] == '(')
// 				num++;
// 			if(a[j] == ')')
// 				num--;
// 		}
// 		if(num == 0) printf("YES\n");
// 		else printf("NO\n");
// 	}
	
// 	return 0;
// }

// 이중반복문으로 해결

// 스택으로 해결

#include <stdio.h>

char stack[50]; // 스택
int top = 0; 

int isVPS(char *);

void push(char);
char pop();
int isEmpty();

int main() {
	int t;
	char str[51];

	int i;
	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%s", str);

		if (isVPS(str))
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

int isVPS(char *str) {
	int result = 1;

	for (int i = 0; str[i]; i++) {
		if (str[i] == '(') {
			push(str[i]);
		}
		else {
			if (isEmpty()) { // + 주어진 문자열의 시작이 ) 일때 걸러주는 역할
				result = 0;
				break;
			}
			else
				pop();
		}
	}
	if (!isEmpty())
		result = 0;
	while (!isEmpty()) {
		pop();
	}
	return result;
}

void push(char c) {
	stack[top++] = c; // [1] 부터 저장
}

char pop() {
	return stack[--top];
}

int isEmpty() {
	return top == 0;
}

