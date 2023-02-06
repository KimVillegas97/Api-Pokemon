class Pokemon():
    def __init__(self, nombre, pokedex_index, type, abilidad, generation, sprite):
        self.nombre = nombre
        self.num = pokedex_index
        self.type = type
        self.abilidad = abilidad
        self.gen = generation
        self.png = sprite

    def get_nombre(self):
        return self.nombre

    def get_num(self):
        return self.num

    def get_type(self):
        ret_string = self.type.replace("  ", ", ")
        return ret_string

    def get_abilidad(self):
        ret_string = self.abilidad.replace("  ", ", ")
        return ret_string

    def get_gen(self):
        return self.gen

    def get_sprite(self):
        return self.png
