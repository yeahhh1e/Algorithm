def solution(array):
    max_v = array[0]
    m_i = 0
    for i in range(len(array)):
        if max_v < array[i]:
            max_v = array[i]
            m_i = i
    answer = [max_v, m_i]

    return answer