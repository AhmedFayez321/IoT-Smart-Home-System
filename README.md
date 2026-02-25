# 🏠 IoT Smart Home System (ESP-01 & Firebase)

A professional, full-stack IoT home automation system designed for 24/7 reliability. This system has been successfully operational in a real-world environment for over **1.5 years**.

## 🥇 Project Overview
This project provides a complete solution to control high-voltage home appliances (Lamp & Fan) via the internet. It features a custom-built hardware controller and multiple control interfaces (Desktop & Mobile).

## 🚀 Key Features
* **Cross-Platform Control:** Manage your home via a Python Desktop App or an Android Mobile App.
* **Real-time Synchronization:** Powered by **Firebase Realtime Database** for instant status updates.
* **Robust Hardware:** Designed for durability with integrated safety and power regulation.
* **Professional UI/UX:** The Python app includes branding, voice greetings, and status indicators.
* **Long-term Stability:** Tested and running 24/7 with zero downtime for 18+ months.

---

## 📂 Project Structure
The repository is organized as follows:

### 1. [/Firmware](./Firmware)
* Contains the C++ code for the **ESP-01 (ESP8266)** module.
* Features automatic Wi-Fi reconnection and Firebase integration.

### 2. [/Software](./Software)
* **Python-Desktop-App:** A modern GUI built with **KivyMD**. Features include audio feedback and real-time button color syncing.
* **Android-Mobile-App:** Includes the `.aia` source file and `.apk` for the mobile controller built with MIT App Inventor.

### 3. [/Hardware](./Hardware)
* Contains circuit schematics, wiring diagrams, and the Bill of Materials (BOM).

---

## 🛠️ Bill of Materials (BOM)

| Component | Quantity | Description / Purpose |
| :--- | :---: | :--- |
| **ESP-01 (ESP8266)** | 1 | The main Wi-Fi brain for cloud communication. |
| **Relay Module (5V/12V)** | 2 | To switch the 220V AC circuits (Lamp & Fan). |
| **AC-to-DC Power Module** | 1 | Converts 220V AC to 5V DC for logic power. |
| **AMS1117 3.3V Regulator**| 1 | Provides clean 3.3V power to the ESP-01. |
| **Transistors (2N2222)** | 2 | Used as switches to drive the relays safely. |
| **Resistors (10kΩ / 1kΩ)**| 4 | Pull-up/down resistors for stable boot & logic. |
| **Electrolytic Capacitor** | 1 | For power decoupling and noise filtering. |
| **Perf-board / PCB** | 1 | For mounting and soldering components. |
| **Connectors/Terminals** | 3 | Screw terminals for safe AC and relay wiring. |

---

## 🔧 Installation & Setup

### For the Python App:
1. Navigate to `/Software/Python-Desktop-App`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Add your Firebase credentials in a `serviceAccountKey.json` file (excluded for security).
4. Run `python main.py`.

### For the Firmware:
1. Open the `.ino` file in Arduino IDE.
2. Install **Firebase ESP Client** library.
3. Update your WiFi and Firebase credentials in the code.
4. Flash the code to your ESP-01 module.

---

## ⚠️ Safety Warning
This project involves working with **220V AC mains electricity**. High voltage can be lethal. Always ensure power is disconnected during wiring, and use proper insulation for all components.

---

### 👨‍💻 Developed by:
**Ahmed Fayez** *AI & Robotics Student at MICA Academy* [GitHub Profile](https://github.com/AhmedFayez321) | [Email](mailto:ahmedfayaez21@gmail.com)
