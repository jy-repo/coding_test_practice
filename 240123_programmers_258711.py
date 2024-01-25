# 도넛과 막대 그래프

edges_test1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges_test2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

# 특징
# 막대 : 시작 vertex IN/OUT = 0/1
# 막대 : 중간 vertex IN/OUT = 1/1
# 막대 : 종료 vertex In/OUT = 1/0
# 막대1 : vertex IN/OUT = 0/0
# 도넛 : 시작 vertex IN/OUT = 1/1
# 도넛 : 중간 vertex IN/OUT = 1/1
# 도넛 : 종료 vertex IN/OUT = 1/1
# 8자 : 시작 vertex IN/OUT = 0/1

def solution(edges):

    # 나가고 들어오는 edge 연결 인덱스 생성
    edge_going_out_from_vertex = {}
    edge_coming_in_to_vertex = {}

    for edge_from, edge_to in edges:
        edge_going_out_from_vertex.setdefault(edge_from, []).append(edge_to)
        edge_going_out_from_vertex.setdefault(edge_to, [])  # 나가는게 없는 vertex 누락 방지
        edge_coming_in_to_vertex.setdefault(edge_to, []).append(edge_from)
        edge_coming_in_to_vertex.setdefault(edge_from, [])  # 둘어오는게 없는 vertex 누락 방지

    # 추가된 vertex : 무조건 1개는 있다는 가정하에 예외처리 스킵
    added_vertex = [v for v in edge_going_out_from_vertex if len(edge_going_out_from_vertex[v]) >= 2 and len(edge_coming_in_to_vertex[v]) == 0][0] 

    # 연결 인덱스 업데이트 (added vertex 제거)
    edge_going_out_from_vertex.pop(added_vertex) 
    edge_coming_in_to_vertex.pop(added_vertex)
    for vertex in edge_going_out_from_vertex:
        if added_vertex in edge_going_out_from_vertex[vertex]: edge_going_out_from_vertex[vertex].remove(added_vertex)
        if added_vertex in edge_coming_in_to_vertex[vertex]: edge_coming_in_to_vertex[vertex].remove(added_vertex)

    done = {}
    graphs = {
        'stick': [],
        'donut': [],
        'eight': []
    }

    for next_vertex in edge_going_out_from_vertex:

        if done.get(next_vertex, False): continue

        vertex_to_visit = [next_vertex]
        vertex_to_visit_d = {}
        vertex_visited  = {}

        is_stick_type = False
        is_eight_type = False        

        while vertex_to_visit:
            current_vertex = vertex_to_visit.pop(0)

            # 어떤 그래프 타입의 vertex 인지 추측
            if len(edge_going_out_from_vertex[current_vertex]) == 1 and len(edge_coming_in_to_vertex[current_vertex]) == 0:
                is_stick_type = True  # 막대형 그래프의 시작 vertex 만 가지는 특징
            elif len(edge_going_out_from_vertex[current_vertex]) == 0 and len(edge_coming_in_to_vertex[current_vertex]) == 1:
                is_stick_type = True  # 막대형 그래프의 마지막 vertex 만 가지는 특징
            elif len(edge_going_out_from_vertex[current_vertex]) == 0 and len(edge_coming_in_to_vertex[current_vertex]) == 0:
                is_stick_type = True  # 1 vertex 로 이루어진 막대형 그래프만 가지는 특징
            elif len(edge_going_out_from_vertex[current_vertex]) >= 2:
                is_eight_type = True  # 8자형 그래프에서만 1개 vertex 에서 2개 edge 가 출발함
            elif len(edge_coming_in_to_vertex[current_vertex]) >= 2:
                is_eight_type = True  # 8자형 그래프에서만 1개 vertex 에 2개 edge가 도착함
            else:
                pass  # 아직 모름

            # 다음 탐색 대상 가져오기
            for visit_candidate_vertex in edge_going_out_from_vertex[current_vertex]:
                if not vertex_visited.get(visit_candidate_vertex, False) and not vertex_to_visit_d.get(visit_candidate_vertex, False):
                    vertex_to_visit.append(visit_candidate_vertex)
                    vertex_to_visit_d[visit_candidate_vertex] = True
            for visit_candidate_vertex in edge_coming_in_to_vertex[current_vertex]:
                if not vertex_visited.get(visit_candidate_vertex, False) and not vertex_to_visit_d.get(visit_candidate_vertex, False):
                    vertex_to_visit.append(visit_candidate_vertex)
                    vertex_to_visit_d[visit_candidate_vertex] = True
            vertex_visited[current_vertex] = True

        # 이미 처리한 vertex 확인용 저장
        for vertex in vertex_visited:
            done[vertex] = True

        # 그래프 유형별로 저장
        if is_stick_type:
            graphs['stick'].append(vertex_visited)
        elif is_eight_type:
            graphs['eight'].append(vertex_visited)
        else:
            graphs['donut'].append(vertex_visited)
    
    answer = [added_vertex, len(graphs['donut']), len(graphs['stick']), len(graphs['eight'])]
    return answer

solution(edges_test2)