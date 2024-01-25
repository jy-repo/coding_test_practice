# 가장 많이 받은 선물

friends1 = ["muzi", "ryan", "frodo", "neo"]
friends2 = ["joy", "brad", "alessandro", "conan", "david"]
friends3 = ["a", "b", "c"]

gifts1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
gifts2 = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
gifts3 = ["a b", "b a", "c a", "a c", "a c", "c a"]

import itertools

def solution(friends, gifts):

    matrix = {(f1, f2): 0 for f1 in friends for f2 in friends}
    gifts_gave = {friend: 0 for friend in friends}
    gifts_recieved = {friend: 0 for friend in friends}

    for gift in gifts:

        g_fr, g_to = gift.split(" ")
        key = (g_fr, g_to)
        gifts_gave[g_fr] += 1
        gifts_recieved[g_to] += 1
        matrix[key] += 1
    
    gifts_to_recieve = {friend: 0 for friend in friends}

    for f1, f2 in itertools.combinations(friends, 2):

        if matrix[(f1, f2)] > matrix[(f2, f1)]:
            gifts_to_recieve[f1] += 1
        elif matrix[(f1, f2)] < matrix[(f2, f1)]:
            gifts_to_recieve[f2] += 1
        else:
            f1_gift_point = gifts_gave[f1] - gifts_recieved[f1]
            f2_gift_point = gifts_gave[f2] - gifts_recieved[f2]
            if f1_gift_point > f2_gift_point:
                gifts_to_recieve[f1] += 1
            elif f1_gift_point < f2_gift_point:
                gifts_to_recieve[f2] += 1
            else:
                pass

    max_gifts_recieved_count = gifts_to_recieve[max(gifts_to_recieve, key=gifts_to_recieve.get)]

    return max_gifts_recieved_count

print(solution(friends3, gifts3))