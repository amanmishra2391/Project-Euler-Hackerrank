digit = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
teen = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
cent = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"} 

def Join(a, *b):
    ab = ""
    ab += a
    for x in b:
        if x != "":
            if ab != "":
                ab += " " + x
            else:
                ab += x
    return ab

def three(num):
    hun = ""
    t = ""
    d = ""
    if num//100!=0:
        hun += digit[num//100] + " Hundred"
    num %= 100
    if num//10==1:
        t += teen[num]
    else:
        if num//10!=0:
            t += cent[num//10]
        if num%10!=0:
            d += digit[num%10]
    return Join(hun, t, d)
def word(num):
    trillion = 10**12
    if num== trillion:
        return "One Trillion"
    elif num % trillion==0:
        return "Zero"
    else:
        a = num // 10**9
        bil = ""
        mil = ""
        thou = ""
        hun = ""
        if a!=0:
            bil = three(a) + " Billion"
        num %= 10**9
        a = num // 10**6
        if a!=0:
            mil = three(a) + " Million"
        num %= 10**6
        a = num // 10**3
        if a!=0:
            thou = three(a) + " Thousand"
        num %= 1000
        if num!=0:
            hun = three(num)
        return(Join(bil, mil, thou, hun))

for _ in range(int(input())):
    num = int(input())
    print(word(num))
