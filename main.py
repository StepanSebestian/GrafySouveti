import PySimpleGUI as sg
import urllib
from PIL import Image, ImageFilter
import sys

# informace pro automatickou aktualizaci
# verze
version = 1
# určíme, jestli chceme kanál release, beta nebo jsme vývojová verze, v tomto případě neaktualizujeme
type = "dev"


# nastaví téma okna
sg.theme("SystemDefault")

def start():
    
    if update():
        layout_start = [[sg.Text("Vítejte! Je k dispozici aktualizace.\nPro stažení klikněte na stáhnout, budete přesměrováni do prohlížeče."), sg.Text(size=(12,1), key='-OUTPUT-')],
                [sg.Button("Pokračovat")]]
    else:
        layout_start = [[sg.Text("Vítejte! Používáte nejnovější verzi GrafySouveti"), sg.Text(size=(12,1), key='-OUTPUT-')],
                [sg.Button("Pokračovat")]]

    window_start = sg.Window("GrafySouveti - kontrola aktualizací", layout_start)

    while True:
        event, values = window_start.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Ukončit":
            window_start.close()
            konec()
        if event == "Pokračovat":
            window_start.close()
            zadat_serie()

def zadat_serie():
    layout_zadat = [
              [sg.Text("Prosím zadejte první prvek a vyberte jeho typ")],
              [sg.Input(key="-PRVEK-IN-")],
              [sg.Text("Prosím vyberte jeho typ")],
              [sg.Button("Podmět (PO)")],
              [sg.Button("Přísudek (PŘ)")],
              [sg.Button("Předmět (PT)")],
              [sg.Button("Přívlastek shodný (PKS)")],
              [sg.Button("Přívlastek neshodný (PKN)")],
              [sg.Button("Doplněk (DO)")],
              [sg.Button("Př. u. místa (PUM)")],
              [sg.Button("Př. u. času (PUČ)")],
              [sg.Button("Př. u. způsobu (PUZ)")],
              [sg.Button("Př. u. příčiny (PU příčiny)")],
              [sg.Button("Př. u. účelu (PU účelu)")],
              [sg.Button("Př. u. míry (PU míry)")],
              [sg.Button("Př. u. podmínky(PU podmínky)")],
              [sg.Button("Př. u. přípustky (PU přípustky)")],
              [sg.Button("Konec zadání")]]

    window_zadat = sg.Window("GrafySouveti - nový prvek", layout_zadat)
    
    event, values = window_zadat.read()
    window_zadat.close()
    konec(True)

def konec(crash=False):
    """
    Ukončí program
    
    Argumenty:

    crash -- výchozí False, pokud True vyhodí chybovou hlášku s kontaktem a ukončí program s nenulovým chybovým kódem
            pokud False, Vyhodí hlášku s poděkováním a zavře program s nulovým chybovým kódem
    """
    if crash:
        msg_crash = "Ale ne. Tohle se nemělo stát.\nProgram selhal a musel se ukončit.\nMůžete to zkusit znovu, nebo využijte emailového kontaktu\norangeorange0123+gs@disroot.org"
        print(msg_crash)
        event, values = sg.Window("GrafySouveti - Program selhal", [[sg.Text(msg_crash)], [sg.Button("Zavřít")]]).read(close=True)

        sys.exit(1)
    else:
        msg_exit = "Děkujeme za použití GrafySouveti\nProgram vytvořil Štěpán Šebestian\norangeorange0123+gs@disroot.org"
        print(msg_exit)
        event, values = sg.Window("GrafySouveti - Konec", [[sg.Text(msg_exit)], [sg.Button("Zavřít")]]).read(close=True)
        sys.exit(0)

def update():
    """
    Vyhledá aktualizace
    """
    if type == "release":
        updateSource = urllib.urlopen("https://raw.githubusercontent.com/StepanSebestian/GrafySouveti/main/version.txt")
    elif type == "beta":
        updateSource = urllib.urlopen("https://raw.githubusercontent.com/StepanSebestian/GrafySouveti/beta/version.txt")
    elif type == "dev":
        return False
    else:
        # Co tady sakra dělám
        konec(True)
    updateContents = updateSource.read()

    return updateContents > version

start()
