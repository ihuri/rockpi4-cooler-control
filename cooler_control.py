
import time
import os

# CONFIGURAÇÕES
GPIO_PIN = 156  # Pino físico 18 no Rock Pi 4

GPIO_PATH = f"/sys/class/gpio/gpio{GPIO_PIN}"

def export_gpio(pin):
    if not os.path.exists(GPIO_PATH):
        try:
            with open("/sys/class/gpio/export", "w") as f:
                f.write(str(pin))
            time.sleep(0.2)
        except IOError:
            print(f"Erro ao exportar GPIO{pin}.")

def unexport_gpio(pin):
    if os.path.exists(GPIO_PATH):
        try:
            with open("/sys/class/gpio/unexport", "w") as f:
                f.write(str(pin))
        except IOError:
            print(f"Erro ao desexportar GPIO{pin}.")

def setup_gpio_as_output(pin):
    export_gpio(pin)
    try:
        with open(f"{GPIO_PATH}/direction", "w") as f:
            f.write("out")
    except IOError:
        print(f"Erro ao configurar GPIO{pin} como saída.")

def set_gpio_value(pin, value):
    try:
        with open(f"{GPIO_PATH}/value", "w") as f:
            f.write(str(value))
    except IOError:
        print(f"Erro ao escrever no GPIO{pin}.")

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.readline()
            return int(temp_str) / 1000
    except FileNotFoundError:
        print("Arquivo de temperatura não encontrado.")
        return 0

try:
    setup_gpio_as_output(GPIO_PIN)
    cooler_on = False

    print("Monitorando temperatura... (Ctrl+C para sair)")
    while True:
        temp = get_cpu_temp()
        print(f"Temperatura atual: {temp:.1f}°C")

        if temp >= 50 and not cooler_on:
            print("Temperatura alta! Ligando o cooler.")
            set_gpio_value(GPIO_PIN, 1)
            cooler_on = True

        elif temp < 39 and cooler_on:
            print("Temperatura baixa! Desligando o cooler.")
            set_gpio_value(GPIO_PIN, 0)
            cooler_on = False

        time.sleep(5)

except KeyboardInterrupt:
    print("\nSaindo...")

finally:
    print("Desligando cooler e liberando GPIO...")
    set_gpio_value(GPIO_PIN, 0)
    unexport_gpio(GPIO_PIN)
