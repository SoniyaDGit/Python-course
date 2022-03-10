import random
Player1points=0
Player2points=0
Tiedpoints=0
No_of_rounds=int(input("Enter number of rounds you want to play: "))
Li=["rock","paper","scissor"]
for i in range(1,No_of_rounds+1):
    print("Enter into Round ::::",i)
    Player2=(random.choice(Li))
    Player1=input("Enter Player1 toss: ")
    print("Player1 choosed:",Player1)
    print("Player2 choosed:",Player2)
    a=1
    if a!=0:
        a=a+1
        if Player1==Player2:
            print("*************The round",i," is tied*************")
            Tiedpoints+=1
        elif Player1==Li[0] and Player2==Li[2]:
            print("*************Player1 Won the round*************",Li[0])
            Player1points+=1
        elif Player1==Li[2] and Player2==Li[0]:
            print("*************Player2 Won the round*************",Li[0])
            Player2points+=1
        elif Player1==Li[1] and Player2==Li[2]:
            print("*************Player2 Won the round*************",Li[2])
            Player2points+=1
        elif Player1==Li[2] and Player2==Li[1]:
            print("*************Player1 Won the round*************",Li[2])
            Player1points+=1
        elif Player1==Li[0] and Player2==Li[1]:
            print("*************Player2 Won the round*************",Li[1])
            Player2points+=1
        elif Player1==Li[1] and Player2==Li[0]:
            print("*************Player1 Won the round*************",Li[1])
            Player1points+=1
        if a==No_of_rounds:
            break
print("Tiedpoints is: ",Tiedpoints)
print("Player1Points: ",Player1points)
print("Player2points: ",Player2points)
if Player1points>Player2points:
    print("Player1 won the game with score : ",Player1points)
elif Player1points<Player2points:
    print("Player2 won the game with score : ",Player2points)
else:
    print("Game is Tied",Tiedpoints)
