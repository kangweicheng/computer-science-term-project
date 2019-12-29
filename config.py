import bullet
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
eff:special effects('Electrify':stuck,'Panic':keyboard out of order,'Freeze':slowed down 50%)
bul_gif:image of bullets
traj_col:color of trajectories
'''
bpoor_gun=bullet.bullet('Poor Gun',1.5,1,600,120,20,0,None,'dark grey','poor_gun.gif')
bbomber=bullet.bullet('Bomber',3,1,400,140,20,0,'Panic','orange','fireball.gif')
bmusket=bullet.bullet('Musket',1.1,1,1600,140,20,0,None,'plum','poor_gun.gif')
bthree_muskets=bullet.bullet('Three Muskets',3,3,1600,140,20,30,None,'plum','poor_gun.gif')
bdart_goblin=bullet.bullet('Dart Goblin',0,3,1000,180,2,0,None,'lawn green','poor_gun.gif')
belectro_wizard=bullet.bullet('Electro Wizard',2.2,1,300,110,20,0,'Electrify','light sky blue','electrify.gif')
bsparky=bullet.bullet('Sparky',6,1,2500,90,20,0,None,'yellow','electrify.gif')
bhunter=bullet.bullet('Hunter',2.2,7,850,110,20,90,None,'slate grey','poor_gun.gif')
bwizard=bullet.bullet('Wizard',2.2,1,1000,140,50,0,None,'salmon','wizard.gif')
bice_wizard=bullet.bullet('Ice Wizard',2.2,1,400,110,20,0,'Freeze','azure','snowball.gif')
