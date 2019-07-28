# By using OOP we can mirror the code into how we think about the world
# If we think about voting we thing about Voter and Politician

# An OOP approach
# We structured our code in a way we think about election
# Procedural & stateful implementation
class Voter:
    def __init__(self, name):
        self.name = name
        self.voted_for = None
    def vote(self, politician):
        self.voted_for = politician
        politician.votes += 1
    def __str__(self):
        return self.name

class Politician:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return self.name

macron = Politician('Macron')
jean = Voter('Jean')
jean.vote(macron)
print('%s voted for %s' % (jean, jean.voted_for))
print('%s received %d vote(s)' % (macron, macron.votes))

# A functional approach
# A functional approach doesn't mirror the world how we think about the world and makes it unintuitive
def vote(voters, politicians, voter, politician):
    # not purely functional since we are resetting the values for dicts
    voters[voter] = politician
    if politician in politicians:
        politicians[politician] += 1
    else:
        politicians[politician] = 1
    return (voters, politicians)

def voted_for(voters, voter):
    # None is the default value
    return '%s voted for %s' % (voter, voters.get(voter, None))

def votes(politicians, politician):
    # 0 is the default value
    return '%s received %d vote(s)' % (politician, politicians.get(politician, 0))

voters, politicians = vote({}, {}, 'Jean', 'Macron')
print(voted_for(voters, 'Jean'))
print(votes(politicians, 'Macron'))
