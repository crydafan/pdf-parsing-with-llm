import json

from extraccion_de_texto import extraer_secciones, extraer_texto, limpiar_texto
from extraccion_estructurada import (
    extraer_bienes,
    extraer_educacion,
    extraer_experiencia_laboral,
    extraer_informacion_personal,
    extraer_sentencias_judiciales,
)


def main():
    ruta = "data/hojas-vida/alfonso-lopez-chau-nava.pdf"

    texto = extraer_texto(ruta)
    texto_limpio = limpiar_texto(texto)
    texto_en_secciones = extraer_secciones(texto_limpio)

    objecto = {}

    candidato = extraer_informacion_personal(texto_en_secciones)
    if not candidato:
        print("No se pudo extraer la información personal.")
        return
    # print(candidato.model_dump_json(indent=2))

    experiencias_laborales = extraer_experiencia_laboral(texto_en_secciones)
    if not experiencias_laborales:
        print("No se pudo extraer la experiencia laboral.")
        return
    # print(experiencias_laborales.model_dump_json(indent=2))

    estudios = extraer_educacion(texto_en_secciones)
    if not estudios:
        print("No se pudieron extraer los estudios.")
        return
    # print(estudios.model_dump_json(indent=2))

    juicios = extraer_sentencias_judiciales(texto_en_secciones)
    if not juicios:
        print("No se pudieron extraer las sentencias judiciales.")
        return

    bienes = extraer_bienes(texto_en_secciones)
    if not bienes:
        print("No se pudieron extraer los bienes.")
        return
    # print(bienes.model_dump_json(indent=2))

    objecto.update(candidato.model_dump())  # pyright: ignore[reportUnknownMemberType]
    objecto.update(experiencias_laborales.model_dump())  # pyright: ignore[reportUnknownMemberType]
    objecto.update(estudios.model_dump())  # pyright: ignore[reportUnknownMemberType]
    objecto.update(juicios.model_dump())  # pyright: ignore[reportUnknownMemberType]
    objecto.update(bienes.model_dump())  # pyright: ignore[reportUnknownMemberType]

    print(json.dumps(objecto, indent=2))


if __name__ == "__main__":
    main()
