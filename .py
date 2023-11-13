x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
x_flat = []

def flatten(lst):
    for i in lst:
        if isinstance(i,list):
            flatten(i)
        else:
            x_flat.append(i)
flatten(x)
print(x_flat)

y = [[1, 2], [3, 4], [5, 6, 7]]
y_rev = []
def revers(lst):
    y = lst[::-1]
    for i in y:
        reversed_y = i[::-1]
        y_rev.append(reversed_y)
       
revers(y)
print(y_rev)
