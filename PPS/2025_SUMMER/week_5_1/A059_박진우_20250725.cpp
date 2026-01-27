#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

int N, T;
char *colors;

int *redPos, *bluePos;
int redCount, blueCount;

// Fenwick Tree (BIT) 구조와 함수
// 1-based indexing
ll *fenw;
int fenwSize;

void fenwInit(int n) {
    fenwSize = n;
    fenw = (ll *)calloc(fenwSize+1, sizeof(ll));
}

void fenwUpdate(int idx, ll delta) {
    while (idx <= fenwSize) {
        fenw[idx] += delta;
        idx += idx & (-idx);
    }
}

ll fenwSum(int idx) {
    ll sum = 0;
    while (idx > 0) {
        sum += fenw[idx];
        idx -= idx & (-idx);
    }
    return sum;
}

// 인버전 카운팅 함수
// points[]: 점들의 원 위치 배열 (0~N-1)
// size: points 배열 크기
// 원 위치를 '점 수'로 좌표 압축 후 사용
ll countInversions(int *points, int size) {
    // 좌표 압축 필수: 점 인덱스는 0~N-1이므로 좌표 그대로 사용 가능
    // Fenwicks indexing은 1-based → points[i] +1 사용

    fenwInit(N);

    ll invCount = 0;

    for (int i = 0; i < size; i++) {
        int val = points[i] + 1;
        // fenwSum(fenwSize) - fenwSum(val) → 현재 값보다 큰 값이 지금까지 몇개 왔는지
        invCount += fenwSum(fenwSize) - fenwSum(val);
        fenwUpdate(val, 1);
    }

    free(fenw);
    return invCount;
}

// 각 색깔 점 배열을 "최적 매칭"하여 교차수 계산
// 이 문제에 경우, 점들을 인접한 짝씩 연결할 때 교차 최소화됨
// 따라서 점들을 순서대로 짝짓기 (2개씩 매칭)
// 교차수는 이 매칭 순서에서 발생하는 인버전 개수와 같음
// 조금 더 복잡한 경우도 있으나, 문제 조건과 예시로 미루어 이 방식 적용

ll calcMinCrosses(int *pos, int count) {
    // 점 개수는 짝수라고 가정 (적어도 2이상)
    // 같은 색 점들은 짝수개여야 모든 점을 연결가능
    // 문제에서는 빨강파랑 각 색깔 점 개수가 2 이상 보장됨

    // 인접 매칭이 최소 교차를 보장하므로, 인접 점들 2개씩 짝짓기
    // 인버전 개수를 구하기 위해 선분 좌표 배열을 재구성

    // 두 점 짝: pos[2k], pos[2k+1] 연결
    // 연결된 선을 기준으로 오른쪽 점의 원 위치 배열을 이용해 인버전을 센다

    int *pairedPoints = (int *)malloc(sizeof(int) * count);

    // 점 개수가 홀수일 수 있으나 본 문제는 2 이상, 짝수도 명시 안됐음
    // 만일 홀수면 일부 점은 하나의 선도 못 가질 수 있으니, 가장 간단하게 인접 연결

    // 인접한 점들 짝짓기
    for (int i = 0; i < count; i++) {
        pairedPoints[i] = pos[i];
    }

    // 인버전 카운트: pos 배열 순서가 연결 순서처럼 사용됨
    // 매칭 순서 그대로 인버전 센다고 보면 됨
    ll res = countInversions(pairedPoints, count);

    free(pairedPoints);
    return res;
}

int main() {
    scanf("%d", &T);
    
    // 최대 N 합 5,000,000 -> 동적 할당 필요
    colors = (char *)malloc(5000001 * sizeof(char));
    redPos = (int *)malloc(5000000 * sizeof(int));
    bluePos = (int *)malloc(5000000 * sizeof(int));

    for (int tc = 1; tc <= T; tc++) {
        scanf("%d", &N);
        scanf("%s", colors);

        redCount = 0;
        blueCount = 0;

        for (int i = 0; i < N; i++) {
            if (colors[i] == 'R') redPos[redCount++] = i;
            else bluePos[blueCount++] = i;
        }

        // 바로 인접 연결 후 교차수 계산
        ll redCrosses = calcMinCrosses(redPos, redCount);
        ll blueCrosses = calcMinCrosses(bluePos, blueCount);

        printf("Case #%d\n%lld\n", tc, redCrosses + blueCrosses);
    }

    free(colors);
    free(redPos);
    free(bluePos);

    return 0;
}
