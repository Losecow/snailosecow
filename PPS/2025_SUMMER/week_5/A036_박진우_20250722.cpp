#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); // 빠른 입력

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int N;
        cin >> N;

        int result = 0;
        for (int i = 0; i < N; ++i)
        {
            int x;
            cin >> x;
            result ^= x; // XOR 누적
        }

        cout << "Case #" << t << '\n';
        cout << result << '\n';
    }

    return 0;
}