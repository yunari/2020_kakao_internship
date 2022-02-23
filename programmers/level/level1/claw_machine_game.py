def solution(board, moves):
    popped_num = 0
    picked = []

    for move in moves:
        for i in range (0, len(board)):
            if board[i][move - 1]:
                if len(picked) > 0 and picked[len(picked) - 1] == board[i][move - 1]:
                    picked.pop()
                    popped_num += 2
                else:
                    picked.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

    return popped_num

if __name__ == "__main__":
    solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])