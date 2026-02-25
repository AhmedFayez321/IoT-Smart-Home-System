### 📋 Bill of Materials (BOM)

| Component | Quantity | Description / Purpose |
| :--- | :---: | :--- |
| **ESP-01 (ESP8266)** | 1 | The main Wi-Fi brain to handle Firebase communication. |
| **Relay Module (5V/12V)** | 2 | To switch the 220V AC circuits (Lamp & Fan). |
| **AC-to-DC Power Module** | 1 | Converts 220V AC to 5V DC (e.g., Hi-Link or generic adapter). |
| **AMS1117 3.3V Regulator** | 1 | Essential to provide clean 3.3V power to the ESP-01. |
| **Transistors (e.g., 2N2222)** | 2 | Used as switches to drive the relays from GPIOs. |
| **Resistors (10kΩ / 1kΩ)** | 4 | Pull-up/down resistors for GPIO0/CH_PD and transistor base. |
| **Electrolytic Capacitor** | 1 | (e.g., 100uF - 470uF) For power decoupling and stability. |
| **Perf-board / PCB** | 1 | For point-to-point soldering and mounting. |
| **Connectors / Terminals** | 3 | Screw terminals for easy AC and relay wiring. |
