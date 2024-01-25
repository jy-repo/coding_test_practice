def solution(sequence, k):

    current_best = []

    # 길이 짧은게 우선순위
    # 인덱스 앞쪽이 우선순위

    sidx = 0    # start index
    eidx = 0    # end   index
    csum = 0    # current sum
    tsum = k    # target  sum

    best_sidx = -1
    best_eidx = -1

    while True:

        if csum < tsum:
            eidx += 1
        elif csum > tsum:
            sidx += 1
        else:
            

            
        

 
    return [0, 0]

if __name__ == "__main__":
    sequence = [1,2,3,4,5]
    sequence = [1,1,1,2,3,4,5]
    k = 7
    k = 5
    answer = solution(sequence, k)
