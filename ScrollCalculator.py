import math
def scroll(n, p):
    # Analyzing scroll chances and percentages
    # determine whether regular or dark
    if p == .3 or p == .7:
        dark_dict = {}
        
        for i in range(0,n+1):
            pass_prob = round( math.comb(n,i)*(p**i)*((1-p)**(n-i)), 4)
            blow_prob = round( (1-(p+(1-p)/2)**i), 4)
            
            dark_dict[i] =('passing', pass_prob,  'blow', blow_prob)
            if i == n:
                no_blow = 1 - blow_prob
                exp_num = math.floor(n*p) * no_blow
                print("Expected number of scrolls to pass if no blow = " + str(math.floor(n*p)))
                print("There is a " + str(blow_prob) + " chance that your items blow up")
                
            else:
                pass
        return dark_dict
            
        # expected chance of blowing up after n scrolls r1
        
      
        # prob of no blow
        

        # for loop displaying chances of n scrolls passing if no blow 
    else:
        reg_dict = {}
        for i in range(0, n+1):
            pass_prob = round( math.comb(n,i)*(p**i)*((1-p)**(n-i)), 4)
            reg_dict[i] = ('passing this many scrolls', pass_prob)

            if i == n:
                exp_num = math.floor(n*p)
                print("Expected number of scrolls to pass = " + str(math.floor(n*p)))
                print()
            
    
        # for loop displaying chances
    return reg_dict
    



        
