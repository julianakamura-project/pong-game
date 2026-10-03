# 🏓 Pong — Python OOP Project

A classic **Pong game** developed in Python as part of my studies in **Object-Oriented Programming (OOP)**.

This project is being developed as a practical exercise to apply OOP concepts such as classes, objects, attributes, methods, inheritance, and object interaction.

## Play the Game

[🎮 Play Pong Online](https://julianakamura-project.github.io/pong-game/)

Disclaimer: currently, the web version of the game was created using AI to convert my Python code into HTML so that it could be played by everyone. However, I plan to learn HTML as well to make this on my own in the future.

---

## 🎯 About the Project

The goal of this project is to recreate the classic Pong game while practicing how to structure a program using **Object-Oriented Programming**.

Instead of having all of the game logic contained in a single script, the game is organized into different classes responsible for specific parts of the application.

The project will be developed progressively as I learn new OOP concepts.

---

## 🧠 OOP Concepts Practiced

This project is being used to practice:

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Instance Methods
- Inheritance

Not every concept may be required for the final game, but the project provides opportunities to experiment with different approaches to object-oriented design.

---

## 🎮 Game Features

The planned game will include:

- [✔️] Two-player gameplay
- [✔️] Player-controlled paddles
- [✔️] Ball movement
- [✔️] Collision detection
- [✔️] Score tracking
- [✔️] Increasing ball speed
- [✔️] Screen boundaries
- [✔️] Game reset after a point
- [✔️] Winning condition
- [✔️] Game over screen
- [✔️] Keyboard controls

Additional features may be added.

---

## 🏗️ Planned Classes

The game will be divided into separate objects responsible for different aspects of the game.

### 🏓 Paddle

Responsible for:

- Creating the paddle
- Moving the paddle
- Handling player controls
- Detecting boundaries

### ⚪ Ball

Responsible for:

- Creating the ball
- Moving the ball
- Changing direction
- Resetting after a point

### 🧮 Scoreboard

Responsible for:

- Keeping track of the players' scores
- Displaying the current score
- Updating the score after each point

### 🎮 Game

Responsible for:

- Managing the game loop
- Coordinating the different objects
- Detecting game conditions
- Handling the overall game state

### 🔳 Border

Responsible for:

- Creating a border for the playable area
- Creating a midline

---

## 🗂️ Project Structure

The project is expected to follow a structure similar to:

```text
Pong-OOP/
│
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
├── border.py
│
└── README.md
