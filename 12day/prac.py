#############################################
# 12. 정렬
# 데이터를 순서대로 나열하는 방법
# 1. 버블정렬
# 버블 정렬은 첫 번째 자료와 두 번째 자료를,
# 두 번째 자료와 세 번째 자료를,
# 세 번째와 네 번째를, … 이런 식으로 (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬하는 방식입니다!
def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst
# 2. 선택정렬
# 한 데이터가 전체적으로 검사해서 제일 작은 숫자와 교체하는 형식


def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst
# 3. 삽입정렬
# 바로 뒤에있는 데이터가 작을시 앞쪽으로 보내주는형식


def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst


def insertionsort_2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val

    return lst
