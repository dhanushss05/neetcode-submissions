class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        a = [ '(',  '{' , '['  ]

        for i in s:
            if i in a:
                l.append(i)
            else:
                if len(l) != 0:
                    if i == ")" and l[-1]=="(":
                        l.pop()
                    elif i == "]" and l[-1]=="[":
                        l.pop()
                    elif i == "}" and l[-1]=="{":
                        l.pop()
                    else:
                        return False
                else:
                    return False
        return not l
