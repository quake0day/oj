def generateNext(string, start, final_res):
    if start == len(string):
        return 
    string = list(string)
    for i in xrange(start+1, len(string)):
        if string[i] == string[i-1] == '+':
            string[i] = string[i-1] = '-'
            final_res.append("".join(string))
            string[i] = string[i-1] = '+'
            generateNext(string, i + 1, final_res)


final_res = []
generateNext("------+++++------", 0, final_res)
print final_res
for string in final_res:
    ff = []
    generateNext(string, 0, ff)
    print ff