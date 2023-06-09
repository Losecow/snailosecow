#include <iostream>
#include <stdlib.h>
#include <queue>

using namespace std;

int main(){
    queue<int> q;
    int n;
    int temp, num;
    scanf("%d",&n);

    for(int i = 1; i <= n; i++){
        q.push(i);
    }

    while(q.size() > 1){ // 사이즈도 있다!!! queue !!!!
        q.pop();
        temp = q.front();
        q.push(temp);
        q.pop();
    }

    printf("%d\n",q.front());

    return 0;
}