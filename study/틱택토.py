# https://www.acmicpc.net/problem/7682 백준 틱택토


# result = []
# ccnt = 0
# while True:
    
#     data = input()    

#     ccnt+=1
#     if data == "end":
#          break
#     else:

        
#         cntO = data.count("O")
#         cntX = data.count("X")

#         if cntX - cntO not in [1,0]:
#             result.append("invalid")
#             continue

#         if cntX + cntO == 9:
#             if cntX - cntO == 1:
#                 result.append("valid")
#             else:
#                 result.append("invalid")
#             continue

#         equal = cntO == cntX
#         win = None

#         data = list(data)
    
#         board = [data[i*3:i*3+3] for i in range(0,3)]

#         valid = False

#         for i in range(3):
            
#             x = board[i][0]
#             cnt = 1
#             for a in range(1,3):
#                 if x == board[i][a]:
#                     cnt +=1
#                 else:
#                     break
            
#             if cnt == 3:
#                 win = x
#                 valid = True

#                 break

#             x = board[0][i]
#             cnt = 1
#             for a in range(1,3):
#                 if x == board[a][i]:
#                     cnt +=1
#                 else:
#                     break

#             if cnt == 3:
#                 win = x
#                 valid = True
#                 break

#         if valid:
#             if win == 'O':
#                 if equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")
#             else:
#                 if not equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")
            
#             continue
        
        
#         x = board[0][0]
        
#         cnt = 1
#         for i in range(2):
#             if x == board[1+i][1+i]:
#                 cnt +=1
#             else:
#                 break
        
#         if cnt == 3:

#             if x == 'O':
#                 if equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")
#             else:
#                 if not equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")
            
#             continue

#         x = board[2][0]
#         cnt = 1
#         for i in range(2):

#             if x == board[1-i][1+i]:
#                 cnt +=1
#             else:
#                 break
        
#         if cnt == 3:
            
#             if x == 'O':
#                 if equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")
#             else:
#                 if not equal:
#                     result.append("valid")
#                 else:
#                     result.append("invalid")

#             continue

#         result.append("invalid")
        
        


# for i in result:
#     print(i)

            
        
def checkThree(player):

    global board

    if player == board[0] == board[1] == board[2]:
        return True
    elif player == board[3] == board[4] == board[5]:
        return True
    elif player == board[6] == board[7] == board[8]:
        return True
    elif player == board[0] == board[3] == board[6]:
        return True
    elif player == board[1] == board[4] == board[7]:
        return True
    elif player == board[2] == board[5] == board[8]:
        return True
    elif player == board[0] == board[4] == board[8]:
        return True
    elif player == board[6] == board[4] == board[2]:
        return True
    else:
        return False

results = []
while True:

    board = input().strip()

    if board == 'end':
        break

    cntX = board.count('X')
    cntO = board.count('O')

    if cntX - cntO == 1:

        if ((cntX + cntO == 9 ) or checkThree("X")) and not checkThree("O"):
            results.append("valid")
            continue
   
    if cntX == cntO:

        if checkThree("O") and not checkThree("X"):
            results.append("valid")
            continue

    results.append("invalid")
        
    
for result in results:
    print(result)

    




                




        

    

    

