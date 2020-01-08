import bullet,gun
MAP_SIZE = (500, 500)
FOG_UPDATE_INTERVAL = 5
TOUCH_FOG_DAMAGE = 100
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
poor_gun=		lambda ratio, pos, dir, owner_name:bullet.bullet('Poor Gun'			,1.5	,1	,1200,170,20,0,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
bomber=			lambda ratio, pos, dir, owner_name:bullet.bullet('Bomber'			,4		,1	,2800,220,20,0,'circle',ratio, pos, dir, 5, owner = owner_name)
musket=			lambda ratio, pos, dir, owner_name:bullet.bullet('Musket'			,1.1	,1	,3200,220,20,0,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
three_muskets=	lambda ratio, pos, dir, owner_name:bullet.bullet('Three Muskets'	,2.8		,3	,3200,220,20,30,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
dart_goblin=	lambda ratio, pos, dir, owner_name:bullet.bullet('Dart Goblin'		,0.5		,1	,1400,360,20,0,'dart',ratio, pos, dir, 0, owner = owner_name)
electro_wizard=	lambda ratio, pos, dir, owner_name:bullet.bullet('Electro Wizard'	,3	,1	,1400,180/0.819152,20,0,'triangle',ratio, pos, dir, 2, owner = owner_name)
sparky=			lambda ratio, pos, dir, owner_name:bullet.bullet('Sparky'			,5		,1	,3500,180,20,0,'electrify',ratio, pos, dir, 0, owner = owner_name)
hunter=			lambda ratio, pos, dir, owner_name:bullet.bullet('Hunter'			,2.5	,7	,1400,110,20,90,'poor_gun',ratio, pos, dir, 0, owner = owner_name)
wizard=			lambda ratio, pos, dir, owner_name:bullet.bullet('Wizard'			,2	,1	,2400,250,50,0,'fireball',ratio, pos, dir, 0, owner = owner_name)
ice_wizard=		lambda ratio, pos, dir, owner_name:bullet.bullet('Ice Wizard'		,2.2	,1	,1400,220,50,0,'snowball',ratio, pos, dir, 7, owner = owner_name)

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
GUN_LIST=[
	{'func': POOR_GUN, 'name': 'Poor Gun'},
	{'func': MUSKET, 'name': 'Musket'},
	{'func': THREE_MUSKETS, 'name': 'Three Muskets'},
	{'func': DART_GOBLIN, 'name': 'Dart Goblin'},
	{'func': ELECTRO_WIZARD, 'name': 'Electro Wizard'},
	{'func': BOMBER, 'name': 'Bomber'},
	{'func': SPARKY, 'name': 'Sparky'},
	{'func': HUNTER, 'name': 'Hunter'},
	{'func': WIZARD, 'name': 'Wizard'},
	{'func': ICE_WIZARD, 'name': 'Ice Wizard'}]
PROPS_LIST=['ATK+','DEF+','HEAL']
description=['爛到爆的槍','火槍，高傷射擊','三個火槍，超值選擇','吹箭手，吹得快','閃電，嗯(?)','發射炸彈，蹦泵绷！','高能注意！超級痛！','散彈槍，近距離痛到炸!','噴射巨~~~型火球','冷凍槍阿很難懂嗎幹嘛圖示','增加傷害5~15%(圖小→大)','增加防禦5~15%(圖小→大)','增加血量1000~2000(圖小→大)']
