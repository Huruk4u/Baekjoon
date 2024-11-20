def solution(scores):
    target_att, target_rel = scores[0]

    scores.sort(key=lambda x: (-x[0], x[1]))
    max_rel, answer = 0, 1
    for att, rel in scores:
        if att > target_att and rel > target_rel:
            return -1
        
        if max_rel <= rel:
            max_rel = rel
            if att + rel > target_att + target_rel:
                answer += 1
                
    return answer
        