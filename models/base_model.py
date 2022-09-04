#!/usr/bin/python3
 class BaseModel:
    """ Our Code insert Here"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __str__(self):
        """
        method for named
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))
    def save(self):
        """
        method for save stuff
        """
    def to_dict(self):
        """
        method for create a dict
        """