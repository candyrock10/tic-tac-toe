from flask import Flask, request, jsonify
from game import TicTacToe

app = Flask(__name__)
game = TicTacToe()


@app.route("/new", methods=["POST"])
def new_game():
    global game
    game = TicTacToe()
    return jsonify({"message": "New game started!", "status": game.get_status()})


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "Missing row or col"}), 400

    if not (0 <= row <= 2 and 0 <= col <= 2):
        return jsonify({"error": "Invalid move position"}), 400

    success = game.make_move(row, col)

    if not success:
        return jsonify({"error": "Invalid move"}), 400

    return jsonify({"message": "Move accepted", "status": game.get_status()})


@app.route("/status", methods=["GET"])
def status():
    return jsonify(game.get_status())


if __name__ == "__main__":
    app.run(debug=True)
