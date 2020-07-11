class Sport():
    def __init__(self, name, num_players, outside):
        self.name = name
        self.num_players = num_players
        self.outside = outside
        

        def is_outside(self):
            if self.outside == True:
                print(f'{self.name} is played outside.')
            else:
                print(f'{self.name} is played inside.')


if __name__ == '__main__':
    
    footy = Sport('footy', 11, True)
    breakpoint()