import requests
import random
import webbrowser
from pokemon_class import *

def create_pokemon(mon_num):
      # abre la url api para el pokémon creado al azar
      link = str(f"https://pokeapi.co/api/v2/pokemon/{mon_num}/")
      response = requests.get(link)
      response = response.json()
      mon_nombre = response['nombre']
      sprite = response['sprites']['front_default']
      mon_type = str()
      abi = str()
      gen = int

      # pasa por todos los tipos que tiene el pokémon y los agrega a la cadena
      for type in response['types']:
            mon_type += f" {type['type']['nombre']} "

      # pasa por todas las habilidades que el pokémon podría tener y las agrega a una cadena
      for abilidad in response['abilidades']:
            abi += f" {abilidad['abilidad']['nombre']} "

      # Codificado una fuerza brutal para la generación
      if mon_num<152: gen = 1
      elif mon_num>151 and mon_num<252: gen = 2
      elif mon_num>251 and mon_num<387: gen = 3
      elif mon_num>386 and mon_num<494: gen = 4
      elif mon_num>493 and mon_num<650: gen = 5
      elif mon_num>649 and mon_num<722: gen = 6
      elif mon_num>721 and mon_num<810: gen = 7
      elif mon_num>809 and mon_num<899: gen = 8

      return Pokemon(mon_nombre, mon_num, mon_type, abi, gen, sprite)


def game():
    # crea un pokémon aleatorio basado en rng
    index = random.randint(1, 898)
   
    # variables:
    round = 1
    playing = True
    prev_guess = str()
    mon = create_pokemon(index)
   
    format_nombre = "_ " * len(mon.get_nombre())

    # comenzando el juego de terminal en bucle
    while playing:
        print(f"\n\nRound {round}")

        # cada ronda representa un conjunto de pistas y las pistas se sumarán y cambiarán con cada suposición incorrecta
        # las pistas se volverán a imprimir para cada ronda con más pistas dependiendo de la ronda.
        if round >= 1:
            print(f"Nombre: {format_nombre}")
            print(f"Generacion: {mon.get_gen()}") 
            print(f"Abilidad: {mon.get_abilidad()}")
            format_nombre = mon.get_nombre()[0].capitalize() + " -" * (len(mon.get_nombre()) - 1) 
        
        if round >= 2:
            print(f"Type: {mon.get_type()}") 
            print(f"Index: {mon.get_num()}")
            print(f"Conjeturas anteriores:{prev_guess}")

        if round == 3:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(mon.get_sprite())
        
        guess = str(input("\nQuien es ese pokemon?:  ")).lower()
        prev_guess += f" {guess}."
        if round > 1:
            prev_guess = prev_guess[:-1].replace(".", ",") + "."

        if guess == mon.ret_nombre():
            print(f"Así es, el pokémon era {mon.get_nombre().capitalize()}") 
            cont = str(input("¿Quieres seguir jugando?:  "))
            if cont.lower() in ["Sí", "si", "s", "Si", "S", "continuar", "c", "cont"]:
                game()        
            else:
                break

        if round == 5:
            print(f"Perdiste. el pokemon era {mon.get_nombre().capitalize()}")
            cont = str(input("¿Quieres seguir jugando?:  "))
            if cont.lower() in ["Sí", "si", "s", "Si", "S", "continuar", "c", "cont"]:
                game()
            else:
                break
        round += 1


def main():
      play = str(input("¿Quieres jugar?:    "))

      if play.lower() in ["Sí", "si", "s", "Si", "S"]:
            print('Esto es "¡Adivina cual es el Pokémon!"')
            game()

      else: 
            print("De acuerdo, entonces esto va a dar miedo, ¿por qué empezaste el programa?")


main()
