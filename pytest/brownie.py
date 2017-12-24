import pandas as pd
from fuzzywuzzy import fuzz,process
def fun_name(movie_name):
    fun = pd.read_csv('merge.csv')
    name,score,x = process.extractOne(movie_name, fun['Title'])
    l = (fun['Title'] == name).idxmax()
    if l == 0 and fun['Title'][0]!=name:
        return "Unknown"
    else:
        return fun['Rating'][l]

print(fun_name('Split'))