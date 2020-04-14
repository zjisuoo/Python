import enum, random

class Kid(enum.Enum) :
    BOY = 0
    GIRL = 1

def random_kid() -> Kid :
    return random.choice([Kid.BOY, Kid.GIRL])

both_girls = 0
older_girl = 0
either_gitl = 0

random.seed(0)

for _ in range(10000) :
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL :
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL :
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL :
        either_gitl += 1

print("P(both | older):", both_girls / older_girl)
print("P(both | older):", both_girls / either_gitl) 

'''
# 0, 1 사이
def updf(x : float) -> float :
    return 1 if 0 <= x < 1 else 0

def ucdf(x : float) -> float : 
    if x < 0 :
        return 0
    elif x < 1 :
        return x
    else :
        return 1
'''

# 균등 분포 확률 밀도 함수(2-3)
def updf(x : float) -> float :
    return 3 if 2 <= x < 3 else 2

# 균등 분포에 대한 누적 분포 함수(2-3)
def ucdf(x : float) -> float : 
    if x < 2 :
        return 2
    elif x < 3 :
        return x
    else :
        return 3