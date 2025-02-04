#include <SoftwareSerial.h>

// TX und RX Pins für das GSM-Modul definieren
const int GSM_TX_PIN = 7;  // Pin 7 des Arduino wird mit RX-Pin des GSM-Moduls verbunden
const int GSM_RX_PIN = 8;  // Pin 8 des Arduino wird mit TX-Pin des GSM-Moduls verbunden

// Softwarebasierte serielle Schnittstelle für das GSM-Modul erstellen
SoftwareSerial gsmSerial(GSM_RX_PIN, GSM_TX_PIN); // RX, TX

void setup() {
  // Hardware-serielle Schnittstelle für Debugging starten
  Serial.begin(9600);
  Serial.println("GSM-Modul Test");
  
  // Software-serielle Schnittstelle für GSM-Modul starten
  gsmSerial.begin(9600);
  
  // GSM-Modul initialisieren
  initGSM();
}

void loop() {
  // Daten von Python zum GSM-Modul weiterleiten
  if (Serial.available()) {
    gsmSerial.write(Serial.read());
  }
  
  // Daten vom GSM-Modul zu Python weiterleiten
  if (gsmSerial.available()) {
    Serial.write(gsmSerial.read());
  }
}

void initGSM() {
  delay(2000); // Warten bis das GSM-Modul startet
  
  // GSM-Modul mit AT-Befehlen konfigurieren
  sendATCommand("AT");
  delay(1000);
  sendATCommand("AT+CMGF=1"); // SMS-Modus auf Text einstellen
  delay(1000);
  sendATCommand("AT+CNMI=2,2,0,0,0"); // Benachrichtigungen für neue SMS konfigurieren
  delay(1000);
}

void sendATCommand(String command) {
  Serial.println("Gesendet: " + command);
  gsmSerial.println(command);
  delay(500);
  
  // Antwort vom GSM-Modul lesen
  String response = "";
  while (gsmSerial.available()) {
    char c = gsmSerial.read();
    response += c;
    delay(10);
  }
  Serial.println("Empfangen: " + response);
} 