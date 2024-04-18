from subprocess import run, PIPE
run(["pip3", "install","pytz"])
import pytz
import datetime

data = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
print(data)
data = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(data)

data_oslo = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
data_sp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
print(data_oslo)
print(data_sp)

espera = 30
data_atual = datetime.datetime.now()
estimativa = data_atual + datetime.timedelta(minutes=espera)
print(f"Começou em:\t {data_atual} e terminara em:\t {estimativa}")
print(estimativa.date())
print(estimativa.time())

data_str = "2024-1-5 5:5"
mascara_ptbr = "%d/%m/%Y %a %H:%M:%S"
mascara_en = "%Y-%m-%d %H:%M"
data_atual_str = data_atual.strftime(mascara_ptbr)
data = datetime.datetime.strptime(data_str, mascara_en)
print(data_atual_str)
print(data)
print(type(data))