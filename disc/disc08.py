# Write a generator function generate_subsets that returns all subsets of the positive
# integers from 1 to n. Each call to this generator’s next method will return a list of
# subsets of the set [1, 2, ..., n], where n is the number of previous calls to next.
import email
from http import client, server
from os import rmdir
from test2 import is_leaf, label, tree


def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ... print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    num = 1
    current = [[]]
    while True:
        yield current
        current += [current + [s + [num] for s in current]]
        num += 1
    #yield means for the next iteration in doctest
    # it is a itetartion that the current keep results and continuing add new lists in its list
    # and the new list is gradually/constant up the value which includes previous list value
    #Start with a base list of subsets. To get the next sequence of subsets, we need two things:
    #   all current subsets will continue to be valid subsets in the future
    #   we take all the subsets we currently have, and add the next number. These are also valid subsets
    # 

def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if is_leaf(t):
        yield label(t)
    for b in sum_paths_gen(t):
        for n in sum_paths_gen(b):
            yield label(t) +n        


class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1 #there it is no self
        print("There are now", Student.students, "students")
        ta.add_student(self)
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sendername = sender_name
        self.recipientname = recipient_name


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
def __init__(self):
    self.clients = {}
def send(self, email):
    """Take an email and put it in the inbox of the client
    it is addressed to.
    """
    # email = self.message
    # self.clients += email

    # server in Client refer to this
    # email has a possesser 
    # client need to receive, the receive to refered to the func in client
    client = self.clients[email.recipient_name]
    client.receive(email)

def register_client(self, client, client_name):
    """Takes a client object and client_name and adds them
    to the clients instance attribute.
    """
    # self.clients.update({client: client_name})
    #mutate those client name with client to get use of client
    self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
def __init__(self, server, name):
    self.inbox = []
    self.name = name
    self.server = server
    self.server.register_client(self, self.name)
def compose(self, msg, recipient_name):
    """Send an email with the given message msg to the
    given recipient client.
    """
    # self.server = msg
    # if recipient_name in Server.clients:
    #     self.receive(Client.name(recipient_name), self.server)
    email = Email(msg, self.name, recipient_name)
    #to get defined to use
    #attributes!!!
    self.server.send(email) #since they are mutal so we should use it again to make the send attribute useful
def receive(self, email):
    """Take an email and add it to the inbox of this
    client.
    """
    self.inbox.append(email)




class Dog():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + "ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + "says woof!")

class Cat():
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives
    def eat(self, thing):
         print(self.name + "ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + "says meow")

#it can be described as define another bigger global for class which can organize the class, and take them as a attribute

class pet():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.is_alive = True
    def eat(self, thing):
        print(self.name + "ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class dog(pet):
    def talk(self):
        print(self.name + ' says woof')

# However, since we want Dog to talk in a way that is unique to dogs, we did override the talk method.

class Cat(pet):
    def __init__(self, name, owner, lives=9): 
        self.has_live = lives
        pet.__init__(self, name, owner) #it should claim that what you inherit from the host
    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!") 
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        self.has_live -= 1
        if self.has_live == 0:
            self.is_alive = False
        elif self.has_live < 0:
            print("that the cat has no more lives to lose ")
        #here is a more logical way to approch this problem, and it is 
        # if self.lives > 0:
            # if ...
        # else: print("This cat has no more lives to lose :> ")

class NoisyCat(pet): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        pet.__init__(self, name, owner)
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print(self.name + " says meow!")
        print(self.name + " says meow!")

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x -1 )

class B(A):
    def f(self):
        return 4

x, y = A(), B()

#in y.g(x, 2) note that x is a obj which previous is assigned to A(),and it is another instance. In this instance it is self - y , obj - x, 2 in the formal parameter, it turns out to be the return order is 2, 4, 2, and adds them upto 8, which in first recursion, the self is bound to y, it's like g(y, y, 1)