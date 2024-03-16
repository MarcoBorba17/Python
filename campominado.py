import random

def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = set()

    while len(mines) < num_mines:
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if board[row][col] != 'X':
            mines.add((row, col))
            board[row][col] = 'X'

    return board

def count_adjacent_mines(board, row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'X':
                count += 1
    return count

def reveal_empty_cells(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ' ':
        mines_around = count_adjacent_mines(board, row, col)
        board[row][col] = str(mines_around) if mines_around > 0 else ' '
        if mines_around == 0:
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    reveal_empty_cells(board, r, c)

def print_board(board):
    for row in board:
        print(' '.join(row))

def main():
    rows, cols, num_mines = 8, 8, 10
    board = create_board(rows, cols, num_mines)

    print("Campo Minado - Jogo Iniciado!")
    print_board(board)

    while True:
        try:
            row, col = map(int, input("Digite a linha e a coluna (separadas por espaço): ").split())
            if board[row][col] == 'X':
                print("Você perdeu! As minas venceram.")
                break
            reveal_empty_cells(board, row, col)
            print_board(board)
        except (ValueError, IndexError):
            print("Entrada inválida. Digite novamente.")

if __name__ == "__main__":
    main()


