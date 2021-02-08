import PySimpleGUI as sg
import urllib
from playsound import playsound
import sys

# informace pro automatickou aktualizaci
# verze
version = 1
# určíme, jestli chceme kanál release, beta nebo jsme vývojová verze, v tomto případě neaktualizujeme
type = "dev"

# uhhhh jo asi potřebujem globální proměnnou
prvky = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]

if type == "dev":
    print("DEBUG Délka prvky[] je: " + str(len(prvky)))

# nastaví téma okna
sg.theme("SystemDefault")

def start():
    
    if update():
        layout_start = [[sg.Text("Vítejte! Je k dispozici aktualizace.\nPro stažení klikněte na stáhnout, budete přesměrováni do prohlížeče."), sg.Text(size=(12,1), key='-OUTPUT-')],
                [sg.Button("Ignorovat")]]
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
            zadat()

def zadat():
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

    

    layout_misto = [[sg.Text("Vyberte pozici prvku\nPrvek značí X")],
                    [sg.Button(prvky[0], key="_Misto_0_"), sg.Button(prvky[1], key="_Misto_1_"), sg.Button(prvky[2], key="_Misto_2_"), sg.Button(prvky[3], key="_Misto_3_"), sg.Button(prvky[4], key="_Misto_4_"), sg.Button(prvky[5], key="_Misto_5_"), sg.Button(prvky[6], key="_Misto_6_"), sg.Button(prvky[7], key="_Misto_7_"), sg.Button(prvky[8], key="_Misto_8_"), sg.Button(prvky[9], key="_Misto_9_")],
                    [sg.Button(prvky[10], key="_Misto_10_"), sg.Button(prvky[11], key="_Misto_11_"), sg.Button(prvky[12], key="_Misto_12_"), sg.Button(prvky[13], key="_Misto_13_"), sg.Button(prvky[14], key="_Misto_14_"), sg.Button(prvky[15], key="_Misto_15_"), sg.Button(prvky[16], key="_Misto_16_"), sg.Button(prvky[17], key="_Misto_17_"), sg.Button(prvky[18], key="_Misto_18_"), sg.Button(prvky[19], key="_Misto_19_")],
                    [sg.Button(prvky[20], key="_Misto_20_"), sg.Button(prvky[21], key="_Misto_21_"), sg.Button(prvky[22], key="_Misto_22_"), sg.Button(prvky[23], key="_Misto_23_"), sg.Button(prvky[24], key="_Misto_24_"), sg.Button(prvky[25], key="_Misto_25_"), sg.Button(prvky[26], key="_Misto_26_"), sg.Button(prvky[27], key="_Misto_27_"), sg.Button(prvky[28], key="_Misto_28_"), sg.Button(prvky[29], key="_Misto_29_")],
                    [sg.Button(prvky[30], key="_Misto_30_"), sg.Button(prvky[31], key="_Misto_31_"), sg.Button(prvky[32], key="_Misto_32_"), sg.Button(prvky[33], key="_Misto_33_"), sg.Button(prvky[34], key="_Misto_34_"), sg.Button(prvky[35], key="_Misto_35_"), sg.Button(prvky[36], key="_Misto_36_"), sg.Button(prvky[37], key="_Misto_37_"), sg.Button(prvky[38], key="_Misto_38_"), sg.Button(prvky[39], key="_Misto_39_")],
                    [sg.Button(prvky[40], key="_Misto_40_"), sg.Button(prvky[41], key="_Misto_41_"), sg.Button(prvky[42], key="_Misto_42_"), sg.Button(prvky[43], key="_Misto_43_"), sg.Button(prvky[44], key="_Misto_44_"), sg.Button(prvky[45], key="_Misto_45_"), sg.Button(prvky[46], key="_Misto_46_"), sg.Button(prvky[47], key="_Misto_47_"), sg.Button(prvky[48], key="_Misto_48_"), sg.Button(prvky[49], key="_Misto_49_")],
                    [sg.Button(prvky[50], key="_Misto_50_"), sg.Button(prvky[51], key="_Misto_51_"), sg.Button(prvky[52], key="_Misto_52_"), sg.Button(prvky[53], key="_Misto_53_"), sg.Button(prvky[54], key="_Misto_54_"), sg.Button(prvky[55], key="_Misto_55_"), sg.Button(prvky[56], key="_Misto_56_"), sg.Button(prvky[57], key="_Misto_57_"), sg.Button(prvky[58], key="_Misto_58_"), sg.Button(prvky[59], key="_Misto_59_")],
                    [sg.Button(prvky[60], key="_Misto_60_"), sg.Button(prvky[61], key="_Misto_61_"), sg.Button(prvky[62], key="_Misto_62_"), sg.Button(prvky[63], key="_Misto_63_"), sg.Button(prvky[64], key="_Misto_64_"), sg.Button(prvky[65], key="_Misto_65_"), sg.Button(prvky[66], key="_Misto_66_"), sg.Button(prvky[67], key="_Misto_67_"), sg.Button(prvky[68], key="_Misto_68_"), sg.Button(prvky[69], key="_Misto_69_")],
                    [sg.Button(prvky[70], key="_Misto_70_"), sg.Button(prvky[71], key="_Misto_71_"), sg.Button(prvky[72], key="_Misto_72_"), sg.Button(prvky[73], key="_Misto_73_"), sg.Button(prvky[74], key="_Misto_74_"), sg.Button(prvky[75], key="_Misto_75_"), sg.Button(prvky[76], key="_Misto_76_"), sg.Button(prvky[77], key="_Misto_77_"), sg.Button(prvky[78], key="_Misto_78_"), sg.Button(prvky[79], key="_Misto_79_")],
                    [sg.Button(prvky[80], key="_Misto_80_"), sg.Button(prvky[81], key="_Misto_81_"), sg.Button(prvky[82], key="_Misto_82_"), sg.Button(prvky[83], key="_Misto_83_"), sg.Button(prvky[84], key="_Misto_84_"), sg.Button(prvky[85], key="_Misto_85_"), sg.Button(prvky[86], key="_Misto_86_"), sg.Button(prvky[87], key="_Misto_87_"), sg.Button(prvky[88], key="_Misto_88_"), sg.Button(prvky[89], key="_Misto_89_")],
                    [sg.Button(prvky[90], key="_Misto_90_"), sg.Button(prvky[91], key="_Misto_91_"), sg.Button(prvky[92], key="_Misto_92_"), sg.Button(prvky[93], key="_Misto_93_"), sg.Button(prvky[94], key="_Misto_94_"), sg.Button(prvky[95], key="_Misto_95_"), sg.Button(prvky[96], key="_Misto_96_"), sg.Button(prvky[97], key="_Misto_97_"), sg.Button(prvky[98], key="_Misto_98_"), sg.Button(prvky[99], key="_Misto_99_")]]

    window_misto = sg.Window("GrafySouveti - pozice prvku", layout_misto)

    event1, values1 = window_misto.read()
    window_misto.close()


def konec(crash=True):
    """
    Ukončí program
    
    Argumenty:

    crash -- výchozí False, pokud True vyhodí chybovou hlášku s kontaktem a ukončí program s nenulovým chybovým kódem
            pokud False, Vyhodí hlášku s poděkováním a zavře program s nulovým chybovým kódem
    """
    if crash:
        msg_crash = "A jéje, toho jsme se báli.\nProgram selhal a musel se ukončit.\nMůžete to zkusit znovu, nebo využijte emailového kontaktu\norangeorange0123+gs@disroot.org"
        print(msg_crash)
        playsound("ajeje.mp3")
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
