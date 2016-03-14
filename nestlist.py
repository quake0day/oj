def flattern(l, final_res):
    
    for item in l:
        if isinstance(item, list):
            flattern(item, final_res)
        else:
            final_res.append(item)

    return final_res
final_res = []
flattern([1,[1,2]], final_res)
print final_res