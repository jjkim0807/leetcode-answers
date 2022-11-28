from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        used_i = {}
        used_j = {}
        points = {}
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                # 검은색이 등장할때마다 x, y좌표를 저장해두고, 해당 좌표를 이용하는 점을 연결해둔다.
                # 해당 점이 저장된 좌표와 같은 행이나 열에 있는 경우 해당 좌표와 연결된 점들을 중복된 점이라고 표시한다.
                if picture[i][j] == "B":
                    if i in used_i:
                        if len(used_i[i]) == 1:
                            points[used_i[i][0]] = True
                        points[(i, j)] = True
                        used_i[i].append((i, j))
                    else:
                        used_i[i] = [(i, j)]
                        if (i, j) not in points:
                            points[(i, j)] = False

                    if j in used_j:
                        if len(used_j[j]) == 1:
                            points[used_j[j][0]] = True
                        points[(i, j)] = True
                        used_j[j].append((i, j))
                    else:
                        used_j[j] = [(i, j)]
                        if (i, j) not in points:
                            points[(i, j)] = False

        # 중복된 좌표라고 표시된 것들은 제외한 좌표의 개수를 세어 리턴한다
        count = 0
        for k, v in points.items():
            if not v:
                count += 1
        return count
