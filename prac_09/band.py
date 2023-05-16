class Band():
    def __init__(self, name):
        self.name = name
        self.band_members = []

    def add(self, musician):
        self.band_members.append(musician)

    def play(self):
        outlist = []
        for musician in self.band_members:
            if not musician.instruments:
                #outlist.append(f"{musician.name} needs an instrument")
                print(f"{musician.name} needs an instrument")
            else:
                #outlist.append(f"{musician.name} is playing: {musician.instruments[0]}")
                print(f"{musician.name} is playing: {musician.instruments[0]}")

        #return outlist



    def __str__(self):
        out = f"{self.name} ("
        for member in self.band_members:
            out += str(member)
        out += ")"
        return out



if __name__ == '__main__':
    from musician import Musician
