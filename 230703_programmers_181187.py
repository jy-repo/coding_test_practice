import math
def solution(r1, r2):

    total = 0

    for i in range(-r2, r2+1):
        
        integer_points = 0

        # y=0
        if -r2 <= i <= -r1 or r1 <= i <= r2:
            integer_points += 1
        
        # y != 0
        r1_limit = 0 if abs(r1) < abs(i) else math.ceil(math.sqrt(r1**2 - i**2))
        r2_limit = math.floor(math.sqrt(r2**2 - i**2))
        integer_points += (r2_limit * 2) if r1_limit == 0 else (r2_limit - r1_limit + 1) * 2

        total += integer_points


    return total
        

if __name__ == "__main__":
    r1 = 2
    r2 = 3
    answer = solution(r1, r2)
    print(answer)