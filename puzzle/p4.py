"""
    Given an absolute path for a file (Unix-style), simplify it.

    ex: /home/  -?> /home

    /a/./b/../../c/ -> /c

    /../ -> /

"""

def simplifyPath( path):
    
    stack = []
    i = 0
    res = ''
    while i < len(path):
        end = i+1
        while end < len(path) and path[end] != "/":
            end += 1
        sub=path[i+1:end]
        if len(sub) > 0:
            if sub == "..":
                if stack != []: stack.pop()
            elif sub != ".":
                stack.append(sub)
        i = end
    if stack == []: return "/"
    for i in stack:
        res += "/"+i
    return res

print simplifyPath("/home//foo/")
