class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        idx = 0
        while idx < len(arr):
            if arr[idx] == "" and idx != 0:
                del arr[idx]
                continue
            if arr[idx] == ".":
                del arr[idx]
                continue
            if arr[idx] == "..":
                del arr[idx]
                if idx == 1:
                    continue
                else:
                    del arr[idx-1]
                    idx -= 1
                    continue
            else:
                idx += 1
        if len(arr) == 1:
            return "/" + arr[0]
        return "/".join(arr)