
# Controle Automático de Cooler no Rock Pi 4

## Objetivo
Automatizar o controle de um cooler 5V no Rock Pi 4 baseado na temperatura da CPU, utilizando um transistor 2N2222 e controle por GPIO via script Python.

## Materiais Necessários
- Rock Pi 4
- Cooler 5V
- Transistor 2N2222
- Resistor 1kΩ
- Fios de conexão
- Fonte de alimentação (pelo próprio Rock Pi 4)

## Instalação de Dependências

De acordo com a documentação oficial: https://wiki.radxa.com/Gpiod

Execute no terminal:

```bash
sudo apt update
sudo apt install gpiod -y
```

## Diagrama Elétrico
Rock Pi 5V (Pino 2) ── (+) Cooler ── [Coletor] 2N2222 [Emissor] ── Rock Pi GND (Pino 6)
Base do 2N2222 ── Resistor 1kΩ ── Rock Pi GPIO (Pino 18 - GPIO156)

## Instalação do Script
1. Copie os arquivos para `/home/ihuri/scripts/`.
2. Torne o script executável:
   ```bash
   chmod +x /home/ihuri/scripts/cooler_control.py
   ```
3. Instale o serviço:
   ```bash
   sudo cp cooler_control.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable cooler_control.service
   sudo systemctl start cooler_control.service
   ```
4. Verifique o status:
   ```bash
   sudo systemctl status cooler_control.service
   ```

## Funcionamento
- Liga o cooler a 50°C ou mais
- Desliga o cooler abaixo de 39°C


## Tabela de Pinagem Rock Pi 4
Fonte: https://wiki.radxa.com/Rockpi4/hardware/gpio

| GPIO number | Function2 | Function1 | GPIO    | Pino# |    | Pino# | GPIO    | Function1 | Function2 | GPIO number |
|:-----------:|:---------:|:---------:|:-------:|:-----:|:--:|:-----:|:-------:|:---------:|:---------:|:-----------:|
| +3.3V       |           |           |         | 1     |    | 2     |         |           | +5.0V     |             |
| 71          |           | I2C7_SDA  | GPIO2_A7| 3     |    | 4     |         |           | +5.0V     |             |
| 72          |           | I2C7_SCL  | GPIO2_B0| 5     |    | 6     |         |           | GND       |             |
| 75          | SPI2_CLK  |           | GPIO2_B3| 7     |    | 8     | GPIO4_C4| UART2_TXD |           | 148         |
| GND         |           |           |         | 9     |    | 10    | GPIO4_C3| UART2_RXD |           | 147         |
| 146         | PWM0      |           | GPIO4_C2| 11    |    | 12    | GPIO4_A3| I2S1_SCLK |           | 131         |
| 150         | PWM1      |           | GPIO4_C6| 13    |    | 14    |         |           | GND       |             |
| 149         | SPDIF_TX  |           | GPIO4_C5| 15    |    | 16    | GPIO4_D2|           |           | 154         |
| +3.3V       |           |           |         | 17    |    | 18    | GPIO4_D4|           |           | 156         |
| 40          | UART4_TXD | SPI1_TXD  | GPIO1_B0| 19    |    | 20    |         |           | GND       |             |
| 39          | UART4_RXD | SPI1_RXD  | GPIO1_A7| 21    |    | 22    | GPIO4_D5|           |           | 157         |
| 41          |           | SPI1_CLK  | GPIO1_B1| 23    |    | 24    | GPIO1_B2| SPI1_CSn  |           | 42          |
| GND         |           |           |         | 25    |    | 26    |         |           | ADC_IN0   |             |
| 64          |           | I2C2_SDA  | GPIO2_A0| 27    |    | 28    | GPIO2_A1| I2C2_CLK  |           | 65          |
| 74          | I2C6_SCL  | SPI2_TXD  | GPIO2_B2| 29    |    | 30    |         |           | GND       |             |
| 73          | I2C6_SDA  | SPI2_RXD  | GPIO2_B1| 31    |    | 32    | GPIO3_C0| SPDIF_TX  | UART3_CTSn| 112         |
| 76          |           | SPI2_CSn  | GPIO2_B4| 33    |    | 34    |         |           | GND       |             |
| 133         |           | I2S1_LRCK_TX|GPIO4_A5| 35    |    | 36    | GPIO4_A4| I2S1_LRCK_RX|         | 132         |
| 158         |           |           | GPIO4_D6| 37    |    | 38    | GPIO4_A6| I2S1_SDI  |           | 134         |
| GND         |           |           |         | 39    |    | 40    | GPIO4_A7| I2S1_SDO  |           | 135         |
