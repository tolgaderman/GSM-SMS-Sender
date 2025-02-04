# GSM SMS Sender (GSM SMS-Sender)

Ein duales System zur SMS-Versendung mit Arduino und Python. Dieses Projekt ermöglicht das Senden von SMS-Nachrichten über ein GSM-Modul, das mit Arduino verbunden ist und durch eine Python-Schnittstelle gesteuert wird.

## Komponenten (Komponenten)

- Arduino (Uno/Nano/Mega)
- GSM-Modul (SIM800L/SIM900)
- Jumper-Kabel
- USB-Kabel
- SIM-Karte
- Computer mit Python und Arduino IDE

## Verbindungsschema (Anschlussplan) 

Arduino GSM-Modul
7 (TX) -> RX
8 (RX) -> TX
5V -> VCC (oder externe Stromversorgung)
GND -> GND


⚠️ **Wichtig**: Das GSM-Modul kann einen hohen Stromverbrauch haben. Eine externe Stromversorgung wird empfohlen.

## Installation

1. **Arduino-Setup**
   - Arduino IDE installieren
   - SoftwareSerial-Bibliothek installieren (standardmäßig enthalten)
   - `GSM_SMS_Arduino.ino` auf den Arduino hochladen

2. **Python-Setup**
   ```bash
   pip install pyserial
   ```

## Verwendung (Verwendung)

1. Hardware anschließen gemäß Verbindungsschema
2. Arduino-Code hochladen
3. Python-Skript ausführen:
   ```bash
   python gsm_sms_gonderici.py
   ```
4. Telefonnummer und Nachricht eingeben
5. SMS senden

## Dateien im Projekt

- `GSM_SMS_Arduino.ino` - Arduino-Code für die GSM-Modul-Steuerung
- `gsm_sms_gonderici.py` - Python-Interface für die Benutzereingabe und serielle Kommunikation

## Funktionen

### Arduino-Code
- Initialisierung des GSM-Moduls
- AT-Befehle Handling
- Serielle Kommunikation zwischen Python und GSM-Modul

### Python-Code
- Benutzerfreundliche Eingabeschnittstelle
- Serielle Kommunikation mit Arduino
- Fehlerbehandlung und Statusmeldungen

## Fehlerbehebung

1. **Keine Verbindung zum GSM-Modul**
   - Überprüfen Sie die Stromversorgung
   - Überprüfen Sie die TX/RX-Verbindungen
   - Stellen Sie sicher, dass die SIM-Karte korrekt eingesetzt ist

2. **Kommunikationsfehler**
   - Überprüfen Sie den COM-Port in der Python-Datei
   - Stellen Sie sicher, dass die Baudrate korrekt ist (9600)

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe `LICENSE` Datei für Details.

## Beitragen

1. Fork das Projekt
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## Projektstruktur


GSM-SMS-Sender/
├── README.md
├── LICENSE
├── arduino/
│ └── GSM_SMS_Arduino.ino
└── python/
└── gsm_sms_sender.py
