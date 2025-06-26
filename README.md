# 🐦 Flappy Bird - Reverse Mode

A creative twist on the classic Flappy Bird game: **Instead of controlling the bird to avoid pipes**, you now **control the pipe to avoid incoming birds**!  
The game is built using Python and the **Pygame** library, following the **Object-Oriented Programming (OOP)** model.

---

## 🎮 Gameplay

- Press `SPACE` to start the game.
- Use `↑` and `↓` arrows to move the pipe up and down to dodge birds.
- Press `P` to pause/resume the game.
- Press `ESC` to exit.
- Game difficulty increases every 5 points.
- The highest score is automatically saved.

---

## 🧠 Key Features

- ✅ Well-structured code using OOP principles  
- ✅ Game state management: Menu, Playing, Paused, Game Over  
- ✅ Sound effects for flapping, scoring, and collisions  
- ✅ Animated background with moving clouds and ground  
- ✅ Dynamic difficulty scaling based on score  
- ✅ Easily extensible and customizable  

---

## 🧱 Project Structure

### `main.py`  
- Entry point of the game.  
- Initializes the game loop and handles transitions between states (menu, play, pause, game over).

### `constants.py`  
- Contains global constants like screen size, speed, colors, fonts, etc.

### `assetmanager.py`  
- Centralized resource loader and manager for images, sounds, and fonts.

### `bird.py`  
- Represents **birds**.
- Birds fall and flap at set intervals.
- Birds spawn on the right and move left.
- Automatically spawned and removed off-screen.

### `pipe.py`  
- Represents the **player-controlled pipe**.
- Can move up and down.
- Detects collisions with birds.

### `ground.py` & `cloud.py`  
- Create dynamic visual effects for ground and clouds.
- Scroll to simulate motion.

### `score_manager.py`  
- Tracks current and high scores.
- Increases score when birds are successfully dodged.
- Saves high score to `high_score.txt`.

### `stage_manager.py`  
- Manages overall game state:
  - `menu`, `playing`, `paused`, `game_over`
- Enables easy switching between game states.

### `collision_detector.py`  
- Handles collision detection between the pipe and birds.
- On collision → triggers Game Over state.

---

## 📁 Directory Structure

```bash
flappy-bird-reverse/
├── assets/                # Image assets
├── sound/                 # Sound effects
├── bird.py                # Bird (enemy objects to dodge)
├── pipe.py                # Pipe (controlled by player)
├── cloud.py               # Clouds (background decoration)
├── ground.py              # Ground (scrolling effect)
├── score_manager.py       # Score tracking
├── stage_manager.py       # Game state control
├── collision_detector.py  # Collision detection logic
├── assetmanager.py        # Asset loader
├── constants.py           # Global constants
├── main.py                # Main game loop
├── high_score.txt         # Stores the high score
└── README.md


