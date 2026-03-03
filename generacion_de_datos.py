from concurrent.futures import ThreadPoolExecutor
from typing import Any

from extraccion_de_texto import extraer_secciones, extraer_texto, limpiar_texto
from extraccion_estructurada import (
    extraer_bienes,
    extraer_educacion,
    extraer_experiencia_laboral,
    extraer_informacion_personal,
    extraer_sentencias_judiciales,
)


def generar_datos(ruta: str) -> dict[str, Any]:
    texto = extraer_texto(ruta)
    texto_limpio = limpiar_texto(texto)
    texto_en_secciones = extraer_secciones(texto_limpio)

    extractores = [  # type: ignore
        extraer_informacion_personal,
        extraer_experiencia_laboral,
        extraer_educacion,
        extraer_sentencias_judiciales,
        extraer_bienes,
    ]

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [  # type: ignore
            (fn.__name__, executor.submit(fn, texto_en_secciones))  # type: ignore
            for fn in extractores  # type: ignore
        ]
        resultados = []
        for nombre, future in futures:  # type: ignore
            try:
                resultados.append(future.result())  # type: ignore
            except Exception as e:
                print(f"[ERROR] Excepción inesperada en '{nombre}': {e}")
                resultados.append(None)  # type: ignore

    objecto: dict[str, Any] = {}
    for resultado in resultados:  # type: ignore
        if resultado is not None:
            objecto.update(resultado.model_dump())  # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]

    return objecto
