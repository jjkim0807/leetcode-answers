from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp_solver(k, i, f, lc, ln):
            if i >= len(s):
                return len(f) + 1 + len(str(ln))
            else:
                # keep
                if lc == "":
                    ln = 1
                    lc = s[i]
                elif s[i] == lc:
                    ln += 1
                else:
                    if ln == 1:
                        f += lc
                    else:
                        f += lc + str(ln)
                    lc = s[i]
                    ln = 0
                r1 = dp_solver(k, i+1, f, lc, ln)

                # delete
                r2 = float("inf")
                if k > 0:
                    r2 = dp_solver(k-1, i+1, f, lc, ln)
                return r1 if r1 < r2 else r2

        return dp_solver(k, 0, "", "", 0)
