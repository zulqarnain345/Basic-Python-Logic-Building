v=["a","e","i","o","u"]
count_v=0
count_c=0
try:    
    name=input("enter the name ")
    name=name.lower()
    for i in range(len(name)):        
        if name[i].isalpha():
            if name[i] in v:
                count_v +=1
            else:
                count_c +=1
    print("count vowval::",count_v)
    print("constarate ",count_c)    

except Exception as e:
    print(e)    