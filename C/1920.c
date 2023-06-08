#include <stdio.h>
#include <stdlib.h>

int compare(const void *first, const void *second){
	return *(int*)first > *(int*)second ? : (*(int*)first < *(int*)second ? -1 : 0);
}

int binary_search(int arr[], int num, int size){
	int front, rear, pivot;
	front = 0;
	rear = size - 1;
	while(1) {
		pivot = (front + rear) / 2;
		if(arr[pivot] == num) return 1;
		if(arr[front] == num) return 1;
		if(arr[rear] == num) return 1;
		
		if(arr[pivot] < num) // 수열의 중간에 위치하는 수가 구하고자 하는 수보다 작을 때
			front = pivot + 1; // 첫번째 수는 중간의 수 + 1 번째 수가 된다
		else
			rear = pivot - 1; // 수열의 중간에 위치하는 수가 구하고자 하는 수보다 클 때 
							  // 마지막 수는 중간의 수 - 1 번쨰 수가 된다.
		if (front >= rear) // 수열의 첫번째 수와 마지막 수의 번호가 같거나 첫번째 수의 번호가 더 클 때 반복문 종료
			return 0;
	}
}

int main(){
    int n;
    scanf("%d",&n);
    int *arr1 = (int*)malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
        scanf("%d", &arr1[i]);
    }
    
    int m;
    scanf("%d",&m);
    int *arr2 = (int*)malloc(m * sizeof(int));
    
    for(int i = 0; i < m; i++){
        scanf("%d",&arr2[i]);
    }
    
    qsort(arr1, n, sizeof(int), compare);
    
    for(int i = 0; i < m; i++){
        printf("%d\n", binary_search(arr1, arr2[i], n));
    }
	
	return 0;
}

// 이진 탐색 트리 c 로 구현
// 이진 탐색 트리 자료 https://cjh5414.github.io/binary-search/
// 코드 가져온 블로그 주소 https://daydreamx.tistory.com/entry/baekjoon1920
// 이진 탐색 트리 문제