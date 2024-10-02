class User():
   def __init__(self, firstName, lastName, username,id ):
      self.firstName = firstName
      self.lastName = lastName
      self.username = username,
      self.id = id
      self.choices = {'command': None,
                      'sub': None,
                      'year': None,
                      'item': None,
                      'nature': None,
                      }
      self.back = None
      self.backCleaner = []
   def __repr__(self) -> str:
      return f"User('{self.firstName}', '{self.lastName}', '{self.username}', '{self.id}', '{self.choices}')"
usersDict = {}