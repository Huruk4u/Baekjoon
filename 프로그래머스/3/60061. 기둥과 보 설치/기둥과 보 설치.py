def solution(N, build_frame):

    def in_range(x, y):
        if (0 <= x < N + 1) and (0 <= y < N + 1):
            return True
        else:
            return False

    def exist(x, y, build_set):
        if not in_range(x, y):
            return False
        if (x, y) in build_set:
            return True
        else:
            return False

    def able_build(x, y, build_type):
        # 기둥 설치
        if build_type == 0:
            if y == 0 or exist(x - 1, y, floor) or exist(x, y, floor) or exist(x, y - 1, pillar):
                return True
            else:
                return False
        # 보 설치
        else:
            if exist(x, y - 1, pillar) or exist(x + 1, y - 1, pillar):
                return True
            if exist(x - 1, y, floor) and exist(x + 1, y, floor):
                return True

            return False

    def build(x, y, build_type, is_build):
        if build_type == 0:
            # 기둥 설치
            if is_build:
                if able_build(x, y, build_type):
                    pillar.add((x, y))
                    return
            # 기둥 삭제
            else:
                pillar.remove((x, y))
                if exist(x - 1, y + 1, floor) and not able_build(x - 1, y + 1, 1):
                    pillar.add((x, y))
                    return
                if exist(x, y + 1, floor) and not able_build(x, y + 1, 1):
                    pillar.add((x, y))
                    return
                if exist(x, y + 1, pillar) and not able_build(x, y + 1, 0):
                    pillar.add((x, y))
                    return

        else:
            # 보 설치
            if is_build:
                if able_build(x, y, build_type):
                    floor.add((x, y))
                    return
            # 보 삭제
            else:
                floor.remove((x, y))
                if exist(x - 1, y, floor) and not able_build(x - 1, y, 1):
                    floor.add((x, y))
                    return
                if exist(x + 1, y, floor) and not able_build(x + 1, y, 1):
                    floor.add((x, y))
                    return
                if exist(x, y, pillar) and not able_build(x, y, 0):
                    floor.add((x, y))
                    return
                if exist(x + 1, y, pillar) and not able_build(x + 1, y, 0):
                    floor.add((x, y))
                    return

    pillar = set()
    floor = set()
    for x, y, a, b in build_frame:
        build(x, y, a, b)

    answer = []
    for x, y in pillar:
        answer.append([x, y, 0])
    for x, y in floor:
        answer.append([x, y, 1])

    return sorted(answer)
