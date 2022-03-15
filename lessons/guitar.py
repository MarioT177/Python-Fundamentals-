class Guitar:
    def __init__(self, guitar_type, tuner_color, guitar_color, guitar_brand):
       self._guitar_type = guitar_type
       self._tuner_color = tuner_color
       self._guitar_color = guitar_color
       self._guitar_brand = guitar_brand

    def door_open_close(self):
        print(str.format('The {0} guitar is', self._guitar_brand))

    @property
    def guitar_type(self):
        return self._guitar_type

    @guitar_type.setter
    def guitar_type(self, model):
        self._guitar_type=model

    @property
    def tuner_color(self):
        return self._tuner_color

    @tuner_color.setter
    def tuner_color(self, color):
        self._tuner_color = color

    @property
    def guitar_color(self):
        return self._guitar_color

    @guitar_color.setter
    def guitar_color(self, color):
        self._guitar_color = color

    @property
    def guitar_brand(self):
        return self._guitar_brand

    @guitar_brand.setter
    def guitar_brand(self, brand):
        self._guitar_brand = brand



my_guitar = Guitar('bass', 'black', 'red', 'Yamaha')
print(my_guitar.guitar_color)
print(my_guitar._guitar_brand)









