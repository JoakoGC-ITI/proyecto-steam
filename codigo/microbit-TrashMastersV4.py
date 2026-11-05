distancia = 0
angulo_actual = 90

TAPA_CERRADA = 90   # ángulo de tapa cerrada
TAPA_ABIERTA = 20   # ángulo de tapa abierta (máximo)
PASO_MANUAL = 5     # grados por cada pulsación de A o B

# Cara feliz y rotada 180°
def cara_feliz():
    basic.show_leds("""
        . . . . .
        . # # # .
        # . . . #
        . . . . .
        . . . . .
        """)
 # Cara triste y rotada 180°
def cara_triste():
    basic.show_leds("""
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        . . . . .
        """)

def mover_tapa(destino: number):
    global angulo_actual
    paso = 2
    if destino < angulo_actual:
        paso = -2
    for angulo in range(angulo_actual, destino, paso):
        pins.servo_write_pin(AnalogPin.P0, angulo)
        basic.pause(30)
    pins.servo_write_pin(AnalogPin.P0, destino)
    angulo_actual = destino

# Inicia con la tapa cerrada
pins.servo_write_pin(AnalogPin.P0, TAPA_CERRADA)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_UP)

def on_forever():
    global distancia, angulo_actual

    estado_basura = pins.digital_read_pin(DigitalPin.P8)

    # ---------- BASURERO LLENO ----------
    if estado_basura == 0:
        cara_triste()
        if angulo_actual != TAPA_CERRADA:
            mover_tapa(TAPA_CERRADA)

        # Solo se abre si se toca el logo táctil (para vaciarlo)
        if input.logo_is_pressed():
            cara_feliz()
            mover_tapa(TAPA_ABIERTA)
            basic.pause(3000)
            mover_tapa(TAPA_CERRADA)

    # ---------- BASURERO NO LLENO ----------
    else:
        # A = subir tapa (abrir), B = bajar tapa (cerrar)
        if input.button_is_pressed(Button.A):
            angulo_actual = max(TAPA_ABIERTA, angulo_actual - PASO_MANUAL)
            pins.servo_write_pin(AnalogPin.P0, angulo_actual)
        elif input.button_is_pressed(Button.B):
            angulo_actual = min(TAPA_CERRADA, angulo_actual + PASO_MANUAL)
            pins.servo_write_pin(AnalogPin.P0, angulo_actual)

        # Sensor ultrasónico para la mano
        distancia = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)

        if distancia > 0 and distancia <= 10:
            cara_feliz()
            mover_tapa(TAPA_ABIERTA)
            basic.pause(3000)
            mover_tapa(TAPA_CERRADA)
            basic.clear_screen()
        else:
            if not (input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B)):
                basic.clear_screen()

    basic.pause(100)

basic.forever(on_forever)