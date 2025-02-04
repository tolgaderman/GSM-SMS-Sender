import serial
import time

class GSMModul:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=9600):
        # Seriellen Port initialisieren
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        self.initialize_module()
    
    def initialize_module(self):
        """GSM-Modul Initialisierungseinstellungen"""
        time.sleep(1)
        self.send_command('AT')  # Modulkontrolle
        time.sleep(1)
        self.send_command('AT+CMGF=1')  # SMS-Modus auf Text einstellen
        time.sleep(1)
    
    def send_command(self, command):
        """AT-Befehl senden und Antwort empfangen"""
        self.ser.write((command + '\r\n').encode())
        time.sleep(0.5)
        response = ''
        while self.ser.in_waiting:
            response += self.ser.read().decode()
        print(f"Gesendet: {command}")
        print(f"Empfangen: {response}")
        return response
    
    def send_sms(self, phone_number, message):
        """SMS senden"""
        try:
            print(f"\nTelefonnummer: {phone_number}")
            print(f"Nachricht zum Senden: {message}")
            bestaetigung = input("\nMöchten Sie die SMS senden? (J/N): ")
            
            if bestaetigung.upper() != 'J':
                print("SMS-Versand abgebrochen!")
                return False
            
            # SMS-Sendemodus aktivieren
            self.send_command(f'AT+CMGS="{phone_number}"')
            time.sleep(1)
            
            # Nachricht senden und mit Ctrl+Z beenden
            self.ser.write(message.encode())
            self.ser.write(bytes([26]))  # Ctrl+Z Zeichen
            time.sleep(2)
            
            response = ''
            while self.ser.in_waiting:
                response += self.ser.read().decode()
            
            if 'OK' in response:
                print("\n✓ SMS erfolgreich gesendet!")
                return True
            else:
                print("\n✗ SMS konnte nicht gesendet werden!")
                return False
                
        except Exception as e:
            print(f"\n✗ Fehler aufgetreten: {str(e)}")
            return False
    
    def close(self):
        """Seriellen Port schließen"""
        self.ser.close()

# Beispielverwendung
if __name__ == "__main__":
    try:
        # GSM-Modul initialisieren
        print("GSM-Modul wird initialisiert...")
        gsm = GSMModul(port='COM3', baud_rate=9600)
        
        while True:
            print("\n=== SMS-Versand System ===")
            
            # Telefonnummer eingeben
            while True:
                telefon_nr = input("\nBitte geben Sie die Telefonnummer ein (+49XXXXXXXXXX): ")
                if telefon_nr.startswith('+') and len(telefon_nr) >= 12 and telefon_nr[1:].isdigit():
                    break
                print("Ungültige Telefonnummer! Bitte geben Sie eine gültige Nummer mit +49 ein.")
            
            # Nachricht eingeben
            while True:
                nachricht = input("Bitte geben Sie Ihre Nachricht ein: ")
                if len(nachricht.strip()) > 0:
                    break
                print("Die Nachricht darf nicht leer sein!")
            
            # SMS senden
            gsm.send_sms(telefon_nr, nachricht)
            
            # Weitermachen?
            weitermachen = input("\nMöchten Sie eine weitere SMS senden? (J/N): ")
            if weitermachen.upper() != 'J':
                break
        
        # Verbindung schließen
        gsm.close()
        print("\nProgramm beendet.")
        
    except Exception as e:
        print(f"\nProgrammfehler: {str(e)}")
        print("Programm beendet.") 