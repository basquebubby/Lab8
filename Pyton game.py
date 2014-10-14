import random
playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30
print "A monster approaches! Prepare to fight!"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
while monsterHealth > 0:
    print "You have " + str(playerHealth) + " health."
    print "The monster has " + str(monsterHealth) + " health."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "What attack do you wish to use?"
    print "1 - Punch    2 - Sword    3 - Fireball"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    attack = int(raw_input())
    if attack == 1:
        print "You punched the monster with your fist!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        monsterHealth = int(monsterHealth) - int(punchDmg)
    if attack == 2:
        print "You swing at the monster with your sword!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        monsterHealth = int(monsterHealth) - int(swordDmg)
    if attack == 3:
        print "You set the monster ablaze!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        monsterHealth = int(monsterHealth) - int(fireballDmg)
    damageByMonster = random.randint(1,35)
    playerHealth = int(playerHealth) - int(damageByMonster)
    if playerHealth <= 0:
        print "The monster defeated you. Try again!"
        monsterHealth == -1
if playerHealth > 0:
    print "You defeat the evil monster!! Hooray!!"