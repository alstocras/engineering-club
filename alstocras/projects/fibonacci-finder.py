nTerm = int(input("which term OF TE VJEbrewifhrj fibonaci sequence you want until???!??! "))
terms = [1, 1]
for i in range(1, nTerm + 1):
    sum = terms[i - 1] + terms[i] 
    terms.append(sum)
print(terms)