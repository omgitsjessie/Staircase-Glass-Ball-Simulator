##stairbreak, neater
from numpy import *
import math


def CalcX_maximizeNetGain(n_total):
    #Returns an x to throw the stair to, based on the probability and magnitude of gain or loss
    #depending on if the throw is successful.  This is for the algorithm that tries to maximize
    #the quantity gain - loss.
    ThrowPosition = ((( 1.0 / n_total) - math.pow((math.pow(n_total, -2) + (6 / n_total)), 0.5)) * (n_total * (0 - 1) / 3.0))
    return(math.ceil(ThrowPosition))

def CalcX_equalizeGainAndRisk(n_total):
    #Returns an x to throw the stair to, based on the probability and magnitude of gain or loss
    #depending on if the throw is successful.  This is for the algorithm that finds an x where
    #gain is equal to loss.
    ThrowPosition = (0.5 * (math.pow((1 + (8 * n_total)), 0.5)))
    return(math.ceil(ThrowPosition))

def alg_GainRiskMAX(n):
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = CalcX_maximizeNetGain(n)
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = CalcX_maximizeNetGain(n_new)

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown 
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)

def alg_GainRiskEQUAL(n):
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = CalcX_equalizeGainAndRisk(n)
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = CalcX_equalizeGainAndRisk(n_new)

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown 
        totalthrows = ball_1_throws + ball_2_throws
        #print "breakpoint: ", breakpoint
        #print "ball 1 throws: ", ball_1_throws
        #print "ball 2 throws: ", ball_2_throws
        #print "totalthrows: ", totalthrows
        results_list.append(totalthrows)
    return(results_list)

def alg_recursive(n, divisor): 
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = n / divisor
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = math.ceil(n_new / divisor)

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)

def alg_root(n, root):
    ##step size is: (n_new) ^ (1 / root)
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = math.pow(n,(1.0 / root))
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = math.ceil(math.pow(n_new,(1.0 / root))) 

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown 
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)

def alg_root_modified(n, multiplier):
    ## step size is: sqrt( n * multiplier )
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = math.pow((n * multiplier), 0.5)
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = math.ceil(math.pow((n * multiplier), 0.5)) 

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown 
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)

def alg_root_modified_recursive(n, multiplier):
    ## step size is: sqrt( n_new * multiplier )
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stair_to_throw = math.pow((n * multiplier), 0.5)
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n
        breakpoint_PRIME = breakpoint

        while stair_to_throw < breakpoint_PRIME: 
            stair_last_thrown += stair_to_throw
            n_new = n - stair_last_thrown
            breakpoint_PRIME = breakpoint - stair_last_thrown

            stair_to_throw = math.ceil(math.pow((n_new * multiplier), 0.5)) 

            ball_1_throws += 1
        
        ball_2_throws = breakpoint - stair_last_thrown 
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)

def alg_andrew(n, step_divisor):
    results_list = []
    breakindex = 0
    while breakindex < n:
        breakindex += 1
        breakpoint = breakindex
        stepinterval = math.ceil(n / step_divisor)
        stair_to_throw = stepinterval
        stair_last_thrown = 0
        ball_1_throws = 1
        ball_2_throws = 0
        n_new = n   

        while stair_to_throw < breakpoint:
            stair_last_thrown += stepinterval
            n_new = n - stair_last_thrown

            if (n_new) < stepinterval:
                stair_to_throw = n
            else:
                stair_to_throw = stair_last_thrown + stepinterval

            ball_1_throws = ball_1_throws + 1

        ball_2_throws = breakpoint - stair_last_thrown
        totalthrows = ball_1_throws + ball_2_throws
        results_list.append(totalthrows)
    return(results_list)


def average(values):
    return( sum(values) / (len(values) * 1.0))

for n in [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]:  
    print
    print
    print "N = %d" % (n)

##    for divisor in [2, 3, 4]:
##        results_list = alg_recursive(n, divisor)
##        print "The average number of throws for the (n_remaining) / %d recursive algorithm: %.2f" % (divisor, average(results_list))
##    for step_divisor in range(0, 14):
##        results_list = alg_andrew(n, math.pow(2, step_divisor))
##        print "The average number of throws for the constant step of n / (2^%d) algorithm: %.2f" % (step_divisor, average(results_list))
##    for root in range(2, 5):
##        results_list = alg_root(n, root)
##        print "The average number of throws for the recursive step of (n_remaining)^(1/%d): %.2f" % (root, average(results_list))
##    for multiplier in [0.333, 0.5, 1, 2, 3]:
##        results_list = alg_root_modified(n, multiplier)
##        print "The average number of throws for the constant step of sqrt(n * %.2f): %.2f" % (multiplier, average(results_list))
    for multiplier in [0.25, 0.333, 0.5, 1, 2, 3, 4]:
        results_list = alg_root_modified_recursive(n, multiplier)
        print "The average number of throws for the recursive step of sqrt(N_remaining * %.4f): %.2f" % (multiplier, average(results_list))
    
    results_list = alg_GainRiskMAX(n)
    print "Maximize (Gain - Risk) algorithm - The average number of throws at N = %d: %.2f" % (n, average(results_list))
    results_list = alg_GainRiskEQUAL(n)
    print "Risk = Gain algorithm - The average number of throws at N = %d: %.2f" % (n, average(results_list))
    
