n = input()
s = set(map(int, raw_input().split()))
for i in range(n):
    j = input().spilt()
    if j[0]=="remove":
        s.remove(int(j[1]))
    elif j[0]=="discard":
        s.remove(int(j[1]))
    else:
        s.pop()
print(sum(list(s)))


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

def minion_game(string):
        
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")