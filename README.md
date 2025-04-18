# 🕹️ Tic-Tac-Toe API (Flask)

A simple RESTful API for playing Tic-Tac-Toe, built using Flask. This API allows two players to play by sending POST requests and tracking the board, turns, and game status in real-time.

---

## 🚀 Features

- Start a new game
- Make moves by sending row and column
- Automatically switches players (X and O)
- Detects wins and draws
- JSON-based responses

---

## 📂 Project Structure


---

## 🔧 Requirements

- Python 3.7+
- Flask

# 📊 Get Game Status
## GET /status

Response
{
  "board": [["X", "O", "X"], [" ", "O", " "], [" ", " ", " "]],
  "current_symbol": "X",
  "winner": null,
  "draw": false
}

# 📄 License
MIT License

# 🧑‍💻 Author
@candyrock10


