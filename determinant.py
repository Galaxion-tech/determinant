# any order determinant calculator

import copy
#function
def show(det):  #to show determinant
    for i in det:
        print(i)
        
def basic_det(det): # to calcualte 3-order determinant
    D=0 
    for i in range(0,3):
        cf_det=copy.deepcopy(det)
        cf_det[1].pop(i)
        cf_det[2].pop(i)
        
        cf_value= cf_det[1][0]*cf_det[2][1]-cf_det[1][1]*cf_det[2][0]
        D+=(-1)**(i)*det[0][i]*cf_value
        
    return D


def ord_det(det):  #n order determiant calculater
    D=0
    S=0
    for i in range(0,len(det)): #to convert (n)-order determinant to (n-1)-order determinant
        nf_det=copy.deepcopy(det)
        nf_det.pop(0)
        for j in range(0,len(det)-1):
            nf_det[j].pop(i)
        if len(nf_det)==3:# recursion
            D+=(-1)**(i)*det[0][i]*basic_det(nf_det) 
        else:    #recursion
            S+=(-1)**(i)*det[0][i]*int(ord_det(nf_det))
            if i==len(det)-1:
                return S
           
    return D    
        
#__main__

det=eval(input("ENTER THE SQUARE DETERMNANT (ORDER >2) ; for e.g. [[1,2,3],[2,3,4],[2,1,2]]:- "))

if len(det)==3:
    show(det)
    print("DETERMINANT is equal to ",basic_det(det))
else:
    show(det)
    print("DETERMINANT is equal to ",ord_det(det))
    
        
