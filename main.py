from director import Director

def main():
    final_game = Director()
    final_game.start_game()
    # The program will end if the window is closed
    while not final_game.get_window_close():
        final_game.update_game()    
    final_game.end_game()

if __name__ == "__main__":
    main()