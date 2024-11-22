def solution(words, queries):
    answer = []

    tree = dict()
    tree_rev = dict()
    for word in words:
        if len(word) not in tree:
            tree[len(word)] = [0, dict()]
            tree_rev[len(word)] = [0, dict()]

        curr = tree[len(word)]
        for i in range(len(word)):
            cnt_word, dict_word = curr
            if word[i] not in curr[1]:
                dict_word[word[i]] = [0, dict()]
            curr[0] += 1
            curr = curr[1][word[i]]

        curr = tree_rev[len(word)]
        for i in range(len(word) - 1, -1, -1):
            cnt_word, dict_word = curr
            if word[i] not in curr[1]:
                dict_word[word[i]] = [0, dict()]
            curr[0] += 1
            curr = curr[1][word[i]]

    result = []
    for query in queries:
        # ?????
        if query[0] == '?' and query[-1] == '?':
            if len(query) not in tree:
                result.append(0)
            else:
                result.append(tree[len(query)][0])
        # ---??
        elif query[-1] == '?':
            if len(query) not in tree:
                result.append(0)
                continue
            curr = tree[len(query)]
            rtn = 0
            for i in range(len(query)):
                # print()
                # print(query[i], curr)
                if query[i] == '?':
                    break
                if query[i] not in curr[1]:
                    rtn = 0
                    break
                curr = curr[1][query[i]]
                rtn = curr[0]
            result.append(rtn)
        # ???--
        else:
            if len(query) not in tree_rev:
                result.append(0)
                continue
            curr = tree_rev[len(query)]
            rtn = 0
            for i in range(len(query)-1, -1, -1):
                if query[i] == '?':
                    break
                if query[i] not in curr[1]:
                    rtn = 0
                    break
                curr = curr[1][query[i]]
                rtn = curr[0]
            result.append(rtn)

    return result