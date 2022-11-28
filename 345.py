class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # 전체 문자들에 대해서 모음의 위치를 기록함
        v_indices = []
        for i in range(len(s)):
            if s[i] in VOWELS:
                v_indices.append(i)

        # 해당 위치의 모음을 리스트로 만들고 뒤집음
        vs = []
        for i in v_indices:
            vs.append(s[i])
        vs.reverse()

        # 각 모음 위치에 뒤집은 모음 리스트를 순서대로 적용함
        for i, idx in enumerate(v_indices):
            s = s[:idx] + vs[i] + s[idx+1:]

        return s
