import random

def fuzzyMemFunLeft(left):
    if left > 0 and left < 15:
        return 1
    elif left >= 15 and left < 30:
        return random.choice([2, 3])
    elif left >= 30 and left < 45:
        return random.choice([4, 5])
    elif left >= 45 and left < 64:
        return 6
    else:
        return 0
    
def fuzzyMemFunRight(right):
    if right > 0 and right < 15:
        return 1
    elif right >= 15 and right < 30:
        return random.choice([2, 3])
    elif right >= 30 and right < 45:
        return random.choice([4, 5])
    elif right >= 45 and right < 64:
        return 6
    else:
        return 0
    
def fuzzyMemFunFront(front):
    if front > 0 and front < 30:
        return 7
    elif front >= 30 and front < 45:
        return random.choice([8, 9])
    elif front >= 45 and front < 64:
        return 10
    else:
        return 0
    
def fuzzyRules(lVal, fVal, rVal):
    fast = 1.5
    med = 1.0
    slow = 0.5
    
    lms = 0.0
    rms = 0.0
    
    if lVal == 1 and fVal == 7 and rVal == 1:
        lms = fast
        rms = slow
    elif lVal == 1 and fVal == 10 and rVal == 1:
        lms = slow
        rms = slow
    elif (lVal >= 2 and lVal <= 5) and fVal == 7 and rVal == 1:
        lms = med
        rms = fast
    elif (lVal >= 2 and lVal <= 5) and fVal == 10 and rVal == 1:
        lms = med
        rms = med
    elif lVal == 6 and fVal == 7 and rVal == 1:
        lms = slow
        rms = fast
    elif lVal == 6 and fVal == 10 and rVal == 1:
        lms = slow
        rms = med
    elif lVal == 1 and fVal == 7 and (rVal >= 2 and rVal <= 5):
        lms = fast
        rms = med
    elif lVal == 1 and fVal == 10 and (rVal >= 2 and rVal <= 5):
        lms = med
        rms = med
    elif (lVal >= 2 and lVal <= 5) and fVal == 7 and (rVal >= 2 and rVal <= 5):
        lms = slow
        rms = fast
    elif (lVal >= 2 and lVal <= 5) and fVal == 10 and (rVal >= 2 and rVal <= 5):
        lms = med
        rms = med
    elif lVal == 6 and fVal == 7 and (rVal >= 2 and rVal <= 5):
        lms = slow
        rms = fast
    elif lVal == 6 and fVal == 10 and (rVal >= 2 and rVal <= 5):
        lms = med
        rms = med
    elif lVal == 1 and fVal == 7 and rVal == 6:
        lms = fast
        rms = slow
    elif lVal == 1 and fVal == 10 and rVal == 6:
        lms = med
        rms = slow
    elif (lVal >= 2 and lVal <= 5) and fVal == 7 and rVal == 6:
        lms = fast
        rms = med
    elif (lVal >= 2 and lVal <= 5) and fVal == 10 and rVal == 6:
        lms = fast
        rms = fast
    elif lVal == 6 and fVal == 7 and rVal == 6:
        lms = fast
        rms = med
    elif lVal == 6 and fVal == 10 and rVal == 6:
        lms = fast
        rms = fast
        
    return lms, rms


print(fuzzyRules(fuzzyMemFunLeft(15), fuzzyMemFunFront(24), fuzzyMemFunRight(36)))