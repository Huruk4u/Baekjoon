def solution(s):
    for length in range(len(s), 1, -1):
        print(length)
        for i in range(len(s) - length + 1):
            # print("\n팰린드롬 검사")
            flag = True
            for ptr in range(length // 2):
                # print(i + ptr)
                # print("%d vs %d : %s vs %s" % (i+ptr, i+length - ptr-1, s[i+ptr], s[i+length - ptr-1]))
                if s[i + ptr] != s[i + length - ptr -1]:
                    flag = False
                    break
            
            if flag:
                return length

    return 1