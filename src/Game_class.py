import sys


def main():
    while True:
        get_input()
        return

if __name__ == '__main__':
    sys.exit(main())

import time
import random
def say(noun):
    return 'You said "{}"'.format(noun)


def name_per(noun):
    if noun in GameObject.objects:
        msg = GameObject.objects[noun].name
    else:
        msg = "Name is not found"
    return msg


def stat_show(noun):
    return str(10 * "=" + "\n" + "Name: " + GameObject.objects[noun].name + "\n"
               + 5 * "_" + "\n"
               + "Class: " + GameObject.objects[noun].class_name + "\n"
               + 5 * "_" + "\n"
               + "health: " + str(GameObject.objects[noun].health) + "\n" + 10*"=" + "\n")


def stat(noun):
    msg = ""
    if noun == "all":
        for pers in GameObject.objects:
            msg += stat_show(pers)
    elif noun in GameObject.objects:
        msg = stat_show(noun)
    else:
        msg = "Name is not found"
    return msg


def info(noun):
    st = ""
    for key in verb_dict:
        st += key + "\n"
    return st


def fight(houn):
    for i in range(3):
        ent = input("enter first fighter: ")
        if ent in GameObject.objects:
            fighter1 = ent
            break
        else:
            print("Fighter no found")
        if i == 2:
            return "Увы, таких бойцов нет"
    for i in range(3):
        ent = input("enter second fighter: ")
        if ent in GameObject.objects:
            fighter2 = ent
            break
        else:
            print("Fighter no found")
        if i == 2:
            return "Увы, таких бойцов нет"
    print (fighter1 + " VS " + fighter2)
    time.sleep(1)
    print(20*"_" + "\n" +
        5*' ' + 'Round 1')
    time.sleep(1)
    for i in reversed(range(4)):
        print(".." + str(i))
        time.sleep(1)
    print("!!!FIGHT!!!")
    if GameObject.objects[fighter1].agility > GameObject.objects[fighter2].agility:
        first_fighter, second_fighter = fighter1, fighter2
    elif GameObject.objects[fighter1].agility == GameObject.objects[fighter2].agility:
        x = random.random()
        if x == 1:
            first_fighter, second_fighter = fighter1, fighter2
        else:
            first_fighter, second_fighter = fighter2, fighter1
    else:
        first_fighter, second_fighter = fighter2, fighter1

    print(roun(first_fighter, second_fighter))
    fig1 = GameObject.objects[first_fighter]
    fig2 = GameObject.objects[second_fighter]
    if fig1.health <= 0:
        msg = fig2.class_name + " WIN!!!"
        return msg
    else:
        msg = fig1.class_name + " WIN!!!"
        return msg

    #     print(fighter1 + " VS " + fighter2)
    #     time.sleep(0)
    #     print(20 * "_" + "\n" +
    #           5 * ' ' + 'Round 2')
    #     print(roun(first_fighter, second_fighter))
    # if fig1.health <= 0:
    #     msg = fig2.class_name + " WIN!!!"
    #     return msg
    # else:
    #     print(fighter1 + " VS " + fighter2)
    #     time.sleep(0)
    #     print(20 * "_" + "\n" +
    #           5 * ' ' + 'Round 3')
    #     print(roun(first_fighter, second_fighter))


def roun(one,two):
    one_one = GameObject.objects[one]
    two_two = GameObject.objects[two]

    def roun_f(one_one,two_two):
        x = random.randint(0, two_two.agility)
        if x in range(two_two.agility-1):
            msg ='|' + one_one.class_name + " промазал!"
            print(msg)
            time.sleep(1)
            return
        damage = one_one.stenght
        two_two.health = two_two.health - damage
        print("|" +one_one.class_name + " has now hit: " + str(damage))
        time.sleep(1)
        if int(two_two.health) <= 0:
            msg = "☠" + two_two.class_name + " is dead ☠"
            print(msg)
            time.sleep(1)
            return
        else:
            msg = "|Осталось у {}: {}".format(two_two.class_name,str(two_two.health))
        print(msg)
        time.sleep(1)

    def roun_f_next(one_one, two_two):
        roun_f(one_one, two_two)
        if two_two.health <= 0:
            return
        else:
            one_one, two_two = two_two, one_one
            roun_f_next(one_one, two_two)

    roun_f_next(one_one, two_two)
    gg = "---The end Round---"
    return gg




def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if  verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb(".."))

class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Elf(GameObject):
    def __init__(self, name):
        self.class_name = "elf"
        self.health = 4
        self.stenght = 2
        self.agility = 3
        self._desc = " The forest protecs me!"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 2:
            return self._desc
        elif self.health == 1:
            health_line = "He has left leg wound."
        elif self.health == 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 6
    self.stenght = 2
    self.agility = 0
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
     self._desc = value

class Skeleton(GameObject):
  def __init__(self, name):
    self.class_name = "skeleton"
    self.health = 5
    self.stenght = 3
    self.agility = 2
    self._desc = "The shadow of death"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=1:
      return self._desc
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
     self._desc = value

goblin = Goblin("Gobbly")
elf = Elf("Elfucho")
skeleton = Skeleton("Bon")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else:
        msg = "You hit the {}".format(thing.class_name)
        thing.desc = "pitiful wounded {}".format(thing.class_name)
    if type(thing) == Elf:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the elf!"
      else:
        msg = "You hit the {}".format(thing.class_name)
        thing.desc = "pitiful wounded {}".format(thing.class_name)
    if type(thing) == Skeleton:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the skeleton!"
      else:
        msg = "You hit the {}".format(thing.class_name)
        thing.desc = "pitiful wounded {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun)
  return msg



verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
    "name": name_per,
    "stat": stat,
    "info": info,
    "fight": fight,
}
