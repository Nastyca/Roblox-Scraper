import os
import json
import ctypes
import random
import requests

from sys import stdout
from colorama import Fore, Style
from pystyle import Colors, Write
from concurrent.futures import ThreadPoolExecutor

os.system("cls")

Write.Print(f"""
  _____                                  _____       _     _           
 / ____|                                |  __ \     | |   | |          
| (___   ___ _ __ __ _ _ __   ___ _ __  | |__) |___ | |__ | | _____  __
 \___ \ / __| '__/ _` | '_ \ / _ \ '__| |  _  // _ \| '_ \| |/ _ \ \/ /
 ____) | (__| | | (_| | |_) |  __/ |    | | \ \ (_) | |_) | | (_) >  < 
|_____/ \___|_|  \__,_| .__/ \___|_|    |_|  \_\___/|_.__/|_|\___/_/\_\ 
                      | |                                              
                      |_|                                              \n""", Colors.blue_to_purple, interval=0)

nombre = 0
valides = 0
invalides = 0

premier_utilisateur = int(input(f"\n{Fore.LIGHTMAGENTA_EX}Premier utilisateur ->{Fore.RESET} "))
dernier_utilisateur = int(input(f"\n{Fore.LIGHTMAGENTA_EX}Dernier utilisateur ->{Fore.RESET} "))
threads = int(input(f"\n{Fore.LIGHTMAGENTA_EX}Threads ->{Fore.RESET} "))
print(f"")

liste_proxies = [
    "be-bru-wg-socks5-103.relays.mullvad.net:1080",
    "be-bru-wg-socks5-101.relays.mullvad.net:1080",
    "fr-par-wg-socks5-004.relays.mullvad.net:1080",
    "fr-mrs-wg-socks5-001.relays.mullvad.net:1080",
    "fr-par-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-404.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-202.relays.mullvad.net:1080",
    "de-ber-wg-socks5-003.relays.mullvad.net:1080",
    "de-ber-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-501.relays.mullvad.net:1080",
    "de-fra-wg-socks5-004.relays.mullvad.net:1080",
    "fr-par-wg-socks5-101.relays.mullvad.net:1080",
    "fr-par-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-505.relays.mullvad.net:1080",
    "de-ber-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-201.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-503.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-506.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-003.relays.mullvad.net:1080",
    "de-fra-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-006.relays.mullvad.net:1080",
    "de-fra-wg-socks5-008.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-401.relays.mullvad.net:1080",
    "de-dus-wg-socks5-003.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-004.relays.mullvad.net:1080",
    "de-fra-wg-socks5-005.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-502.relays.mullvad.net:1080",
    "de-fra-wg-socks5-101.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-507.relays.mullvad.net:1080",
    "de-fra-wg-socks5-103.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-605.relays.mullvad.net:1080",
    "de-fra-wg-socks5-403.relays.mullvad.net:1080",
    "de-fra-wg-socks5-402.relays.mullvad.net:1080",
    "be-bru-wg-socks5-102.relays.mullvad.net:1080",
    "de-fra-wg-socks5-304.relays.mullvad.net:1080",
    "de-fra-wg-socks5-302.relays.mullvad.net:1080",
    "de-fra-wg-socks5-401.relays.mullvad.net:1080",
    "de-fra-wg-socks5-301.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-403.relays.mullvad.net:1080",
    "de-fra-wg-socks5-007.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-504.relays.mullvad.net:1080",
    "fr-par-wg-socks5-003.relays.mullvad.net:1080",
    "de-fra-wg-socks5-303.relays.mullvad.net:1080",
    "at-vie-wg-socks5-001.relays.mullvad.net:1080",
    "be-bru-wg-socks5-101.relays.mullvad.net:1080",
    "at-vie-wg-socks5-003.relays.mullvad.net:1080",
    "bg-sof-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-004.relays.mullvad.net:1080",
    "ca-mtr-wg-socks5-001.relays.mullvad.net:1080",
    "ca-mtr-wg-socks5-003.relays.mullvad.net:1080",
    "sk-bts-wg-socks5-001.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-103.relays.mullvad.net:1080",
    "rs-beg-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-001.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-001.relays.mullvad.net:1080",
    "au-adl-wg-socks5-302.relays.mullvad.net:1080",
    "se-mma-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-404.relays.mullvad.net:1080",
    "de-ber-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-202.relays.mullvad.net:1080",
    "ro-buh-wg-socks5-002.relays.mullvad.net:1080",
    "se-mma-wg-socks5-102.relays.mullvad.net:1080",
    "se-mma-wg-socks5-003.relays.mullvad.net:1080",
    "no-osl-wg-socks5-002.relays.mullvad.net:1080",
    "se-got-wg-socks5-101.relays.mullvad.net:1080",
    "au-syd-wg-socks5-002.relays.mullvad.net:1080",
    "fr-par-wg-socks5-102.relays.mullvad.net:1080",
    "de-fra-wg-socks5-004.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-102.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-105.relays.mullvad.net:1080",
    "au-bne-wg-socks5-302.relays.mullvad.net:1080",
    "no-svg-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-002.relays.mullvad.net:1080",
    "de-dus-wg-socks5-002.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-102.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-505.relays.mullvad.net:1080",
    "au-syd-wg-socks5-001.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-201.relays.mullvad.net:1080",
    "se-sto-wg-socks5-005.relays.mullvad.net:1080",
    "de-ber-wg-socks5-005.relays.mullvad.net:1080",
    "mk-skp-wg-socks5-001.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-102.relays.mullvad.net:1080",
    "se-sto-wg-socks5-009.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-103.relays.mullvad.net:1080",
    "ee-tll-wg-socks5-002.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-503.relays.mullvad.net:1080",
    "lu-lux-wg-socks5-001.relays.mullvad.net:1080",
    "se-sto-wg-socks5-004.relays.mullvad.net:1080",
    "se-got-wg-socks5-003.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-003.relays.mullvad.net:1080",
    "us-uyk-wg-socks5-102.relays.mullvad.net:1080",
    "hr-zag-wg-socks5-001.relays.mullvad.net:1080",
    "fi-hel-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-001.relays.mullvad.net:1080",
    "de-fra-wg-socks5-008.relays.mullvad.net:1080",
    "no-svg-wg-socks5-003.relays.mullvad.net:1080",
    "de-dus-wg-socks5-003.relays.mullvad.net:1080",
    "ca-tor-wg-socks5-104.relays.mullvad.net:1080",
    "se-sto-wg-socks5-001.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-101.relays.mullvad.net:1080",
    "se-sto-wg-socks5-002.relays.mullvad.net:1080",
    "no-osl-wg-socks5-004.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-004.relays.mullvad.net:1080",
    "pl-waw-wg-socks5-201.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-502.relays.mullvad.net:1080",
    "se-sto-wg-socks5-012.relays.mullvad.net:1080",
    "de-fra-wg-socks5-101.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-302.relays.mullvad.net:1080",
    "ee-tll-wg-socks5-003.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-005.relays.mullvad.net:1080",
    "no-osl-wg-socks5-001.relays.mullvad.net:1080",
    "pt-lis-wg-socks5-101.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-001.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-004.relays.mullvad.net:1080",
    "br-sao-wg-socks5-001.relays.mullvad.net:1080",
    "hr-zag-wg-socks5-002.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-201.relays.mullvad.net:1080",
    "no-svg-wg-socks5-002.relays.mullvad.net:1080",
    "ua-iev-wg-socks5-002.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-007.relays.mullvad.net:1080",
    "nl-ams-wg-socks5-006.relays.mullvad.net:1080",
    "us-rag-wg-socks5-105.relays.mullvad.net:1080",
    "cz-prg-wg-socks5-102.relays.mullvad.net:1080",
    "us-uyk-wg-socks5-103.relays.mullvad.net:1080",
    "de-fra-wg-socks5-106.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-005.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-503.relays.mullvad.net:1080",
    "gb-mnc-wg-socks5-006.relays.mullvad.net:1080",
    "us-qas-wg-socks5-002.relays.mullvad.net:1080",
    "se-sto-wg-socks5-011.relays.mullvad.net:1080",
    "gb-lon-wg-socks5-203.relays.mullvad.net:1080",
    "ch-zrh-wg-socks5-507.relays.mullvad.net:1080",
    "us-atl-wg-socks5-202.relays.mullvad.net:1080",
    "us-rag-wg-socks5-102.relays.mullvad.net:1080",
    "us-chi-wg-socks5-002.relays.mullvad.net:1080",
    "de-fra-wg-socks5-103.relays.mullvad.net:1080",
    "us-nyc-wg-socks5-605.relays.mullvad.net:1080",
    "ro-buh-wg-socks5-001.relays.mullvad.net:1080",
]

