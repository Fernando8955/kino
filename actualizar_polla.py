#!/usr/bin/env python3
"""Actualiza kino-polla.json con los últimos sorteos del Kino oficial de Polla Chilena.

Fuente: chileresultados.com (polla.cl bloquea el acceso automatizado).
Se ejecuta a mano al publicar; el sitio lee kino-polla.json.
"""
import json, re, sys, datetime, urllib.request

FUENTE = "https://chileresultados.com"
CUANTOS = 12
MESES = {m: i for i, m in enumerate(
    ["enero","febrero","marzo","abril","mayo","junio","julio",
     "agosto","septiembre","octubre","noviembre","diciembre"], 1)}

def bajar(path):
    req = urllib.request.Request(FUENTE + path, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "ignore")

def parsear(html):
    numero = re.search(r"[Ss]orteo[^0-9]{0,20}(\d{4})", html)
    fecha = re.search(r"(\d{1,2}) de ([a-záé]+) de (\d{4})", html, re.I)
    sec = html[html.find("Sorteo KINO"):]
    nums = [int(n) for n in re.findall(r'bg-warning text-dark">(\d{2})</span>', sec)[:14]]
    if not (numero and fecha and len(nums) == 14 and len(set(nums)) == 14 and all(1 <= n <= 25 for n in nums)):
        raise ValueError("no pude leer un sorteo completo")
    d = datetime.date(int(fecha.group(3)), MESES[fecha.group(2).lower()], int(fecha.group(1)))
    return {"numero": int(numero.group(1)), "fecha": d.isoformat(), "nums": sorted(nums)}

def main():
    ultimo = parsear(bajar("/kino/ultimosorteo"))
    sorteos = {ultimo["numero"]: ultimo}
    n = ultimo["numero"] - 1
    intentos = 0
    while len(sorteos) < CUANTOS and intentos < CUANTOS + 4:
        try:
            s = parsear(bajar(f"/kino/sorteos/{n}"))
            sorteos[s["numero"]] = s
        except Exception:
            pass
        n -= 1; intentos += 1
    salida = {
        "juego": "Kino · Polla Chilena de Beneficencia",
        "fuente": "chileresultados.com",
        "actualizado": datetime.datetime.now().astimezone().isoformat(timespec="minutes"),
        "sorteos": sorted(sorteos.values(), key=lambda x: x["numero"], reverse=True)[:CUANTOS],
    }
    json.dump(salida, open("kino-polla.json", "w"), ensure_ascii=False, indent=2)
    print(f"kino-polla.json: {len(salida['sorteos'])} sorteos · último {ultimo['numero']} del {ultimo['fecha']}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr); sys.exit(1)
