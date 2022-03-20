def solution(bridge_length, weight, truck_weights):
    answer = 0 # 걸린 시간
    c = 0 #들어가는 트럭 차례
    right = [] # 지나간 트럭
    center = [0] # 지나는 트럭
    while len(center): # 1
        answer += 1 # 4
        if c < len(truck_weights): # 0 < 1
            if sum(center) < weight: # 4 < 10
                center.append(truck_weights[c]) #  c:[,4,5]
                truck_weights.pop(c) # t:[,,5,6]
                c += 1 # 2
            else:
                right.append(center.pop(1)) # r:[7] 
                c -= 1 # 1
        else:
            break
    
    return answer

##########################################################
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 걸린 시간 초 
    trucks_on_bridge = [0] * bridge_length # 다리 길이
    while len(trucks_on_bridge): # 지나갈 트럭이 있을때까지
        answer += 1 # 반복마다 1초씩 증가
        trucks_on_bridge.pop(0) # 가장 앞에 있는 트럭 지나가기
        if truck_weights: # 트럭이 존재 할 때
            if sum(trucks_on_bridge) + truck_weights[0] <= weight: # 무게 초과
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer