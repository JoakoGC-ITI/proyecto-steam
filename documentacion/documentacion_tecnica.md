# Documentación Técnica

*Fecha: XX de noviembre de 2026*

Este documento contiene la documentación técnica para el proyecto STEAM del curso **Laboratorio STEAM+** de la tecnicatura **Redes y Software** del **Instituto Tecnologico de Infórmatica** de **UTU** año 2026.

# Proyecto: Contenedor de basura automatico

## 1. Integrantes
- Joaquin Garcia
- Federico Bardecio
- Pablo Puerto
- Luis Guarguana

## 2. Descripción
El proyecto busca desarrollar un contenedor de basura inteligente diseñado para optimizar la gestión de residuos y promover un uso más eficiente e higiénico. El sistema central es gestionado por una placa programable MicroBit, la cual procesa las señales de los sensores y coordina las respuestas mecánicas en tiempo real.

Para garantizar una experiencia sin contacto, el contenedor cuenta con un sensor de proximidad que detecta al usuario, activando un servomotor para abrir la tapa de forma automática. Una vez que la persona sale del campo de detección, el sistema espera un lapso de 3 segundos antes de volver a cerrar la tapa de forma segura.

Además, el dispositivo incorpora un sensor de obstáculos interno que monitorea la capacidad del recipiente. Si se detecta que el contenedor está lleno, la MicroBit envía la orden de bloquear el servomotor, impidiendo que la tapa se vuelva a abrir para evitar el desborde y la sobrecarga de residuos.

- [Realizar una descripción general del proyecto en dos o tres párrafos]
- [Formular el problema que se busca resolver y describir la solución]

## 3. Materiales
- [Listar los materiales usados por el proyecto]

## 4. Diseño Mecánico
- [Realizar una descripción de como funciona la solución a nivel mecánico]
- [¿Cómo se arma la solución? Incluir instrucciones de ensamblaje]
  - [Sugerencia: inspirarse en la forma como https://www.instructables.com detalla el armado de un proyecto]
- [Incluir fotografías ilustrativas]

## 5. Diseño Electrónico
- [Realizar una descripción de como funciona la solución a nivel electrónico]
- [Incluir diagramas de Tinkercad mostrando los componentes electrónicos y como van conectados]

## 6. Diseño Software
- [Realizar una descripción de como funciona la solución a nivel de software]
- [Explicar los bloques de código más importantes de la solución programada]
- [Incluir código fuente de python (u otro lenguaje)]
  - [El código debe almacenarse en una carpeta dentro del repositorio]
  - [Sugerencia: almacenar el código en diferentes etapas para mostrar su evolución]

## 7. Referencias y recursos
- [Documentacion sobre pines del microBit](https://makecode.microbit.org/device/pins)

## 8. Otros
[Incluir cualquier otra información que consideren relevante para el proyecto]

## Nota
En este enlace encontrarás un [ejemplo como debe completarse la documentación técnica](documentacion_tecnica_ejemplo.md).
