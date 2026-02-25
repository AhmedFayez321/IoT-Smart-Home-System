/*
 * Project: IoT Smart Home System
 * Author: Ahmed Fayez (AI & Robotics Student)
 * Description: Control Home Appliances (Lamp/Fan) via Firebase RTDB using ESP8266.
 * Hardware: ESP-01 Module / Relay Circuits
 */

#include <ESP8266WiFi.h>
#include <Firebase_ESP_Client.h>

// WiFi Credentials - Replace with your own for local testing
// DO NOT upload your real credentials to GitHub
#define WIFI_SSID "YOUR_WIFI_SSID"
#define WIFI_PASSWORD "YOUR_WIFI_PASSWORD"

// Firebase Credentials
#define API_KEY "YOUR_FIREBASE_API_KEY"
#define DATABASE_URL "YOUR_DATABASE_URL"

// Firebase User Authentication (If enabled)
#define USER_EMAIL "YOUR_EMAIL@example.com"
#define USER_PASSWORD "YOUR_PASSWORD"

// Firebase objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// Timing variables
unsigned long sendDataPrevMillis = 0;
const long interval = 1000; // Check database every 1 second

// Pin Definitions
const int lampPin = 2;  // GPIO2
const int fanPin = 3;   // GPIO3 (Note: GPIO3 is also RX pin on ESP-01)

/**
 * Connects the ESP module to the local WiFi network
 */
void setupWiFi() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nConnected to WiFi!");
}

/**
 * Configures Firebase settings and authentication
 */
void setupFirebase() {
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}

void setup() {
  // Initialize GPIO pins as outputs
  pinMode(lampPin, OUTPUT);
  pinMode(fanPin, OUTPUT);
  
  // Set initial state (OFF)
  digitalWrite(lampPin, HIGH); // Assuming Active-Low Relay
  digitalWrite(fanPin, LOW);

  setupWiFi();
  setupFirebase();
}

void loop() {
  // Check connection and timing interval
  if (Firebase.ready() && (millis() - sendDataPrevMillis > interval || sendDataPrevMillis == 0)) {
    sendDataPrevMillis = millis();

    // 1. Control Lamp (Active-Low Logic Example)
    if (Firebase.RTDB.getString(&fbdo, "Smart_Home/Lamp/state")) {
      int state = atoi(fbdo.to<const char *>());
      // !(state) is used if your relay module is Active-Low
      digitalWrite(lampPin, !state); 
    }

    // 2. Control Fan (Active-High Logic Example)
    if (Firebase.RTDB.getString(&fbdo, "Smart_Home/Fan/state")) {
      int state = atoi(fbdo.to<const char *>());
      digitalWrite(fanPin, state);
    }
  }
}