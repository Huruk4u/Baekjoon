import heapq


def solution(genres, plays):
    answer = []
    
    # 플레이 횟수 -> 장르
    playcnt_genres = dict()
    genres_playcnt = dict()
    genres_music = dict()
    
    N = len(genres)
    for i in range(N):
        if genres[i] not in genres_playcnt:
            genres_playcnt[genres[i]] = plays[i]
            genres_music[genres[i]] = [(-plays[i], i)]
        else:
            genres_playcnt[genres[i]] += plays[i]
            heapq.heappush(genres_music[genres[i]], (-plays[i], i))
            
    playcnt = []
    for key, value in genres_playcnt.items():
        playcnt.append(value)
        playcnt_genres[value] = key
    
    playcnt.sort(reverse = True)
    for cnt in playcnt:
        music_list = genres_music[playcnt_genres[cnt]]
        answer.append(heapq.heappop(music_list)[1])
        if music_list: answer.append(heapq.heappop(music_list)[1])
        
    
    return answer