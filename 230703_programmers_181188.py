
def solution(targets):

    answer = 0

    targets = sorted(targets, key=lambda x: x[0])

    print(targets)

    groupings_count = 0

    overlap_e = 0
    i = 1
    for s, e in targets:
        
        if overlap_e <= s:
            overlap_e = e
            groupings_count += 1
        else:
            overlap_e = min(overlap_e, e)


    return answer

if __name__ == "__main__":
    targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	
    answer = solution(targets)
    print(answer)