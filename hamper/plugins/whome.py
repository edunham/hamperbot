import random

from hamper.interfaces import ChatPlugin
from hamper.utils import ude

from whome.txt import *

def art(noun):
        if noun[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
            return "an " + noun
        return "a " + noun

def punc():
    return random.choice(['.','...','!','?'])

class WhoMePlugin(ChatPlugin):
    """ What someone said, and how it harmed you
        Something you did, that failed to be charming """
    name = 'whome'
    priority = 2

    def setup(self, *args):
        pass

    def discusses_me(self, msg):
        for w in whome:
            if w in msg:
                return w.strip()

    def repa(self, prefix):
        out = prefix + "? "                         # vile?
        out += random.choice(mopes)                 # gosh
        out += ", I must be "                       # , I must be
        out += art(random.choice(bigs))             # a big
        out += " " + random.choice(whome)           # failure
        return out

    def repb(self, prefix):
        out =  prefix                               # barbaric
        out += "? Only " + art(random.choice(bigs)) # ? Only a massive
        out += " " + random.choide(whome) + "ing "  # failureing
        out += random.choice(whome) + " "           # terrible
        out += random.choice(whome)                 # toaster
        out += " would call some"                   # would call someone
        out += random.choice(['one ', 'thing ', 'body '])
        out += art(prefix)                          # a barbaric
        out += punc()                               # !
        return out

    def repc(self, prefix):
        return "no YOU'RE " + art(prefix) + punc()

    def repd(self, prefix):
        return "Who me, a " + art(prefix) "?"

    def whomereply(self, bot, comm, prefix):
        resp = random.choice([repa, repb, repc, repd])()
        bot.reply(comm, '{0}: {1}'.format(comm['user'], resp))

    def manners(self, bot, comm, prefix):
        if "##" in comm['channel']:
            # Offtopic? ANYTHING GOES
            if comm['directed']:
                self.whomereply(bot, comm, prefix)
                return True
            elif random.random() < .85:
                self.whomereply(bot, comm, prefix)
                return True
        elif comm['directed']:
            out = "Now now, " + random.choice(['saying ','calling me '])
            out += prefix
            out += "isn't very nice."
            bot.reply(comm, '{0}: {1}'.format(comm['user'], out))
            return True
        else:
            # Politely ignore unkind language in on-topic channels
            return False


    def command(self, bot, comm):
        msg = ude(comm['message'].strip())
        prefix = self.discusses_me(msg)
        if prefix:
            return self.manners(bot, comm, prefix)
        return False


