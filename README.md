# 🧠 Flappy Bird OpenCV Bot

This project is an experimental bot that uses **Computer Vision (CV)** to **see** and **play Flappy Bird**—completely hands-free! Built using Python and OpenCV, the bot captures your screen in real-time, detects the bird and pipes visually, and makes jumping decisions like a human.

> 🎮 Repo by [Sanjay Kumar](https://www.sanjaybuilds.com/) – Polyglot Dev, Indie Hacker & Self-taught Dev curious about AI x automation.

---

## 🚀 What This Bot Does

✅ Captures the game screen in real time  
✅ Detects the bird using color filters in HSV  
✅ Detects pipes as obstacles  
✅ Compares positions to decide **when to jump**  
✅ Automates gameplay using simulated keystrokes  

---

## 🔧 Tech Stack

| Tool/Library      | Purpose                          |
|------------------|----------------------------------|
| `pygame`          | Runs the original Flappy Bird game |
| `OpenCV`          | Computer vision – detecting bird and pipes |
| `mss`             | Fast screen capture              |
| `numpy`           | Image + math processing          |
| `pyautogui` / `keyboard` | Simulate jump inputs            |

---

## 🗺️ Project Roadmap

| Phase        | Goal                               | Status |
|--------------|------------------------------------|--------|
| ✅ Phase 1   | Real-time screen capture with `mss`| Done   |
| ✅ Phase 2   | Bird detection using HSV mask      | Done   |
| ⏳ Phase 3   | Pipe detection (next obstacle)     | WIP    |
| ⏳ Phase 4   | Decision logic: when to jump       | WIP    |
| 🔜 Phase 5   | Simulate keypress to play          | Pending|
| 🔜 Phase 6   | Add score tracking & stats         | Planned|
| 🔜 Phase 7   | Optional ML model for smarter play | Planned|


---

## 🧠 How It Works (Short Summary)

1. The bot uses `mss` to continuously grab a section of your screen where the game window is placed.
2. It converts the screen to HSV color space to detect colored objects (bird, pipes).
3. OpenCV contour detection is used to get bounding boxes around objects.
4. It uses logic to decide when the bird needs to jump (based on upcoming pipe gap).
5. The bot sends keypresses automatically to keep the bird alive.

---

## 🧪 Try It Locally

```bash
git clone https://github.com/05sanjaykumar/Flappy-Bird-OpenCV
cd Flappy-Bird-OpenCV
pip install -r requirements.txt
python cv_bot.py
````

Make sure your Pygame window is launched and placed in the expected screen area (or set a fixed position in code).

---

## 🎯 Where to Find Me

🌐 Portfolio: [sanjaybuilds.com](https://www.sanjaybuilds.com/)
🐍 GitHub: [@05sanjaykumar](https://github.com/05sanjaykumar)

---

## 🙏 Credits

Inspired by open source game automation, built from scratch for learning and experimentation.

---

## 🧠 License

MIT License – for learning and experimentation. Attribution appreciated.

````
