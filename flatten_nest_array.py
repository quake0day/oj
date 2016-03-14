

def flattern_nest_arary(arr, final_res):
    
    for i in arr:
        if type(i) is list:
            flattern_nest_arary(i, final_res)
        else:
            final_res.append(i)
    return final_res


arr = [1,2,[3,4,[5]]]
final_res = []
print flattern_nest_arary(arr, final_res)