def scraper(user_id):
    global nombre, valides, invalides
    nombre += 1

    proxy = random.choice(liste_proxies)
    proxies = {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}
    try:
        requete = requests.get(f'https://users.roblox.com/v1/users/{user_id}', proxies=proxies, timeout=5)
        requete.raise_for_status()

        data = requete.json()
        id_ = data.get('id', 'N/A')
        id = f"{id_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        nom_ = data.get('displayName', 'N/A')
        nom = f"{nom_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        pseudo_ = data.get('name', 'N/A')
        pseudo = f"{pseudo_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        creation_ = data.get('created', 'N/A')
        creation = f"{creation_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        est_banni_ = 'Yes' if data.get('isBanned') else 'no'
        est_banni = f"{est_banni_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        badge_ = data.get('hasVerifiedBadge', 'no')
        badge = f"{badge_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        nom_externe_ = data.get('externalAppDisplayName', 'N/A')
        nom_externe = f"{nom_externe_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        description_ = data.get('description', 'N/A')
        description = f"{description_}".replace("|", "").replace("\\", "\\\\").replace('"', "'").replace(",", "")

        resultat = ({"id": id,
                     "display_name": nom,
                     "username": pseudo,
                     "created": creation,
                     "isBanned": est_banni,
                     "hasVerifiedBadge": badge,
                     "externalAppDisplayName": nom_externe,
                     "description": description})

        with open(f"data/users.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(resultat, ensure_ascii=False) + ",\n")
        stdout.write(f"\r{Fore.GREEN}[{Fore.WHITE}ID : {id}{Fore.GREEN}] {Fore.WHITE}> {Fore.GREEN}[{Fore.WHITE}Pseudo : {pseudo[:20]}{Fore.GREEN}] {Fore.WHITE}> {Fore.GREEN}[{Fore.WHITE}Création : {creation}{Fore.GREEN}]{Fore.RESET}    ")
        stdout.flush()
        valides += 1
    except:
        invalides += 1
        pass

    ctypes.windll.kernel32.SetConsoleTitleW(f"Nombre : {nombre} | Valides : {valides} | Invalides : {invalides}")

with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scraper, range(premier_utilisateur, dernier_utilisateur + 1))
