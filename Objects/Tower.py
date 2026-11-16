class Tower:
    def __init__(self, health, level, x, y, heading):
        self.health = health
        self.level = level
        self.x = x
        self.y = y
        self.heading = heading

    def draw(self, win):
        win.blit(self, (self.x, self.y))

    def turn_to():
        pass
    # Leo will do all the math for this

    def upgrade_status(self):
        self.level += 1

#will probaby add more for when selected on side bar what will it do
# will have one function to detect if that happened or not, another to see what to do with that info
#maybe make a whole other class just for the sidebar
    

    