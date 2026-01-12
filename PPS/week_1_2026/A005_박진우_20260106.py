def solution(skill, skill_trees):
    count = 0
    
    for tree in skill_trees:
        filtered = [s for s in tree if s in skill]
        if "".join(filtered).startswith(skill[:len(filtered)]):
            count += 1
    
    return count
