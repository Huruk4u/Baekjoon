import sys, re
from collections import deque


def solution(word, pages):
    dict_site, score, graph = dict(), dict(), dict()
    word = word.lower()
    # page 정리
    for page in pages:
        page = page.lower()

        domain = re.search('<meta property=\"og:url\" content=\"https://([\S]+)\".*/>', page).group(1)
        out_link = re.findall('<a href=\"https://([\S]+)\">', page)

        basic_score = 0
        for string in re.findall('[a-z]+', page):
            if string == word:
                basic_score += 1

        dict_site[domain] = [basic_score, len(out_link)]
        graph[domain] = out_link
        score[domain] = float(basic_score)

    for node, linked_node in graph.items():
        for next in linked_node:
            if next not in dict_site:
                continue
            link_score = dict_site[node][0] / dict_site[node][1]
            score[next] += link_score

    idx, max_score, answer = 0, 0, 0
    for n, sc in score.items():
        if sc > max_score:
            max_score = sc
            answer = idx
        idx += 1

    return answer
