class Enemy(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.yVel = 0
        self.xVel = 2 # start moving immediately
        self.image = Surface((32,32))
        self.image.fill(Color("#00FF00"))
        self.image.convert()
        self.rect = Rect(300, 1200, 32, 32)
        self.onGround = False

    def update(self, platforms):
        if not self.onGround:
            self.yVel += 0.3

        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0

        # create a point at our left (or right) feet
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1

        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0:
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0:
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom
