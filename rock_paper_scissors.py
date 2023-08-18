import random
from fastapi import FastAPI

app = FastAPI()

def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of the Rock-Paper-Scissors game based on the choices.

    Args:
        player_choice (str): The player's choice (rock, paper, or scissors).
        computer_choice (str): The computer's random choice.

    Returns:
        str: Result message indicating the winner or tie.
    """
    if player_choice == computer_choice:
        return "It's a tie!"
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    return "Computer wins!"

def get_computer_choice():
    """
    Get a random choice for the computer (rock, paper, or scissors).

    Returns:
        str: Computer's random choice.
    """
    return random.choice(["rock", "paper", "scissors"])

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: Welcome message.
    """
    return {"message": "Welcome to Rock-Paper-Scissors API!"}

@app.post("/play/{player_choice}")
def play_game(player_choice: str):
    """
    Play the Rock-Paper-Scissors game.

    Args:
        player_choice (str): The player's choice (rock, paper, or scissors).

    Returns:
        dict: Result of the game, including player and computer choices and winner.
    """
    player_choice = player_choice.lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        return {"error": "Invalid choice. Please choose rock, paper, or scissors."}

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    return {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
