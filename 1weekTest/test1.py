def solution(progresses, speeds):
    r = []  # 100% 완료 상태까지 도달하는 시간
    c = 1
    answer = []
    for i in range(len(progresses)):
        for j in range(1000):
            if progresses[i] + (j * speeds[i]) >= 100:
                r.append(j)  # r:[5,10,1,1,20,1]
                break
    for k in range(len(r)-1):  # 0~5
        if r[k] >= r[k+1]:  # [5,10,1,1,20,1]
            c += 1
        else:
            answer.append(c)  # answer[1,3]
            c = 1
    answer.append(c)
    return answer

### 시간상의 문제 (코드는 돌아감)###
##########################################
### 시간 해결 ###
def solution(progresses, speeds):
    answer = []  # return 값
    time = 0  # n일간의 작업 시간
    count = 0  # 작업 시간 카운트

    while len(progresses) > 0:  # progresses의 배열값이 0보다 클때 p=[93,30,55] -> 3
        if (progresses[0] + time*speeds[0]) >= 100:  # 93 + time * 1 >= 100
            progresses.pop(0)  # p=[30,55]
            speeds.pop(0)  # s=[30,5]
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1  # 7번 올라가야 if문에 도달함
    answer.append(count)
    return answer
