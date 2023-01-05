#Tic Tac Toe

board = [[""for x in range(3)]for y in range(3)] # 3x3의 board 이중배열을 만든다
i = 1
print("Tic Tac Toe 게임!")
print("A유저부터 시작합니다~")

while True:

    print("--------------") # 가로세로 3x3 그래프 만들기 

    for h in range(3):
        print("  ",board[h][0],"| ",board[h][1]," |",board[h][2])
        if(h!=2):
            print("--------------")

    print("--------------")
    
    x = int(input("x좌표를 입력하시오(끝내고 싶으면 9를 입력하세요!): "))
    y = int(input("y좌표를 입력하시오:"))
    
    if i%2 == 1:              # 1부터 시작이기 때문에 A유저 먼저 시작한다. A유저는 홀수 일 때 차례이다.
        if x == 9:  # 9를 입력하면 게임을 종료
            print("게임이 종료되었습니다.")
            break
        if board[x][y] != "": # 빈칸이 아니라면 이미 둔 곳이기 때문에 다시 입력시킨다.
           print("이미 둔 곳입니다. 다시 입력하세요.")
           continue
        else:
           board[x][y] = "A"
           i = i + 1                                 # 밑에 if는 가로 혹은 세로 혹은 대각선을 A로 채우는 것을 모두 포함하는 경우이다.
        if (board[0][0] == 'A' and board[0][1] == 'A' and board[0][2] == 'A') or (board[1][0] == 'A' and board[1][1] == 'A' and board[1][2] == 'A') or (board[2][0] == 'A' and board[2][1] == 'A' and board[2][2] == 'A') or (board[0][0] == 'A' and board[1][0] == 'A' and board[2][0] == 'A') or (board[0][1] == 'A' and board[1][1] == 'A' and board[2][1] == 'A') or (board[0][2] == 'A' and board[1][2] == 'A' and board[2][2] == 'A') or (board[0][0] == 'A' and board[1][1] == 'A' and board[2][2] == 'A') or (board[0][2] == 'A' and board[1][1] == 'A' and board[2][0] == 'A'):
               print("--------------")

               for h in range(3):                   # break로 끝내기 전에 승리한 그래프를 보여준다. 
                   print("  ",board[h][0],"| ",board[h][1]," |",board[h][2])
                   if(h!=2):
                       print("--------------")

               print("--------------")
               print("A유저가 승리하였습니다!!")      
               break

    elif i%2 == 0:                   # B유저는 짝수일 때 차례이다.
        if x == 9:    # 9를 입력하면 게임을 종료
            print("게임이 종료되었습니다.")
            break
        if board[x][y] != "":   # 빈칸이 아니라면 이미 둔 곳이기 때문에 다시 입력시킨다.
           print("이미 둔 곳입니다. 다시 입력하세요.")
           continue
        else:
           board[x][y] = "B"
           i = i + 1                           # 밑에 if는 가로 혹은 세로 혹은 대각선을 B로 채우는 것을 모두 포함하는 경우이다.
        if (board[0][0] == 'B' and board[0][1] == 'B' and board[0][2] == 'B') or (board[1][0] == 'B' and board[1][1] == 'B' and board[1][2] == 'B') or (board[2][0] == 'B' and board[2][1] == 'B' and board[2][2] == 'B') or (board[0][0] == 'B' and board[1][0] == 'B' and board[2][0] == 'B') or (board[0][1] == 'B' and board[1][1] == 'B' and board[2][1] == 'B') or (board[0][2] == 'B' and board[1][2] == 'B' and board[2][2] == 'B') or (board[0][0] == 'B' and board[1][1] == 'B' and board[2][2] == 'B') or (board[0][2]== 'B' and board[1][1] == 'B' and board[2][0] == 'B'):
               print("--------------")

               for h in range(3):                # break로 끝내기 전에 승리한 그래프를 보여준다. 
                   print("  ",board[h][0],"| ",board[h][1]," |",board[h][2])
                   if(h!=2):
                       print("--------------")

               print("--------------")
               print("B유저가 승리하였습니다!!")
               break
        
    if i == 10: #마지막으로 A유저가 자리를 채우면 i=10 이므로 무승부가 된다.
        print("--------------")

        for h in range(3):
            print("  ",board[h][0],"| ",board[h][1]," |",board[h][2])
            if(h!=2):
                print("--------------")
                       
        print("--------------")  
        print("무승부입니다!!")      
        break 