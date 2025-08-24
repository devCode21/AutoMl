
import os 
def ongoing_add(data ):
    
    with open("artifacts/ongoin.txt" ,'a') as f:
        if type(data)==dict:
            for key,value in data.items():
                f.write(str(key) +str(value) +'\n')
        else:
            f.write(str(data)  + '\n' )
        
