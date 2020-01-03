import bullet,gun
MAP_SIZE = (500, 500)
FOG_UPDATE_INTERVAL = 2
TOUCH_FOG_DAMAGE = 10
hpmax=10000
bar_width=240
bar_height=30
keyPressCoolTime = 0.3 # seconds
playerStepSize = 3
'''
name
cd:countdown time
nop:number of projectiles
damage:damage of one projectile
rop:radius of projectiles
rod:radius of damage
ang:spreading angle
bul_gif:image of bullets
'''
poor_gun=		lambda ratio, pos, dir, owner_name:bullet.bullet('Poor Gun'			,1.5	,1	,600,240,20,0,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
bomber=			lambda ratio, pos, dir, owner_name:bullet.bullet('Bomber'			,5		,1	,1600,280,20,0,'circle',ratio, pos, dir, 5, owner = owner_name)
musket=			lambda ratio, pos, dir, owner_name:bullet.bullet('Musket'			,1.1	,1	,1600,280,20,0,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
three_muskets=	lambda ratio, pos, dir, owner_name:bullet.bullet('Three Muskets'	,3		,3	,1600,260,20,30,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
dart_goblin=	lambda ratio, pos, dir, owner_name:bullet.bullet('Dart Goblin'		,0		,1	,1000,360,2,0,'dart',ratio, pos, dir, 0, owner = owner_name)
electro_wizard=	lambda ratio, pos, dir, owner_name:bullet.bullet('Electro Wizard'	,2.2	,1	,300,220/0.819152,20,0,'triangle',ratio, pos, dir, 2, owner = owner_name)
sparky=			lambda ratio, pos, dir, owner_name:bullet.bullet('Sparky'			,6		,1	,2500,180,20,0,'electrify',ratio, pos, dir, 0, owner = owner_name)
hunter=			lambda ratio, pos, dir, owner_name:bullet.bullet('Hunter'			,2.2	,7	,800,190,20,90,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
wizard=			lambda ratio, pos, dir, owner_name:bullet.bullet('Wizard'			,2.2	,1	,1000,280,50,0,'fireball',ratio, pos, dir, 0, owner = owner_name)
ice_wizard=		lambda ratio, pos, dir, owner_name:bullet.bullet('Ice Wizard'		,2.2	,1	,400,220,20,0,'snowball',ratio, pos, dir, 7, owner = owner_name)

POOR_GUN=		lambda:gun.gun('Poor Gun')
BOMBER=			lambda:gun.gun('Bomber')
MUSKET=			lambda:gun.gun('Musket')
THREE_MUSKETS=	lambda:gun.gun('Three Muskets')
DART_GOBLIN=	lambda:gun.gun('Dart Goblin')
ELECTRO_WIZARD=	lambda:gun.gun('Electro Wizard')
SPARKY=			lambda:gun.gun('Sparky')
HUNTER=			lambda:gun.gun('Hunter')
WIZARD=			lambda:gun.gun('Wizard')
ICE_WIZARD=		lambda:gun.gun('Ice Wizard')
GUN_LIST=[POOR_GUN,BOMBER,MUSKET,THREE_MUSKETS,DART_GOBLIN,ELECTRO_WIZARD,SPARKY,HUNTER,WIZARD,ICE_WIZARD]
