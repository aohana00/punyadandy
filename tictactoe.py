import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 3

    def print_board(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print("\n")

    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Periksa baris
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True

        # Periksa kolom
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # Periksa diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False

    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def get_computer_move(self):
        # Strategi AI sederhana
        available = self.available_moves()

        # Cek apakah komputer bisa menang
        for move in available:
            board_copy = self.board.copy()
            board_copy[move] = 'O'
            if self.check_winner_copy(board_copy, move, 'O'):
                return move

        # Cek apakah perlu blok pemain
        for move in available:
            board_copy = self.board.copy()
            board_copy[move] = 'X'
            if self.check_winner_copy(board_copy, move, 'X'):
                return move

        # Ambil tengah jika tersedia
        if 4 in available:
            return 4

        # Ambil sudut
        corners = [0, 2, 6, 8]
        corner_moves = [move for move in available if move in corners]
        if corner_moves:
            return random.choice(corner_moves)

        # Ambil gerakan acak
        return random.choice(available)

    def check_winner_copy(self, board, square, letter):
        # Periksa baris
        row_ind = square // 3
        row = board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True

        # Periksa kolom
        col_ind = square % 3
        column = [board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # Periksa diagonal
        if square % 2 == 0:
            diagonal1 = [board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False


def play_game():
    print("=" * 40)
    print("SELAMAT DATANG DI PERMAINAN TIC-TAC-TOE")
    print("=" * 40)
    print("\nAnda bermain sebagai X")
    print("Komputer bermain sebagai O")
    print("\nPermainan akan dimainkan selama 3 ronde")
    print("Pemenang adalah yang mendapat skor lebih tinggi!\n")

    game = TicTacToe()

    while game.rounds_played < game.max_rounds:
        game.rounds_played += 1
        print(f"\n{'=' * 40}")
        print(f"RONDE {game.rounds_played} dari 3")
        print(f"{'=' * 40}")
        print(f"Skor - Anda: {game.player_score} | Komputer: {game.computer_score}\n")

        game.reset_board()
        
        print("Posisi papan:")
        game.print_board_nums()

        while game.empty_squares():
            # Giliran pemain
            print("Giliran Anda (X)")
            valid_move = False
            while not valid_move:
                try:
                    square = input("Pilih posisi (0-8): ")
                    square = int(square)
                    if square < 0 or square > 8:
                        print("Posisi harus antara 0-8. Coba lagi!")
                        continue
                    if square not in game.available_moves():
                        print("Posisi sudah diambil. Coba lagi!")
                        continue
                    valid_move = True
                except ValueError:
                    print("Input tidak valid. Masukkan angka 0-8.")

            game.make_move(square, 'X')
            game.print_board()

            if game.current_winner:
                print(f"🎉 ANDA MENANG RONDE INI!")
                game.player_score += 1
                break

            if not game.empty_squares():
                print("SERI! Tidak ada pemenang.")
                break

            # Giliran komputer
            print("Giliran Komputer (O)...")
            computer_move = game.get_computer_move()
            game.make_move(computer_move, 'O')
            print(f"Komputer memilih posisi {computer_move}")
            game.print_board()

            if game.current_winner:
                print(f"🤖 KOMPUTER MENANG RONDE INI!")
                game.computer_score += 1
                break

    # Tampilkan hasil akhir
    print(f"\n{'=' * 40}")
    print("PERMAINAN SELESAI!")
    print(f"{'=' * 40}")
    print(f"\nSkor Akhir:")
    print(f"  Anda: {game.player_score}")
    print(f"  Komputer: {game.computer_score}")

    if game.player_score > game.computer_score:
        print(f"\n🏆 SELAMAT! ANDA MENANG DENGAN SKOR {game.player_score}-{game.computer_score}!")
    elif game.computer_score > game.player_score:
        print(f"\n😢 KOMPUTER MENANG DENGAN SKOR {game.computer_score}-{game.player_score}")
    else:
        print(f"\n🤝 SERI! KEDUA-DUANYA MENDAPAT SKOR {game.player_score}")

    print(f"\n{'=' * 40}\n")


if __name__ == '__main__':
    while True:
        play_game()
        lagi = input("Ingin bermain lagi? (ya/tidak): ").lower()
        if lagi not in ['ya', 'y']:
            print("Terima kasih telah bermain! Sampai jumpa!")
            break
