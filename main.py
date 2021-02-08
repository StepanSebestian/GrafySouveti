import PySimpleGUI as sg
import sys

# nastaví téma okna
sg.theme("SystemDefault")

def start():
    # layout okna
    layout_start = [[sg.Text("Vítejte! Vyhledávání aktualizací je zakázáno."), sg.Text(size=(12,1), key='-OUTPUT-')],
                [sg.Button("Pokračovat"), sg.Button("Ukončit")]]

    window_start = sg.Window("GrafySouveti - kontrola aktualizací", layout_start)

    while True:
        event, values = window_start.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Ukončit":
            window_start.close()
            konec()
        if event == "Pokračovat":
            window_start.close()
            zadat()

def zadat():
    menu_def_zadat = [["Soubor", ["Ukončit", "Zkontrolovat aktualizace"]],
            ["Nový", ["Prvek", "Spojení", "Skladební vztah"]]]

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
    konec()

def konec(crash=False):
    if crash:
        msg_crash = "Ale ne. Tohle se nemělo stát.\nProgram selhal a musel se ukončit.\nMůžete to zkusit znovu, nebo využijte emailového kontaktu\norangeorange0123@disroot.org"
        print(msg_crash)
        event, values = sg.Window("GrafySouveti - Program selhal", [[sg.Text(msg_crash)], [sg.Button("Zavřít")]]).read(close=True)

        sys.exit(1)
    else:
        msg_exit = "Děkujeme za použití GrafySouveti"
        print(msg_exit)
        event, values = sg.Window("GrafySouveti - Konec", [[sg.Text(msg_exit)], [sg.Button("Zavřít")]]).read(close=True)
        sys.exit(0)

start()
