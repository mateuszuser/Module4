import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile_kalkulator.log")

def dodaj (x, y):
  return x+y
def odejmij(x, y):
  return x-y
def pomnoz (x, y):
  return x*y
def podziel (x, y):
  return x/y
print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
choice=input()


if choice == '1':
    num1 = float(input("Podaj skladnik 1.: "))
    num2 = float(input("Podaj skladnik 2.: "))
    logging.info(f"wykonujemy działanie nr {choice}, argumenty tego działania to {num1} i {num2}")
    print("Wynik to", dodaj(num1,num2))
elif choice =='2':
    num1 = float(input("Podaj skladnik 1.: "))
    num2 = float(input("Podaj skladnik 2.: "))
    logging.info(f"wykonujemy działanie nr {choice}, argumenty tego działania to {num1} i {num2}")
    print("Wynik to", odejmij(num1,num2))
elif choice =='3':
    num1 = float(input("Podaj skladnik 1.: "))
    num2 = float(input("Podaj skladnik 2.: "))
    logging.info(f"wykonujemy działanie nr {choice}, argumenty tego działania to {num1} i {num2}")
    print("Wynik to", pomnoz(num1,num2))
elif choice =='4':
    num1 = float(input("Podaj skladnik 1.: "))
    num2 = float(input("Podaj skladnik 2.: "))
    logging.info(f"wykonujemy działanie nr {choice}, argumenty tego działania to {num1} i {num2}")
    print("Wynik to", podziel(num1,num2))
else:
    print("Niepoprawna wartość")