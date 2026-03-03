import json
from pathlib import Path
from typing import Any

from generacion_de_datos import generar_datos

ARCHIVO_SALIDA = "candidatos.json"


def main():
    directorio = Path("data/hojas-vida")
    rutas = sorted(directorio.glob("*.pdf"))
    total = len(rutas)

    candidatos: list[dict[str, Any]] = []

    for i, ruta in enumerate(rutas, start=1):
        print(f"Procesando {i}/{total}: {ruta.name}")

        datos = generar_datos(str(ruta))
        datos["archivo_fuente"] = ruta.stem

        candidatos.append(datos)

    salida = Path(ARCHIVO_SALIDA)
    salida.write_text(
        json.dumps(candidatos, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\nArchivo generado: {salida} ({total} candidatos)")


if __name__ == "__main__":
    main()
