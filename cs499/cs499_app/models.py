from django.db import models
from collections import OrderedDict
import json

from cs499.cs499_app.views.api.helpers import dejsonify


# Abstract Models #############################################################

class AbstractBaseModel(models.Model):
    class Meta:
        abstract = True

    # Returns the object represented as a dict.
    def to_dict(self, short=False, deep=False):
        """
        Returns the object represented as a dict. If short is set to true, an
        abbreviated version of the object will be returned (usually just id and
        a any other essential fields, the rest should be omitted).  If deep is
        set to true, the dict will contain child objects, and will assume this
        instance has been annotate with the children objects in a predefined
        attribute.  See the documentation for each model's to_dict() for what
        those attributes should be. Note that sometimes setting short to true
        will cause the attribute that deep enables to be skipped.
        """
        raise NotImplementedError("This model hasn't implemented to_dict().")

    # Returns the object represended as json (based on the value of to_dict())
    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=False, indent=4)

    # Returns an instance of this model populated with data from the json 
    # string passed in.
    @classmethod
    def create_from_json(cls, json_string, **kwargs):
        instance = cls()
        instance.update_from_json(json_string, **kwargs)
        return instance

    # Returns an instance of this model populated with data from the dict
    # passed in.
    @classmethod
    def create_from_dict(cls, d, **kwargs):
        instance = cls()
        instance.update_from_dict(d, **kwargs)
        return instance

    # Updates this object to match the data in the json passed in.
    def update_from_json(self, json_string, **kwargs):
        d = dejsonify(json_string)
        self.update_from_dict(d, **kwargs)

    # Updates this object to match the data in the dict passed in.
    # If full_clean is true, it'll automatically call self.full_clean() before
    # returning.  If false, validating the model before saving is up to the 
    # caller.
    def update_from_dict(self, d, **kwargs):
        raise NotImplementedError(
            "Ths model hasn't implemented update_from_dict()")

class MotionEvent(AbstractBaseModel):
     event_x = models.IntegerField(null=False, blank= False, default=0)
     event_y = models.IntegerField(null=False, blank= False, default=0)
     time = models.IntegerField(null=False,blank=False,default=0)

     def to_dict(self):
        d = OrderedDict()
        d['id'] = self.id;
        d['time'] = self.time
        d['event_x'] = self.event_x
        d['event_y'] = self.event_y

        return d

     def __unicode__(self):
        return "id:{id} time:{time} event_x:{x} event_y:{y}".format(
            id = self.id,
            time = self.time,
            x = self.event_x,
            y = self.event_y
        )

class Parser(AbstractBaseModel):
    point_x = models.IntegerField(null=False, blank= False, default=0)
    point_y = models.IntegerField(null=False, blank= False, default=0)
    pt_time = models.IntegerField(null=False, blank= False, default=0)

    def to_dict(self):
        p = OrderedDict()
        p['id'] = self.id;
        p['pt_time'] = self.pt_time
        p['point_x'] = self.point_x
        p['point_y'] = self.point_y

        return p

    def __unicode__(self):
        return "id:{id} pt_time:{pt_time} point_x:{point_x} point_y:{point_y}".format(
            id = self.id,
            pt_time = self.pt_time,
            point_x = self.point_x,
            point_y = self.point_y
        )

class LoginUsers(AbstractBaseModel):
    username = models.CharField(max_length=20,blank=False,null=False)
    password = models.CharField(max_length=20,blank=False,null=False)

    def to_dict(self):
        u = OrderedDict()        
        u['username'] = self.username
        u['password'] = self.password

        return u

    def __unicode__(self):
        return "username:{username} password:{password}".format(
            username=self.username,
            password=self.password
        )

class UserFiles(AbstractBaseModel):
    numFiles = models.IntegerField(blank=False,null=False,default=0)
    filename = models.CharField(blank=False,null=False,max_length="40")
    user_id = models.CharField(max_length=20,blank=False,null=False)

    def to_dict(self):
        f = OrderedDict()
        f['numFiles'] = self.numFiles
        f['filename'] = self.filename
        f['user_id'] = self.user_id

        return f

    def __unicode__(self):
        return "For {user_id}: number of files is {numFiles} filenames={filename}".format(
            user_id = self.user_id,
            numFiles = self.numFiles,
            filename = self.filename
        )

