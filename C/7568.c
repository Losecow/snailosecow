#include <stdio.h>

int main(){
	int n;
	int kg[51];
	int cm[51];
	
	scanf("%d",&n);
	
	for(int i = 0; i < n; i++){
		scanf("%d %d",&kg[i], &cm[i]);
	}
	
	int kgN, cmN;
	int cnt = 0;
	int ccc[51];
	
	for(int i = 0; i < n; i++){
		kgN = kg[i];
		cmN = cm[i];
		for(int j = 0; j < n; j++){
			if(kg[j] > kgN && cm[j] > cmN){
				cnt++;
			}
		}
		ccc[i] = cnt;
		cnt = 0;
	}
	
	for(int i = 0; i < n; i++){
		printf("%d ",ccc[i] + 1);
	}
	
	return 0;
}