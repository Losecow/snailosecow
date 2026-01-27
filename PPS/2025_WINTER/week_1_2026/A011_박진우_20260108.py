def solution(N, stages):
    stage_counts = [0] * (N + 2)

    # 각 스테이지에 멈춘 사람 수
    for stage in stages:
        stage_counts[stage] += 1

    result = []
    total_players = len(stages)

    for stage in range(1, N + 1):
        if total_players > 0:
            fail_rate = stage_counts[stage] / total_players
            result.append((stage, fail_rate))
            total_players -= stage_counts[stage]
        else:
            result.append((stage, 0))

    result.sort(key=lambda x: (-x[1], x[0]))

    answer = [stage for stage, fail in result]

    return answer