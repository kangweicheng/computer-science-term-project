import gun
MAP_SIZE = (500, 500)
FOG_UPDATE_INTERVAL = 1
TOUCH_FOG_DAMAGE = 1
hpmax=10000
bar_width=240
bar_height=30
keyPressCoolTime = 0.3 # seconds
'''
name
cd:countdown time
nop:number of projectiles
dop:damage of one projectile
rop:radius of projectiles
rod:radius of damage
ang:spreading angle
eff:special effects('Electrify':stuck for 1s,'Panic':keyboard go out of order for 2s,'Freeze':slowed down 50% for 5s)
gun_gif:image of the gun
bul_gif:image of bullets
traj_col:color of trajectories
'''
poor_gun=gun.gun('Poor Gun',1.5,1,600,120,20,0,None,'dark grey')
bomber=gun.gun('Bomber',3,1,400,140,20,0,'Panic','orange')
musket=gun.gun('Musket',1.1,1,1600,140,20,0,None,'plum')
three_muskets=gun.gun('Three Muskets',3,3,1600,140,20,30,None,'plum')
dart_goblin=gun.gun('Dart Goblin',0,3,1000,180,2,0,None,'lawn green')
electro_wizard=gun.gun('Electro Wizard',2.2,1,300,110,20,0,'Electrify','light sky blue')
sparky=gun.gun('Sparky',6,1,2500,90,20,0,None,'yellow')
hunter=gun.gun('Hunter',2.2,7,850,110,20,90,None,'slate grey')
wizard=gun.gun('Wizard',2.2,1,1000,140,50,0,None,'salmon')
ice_wizard=gun.gun('Ice Wizard',2.2,1,400,110,20,0,'Freeze','azure')
GUN_LIST=[poor_gun,bomber,musket,three_muskets,dart_goblin,electro_wizard,sparky,hunter,wizard,ice_wizard]