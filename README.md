# GSM SMS Sender

A dual system for sending SMS messages using Arduino and Python. This project allows sending SMS messages via a GSM module connected to an Arduino, controlled by a Python interface.

## Components

- Arduino (Uno/Nano/Mega)
- GSM Module (SIM800L/SIM900)
- Jumper wires
- USB cable
- SIM card
- Computer with Python and Arduino IDE

## Wiring Diagram

| Arduino Pin  | GSM Module Pin |
|--------------|----------------|
| 7 (TX)       | RX             |
| 8 (RX)       | TX             |
| 5V           | VCC (or external power supply) |
| GND          | GND            |

⚠️ **Important**: The GSM module can have high power consumption. It is recommended to use an external power supply.

## Installation

### 1. Arduino Setup
- Install the Arduino IDE.
- Install the SoftwareSerial library (included by default).
- Upload `GSM_SMS_Arduino.ino` to the Arduino.

### 2. Python Setup
Install the required Python package for serial communication:

```bash
pip install pyserial
```

## Usage

1. Connect the hardware according to the wiring diagram.
2. Upload the Arduino code.
3. Run the Python script:
   ```bash
   python gsm_sms_sender.py
   ```
4. Enter the phone number and message.
5. Send the SMS.

## Project Files

- `GSM_SMS_Arduino.ino` - Arduino code for controlling the GSM module.
- `gsm_sms_sender.py` - Python interface for user input and serial communication.

## Features

### Arduino Code
- GSM module initialization.
- Handling AT commands.
- Serial communication between Python and the GSM module.

### Python Code
- User-friendly input interface.
- Serial communication with Arduino.
- Error handling and status messages.

## Troubleshooting

1. **No connection to the GSM module:**
   - Check the power supply.
   - Verify TX/RX connections.
   - Ensure the SIM card is properly inserted.

2. **Communication errors:**
   - Check the COM port in the Python script.
   - Make sure the baud rate is correct (9600).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Project Structure

```bash
GSM-SMS-Sender/
├── README.md
├── LICENSE
├── arduino/
│   └── GSM_SMS_Arduino.ino
└── python/
    └── gsm_sms_sender.py
```

