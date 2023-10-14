def simplify_path(path):
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    canonical_path = '/' + '/'.join(stack)
    
    return canonical_path
path = "/../"
canonical_path = simplify_path(path)
print(canonical_path)
## time complexity->O(N)
## SPACE COMPLEXITY ->O(N)
