#include <stdio.h>

int main() {
	int n = 0;
	int m = 0;
	
	int arr1[n];
	int arr2[m];
	int arr3[m];
	
	scanf("%d",&n);
	for(int i = 0; i < n; i++) scanf("%d",&arr1[i]);
	
	scanf("%d",&m);
	for(int i = 0; i < n; i++) scanf("%d",&arr2[i]);
	
	for(int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			if(arr2[i] == arr1[j]) arr3[i]++;
		}
		printf("%d\n",arr3[i]);
	}
	
	
	return 0;
	
}

// https://kbw1101.tistory.com/27