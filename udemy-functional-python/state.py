current_speaker = None

# A stateful example
def register(name):
    global current_speaker
    current_speaker = name

def speak(text):
    print('[%s] %s' % (current_speaker, text))

register('John')
speak('Hello world!')
register('Carlos')
speak('Foobar!')

# Object are also states
# Stateful implementation the object has a self._name and this property is a state that is inside the object (encapsulation)
# Objects are stateful
class Speaker():
    def __init__(self, name):
        self._name = name
    def speak(self, text):
        print('[%s] %s' % (self._name, text))

john = Speaker('John')
john.speak('Hello World')
carlos = Speaker('Carlos')
carlos.speak('Foobar!')


# Stateless implementation of the above examples
def speak(speaker, text):
    print('[%s], %s' % (speaker, text))

speak('John', 'Hello world')
speak('Carlos', 'Foobar!')
