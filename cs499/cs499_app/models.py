from django.db import models
from collections import OrderedDict
from datetime import datetime
import json
from django.contrib.auth.models import User
from cs499.cs499_app.views.api.helpers import dejsonify


#******* Purpose ********#
# This file conatins all the models needed for creating tables in the database. 
# Parts of this code was provided to us by our Customer Chris Allen.


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



#Device can belong to multiple users but is unique
class Device(AbstractBaseModel):
    serial = models.CharField(max_length = 50, null=False,blank=False,default="0", unique=True)
    version = models.CharField(max_length = 30, null=False,blank=False,default= "0")
    screenHeight = models.IntegerField(null=False, blank= False, default=0)
    screenWidth = models.IntegerField(null=False, blank= False, default=0)
    user = models.ForeignKey(User) 

    def to_dict(self):
        de = OrderedDict()
        de['id'] = self.id;
        de['serial'] = self.serial
        de['version'] = self.version
        de['screenWidth'] = self.screenWidth
        de['screenHeight'] = self.screenHeight
        ge['user'] = self.user

        return de

    def __unicode__(self):
        return "id:{id}, serial:{serial}, version:{version}, screenWidth:{screenWidth}, screenHeight:{screenHeight}, user:{user}".format(
            id = self.id,
            serial = self.serial,
            version = self.version,
            screenWidth = self.screenWidth,
            screenHeight = self.screenHeight,
            user = self.user
        )     

#App can belong to multiple users but is unique
class App(AbstractBaseModel):
    appname = models.CharField(max_length = 100, null=False,blank=False, unique = True)
    user = models.ForeignKey(User) 

    def to_dict(self):
        an = OrderedDict()
        an['id'] = self.id;
        an['appname'] = self.appname
        an['user'] = self.user

        return an

    def __unicode__(self):
        return "id:{id} appname:{appname} user:{user}".format(
            id = self.id,
            appname = self.appname,
            user = self.user
        )           


#Session refers to a collection of motionevents        
class Session(AbstractBaseModel):
    device = models.ForeignKey(Device)
    app = models.ForeignKey(App)
    user = models.ForeignKey(User)
    submission = models.DateTimeField(auto_now_add = True)
   
    def to_dict(self):
        s = OrderedDict()
        s['id'] = self.id      
        s['user'] = self.user
        s['submission'] = self.submission        
        
        return s

    def __unicode__(self):
        return "SessionId:{id} User:{user} Submission:{submission}".format(
            id = self.id,
            user = self.user,            
            submission = self.submission
        )

# Motion event containing all the information for each touch point
class MotionEvent(AbstractBaseModel):
    action     = models.IntegerField(null=False, blank= False, default=0)
    deviceId   = models.IntegerField(null=False, blank= False, default=0)
    downTime   = models.IntegerField(null=False, blank= False, default=0)
    edgeFlags  = models.IntegerField(null=False, blank= False, default=0)
    eventTime  = models.IntegerField(null=False, blank= False, default=0)
    metaState  = models.IntegerField(null=False, blank= False, default=0)
    pressure   = models.IntegerField(null=False, blank= False, default=0)
    size       = models.IntegerField(null=False, blank= False, default=0)
    x          = models.FloatField(null = False, default = 0)
    xPrecision = models.FloatField(null = False, default = 0)
    y          = models.FloatField(null = False, default = 0)
    yPrecision = models.FloatField(null = False, default = 0)
    sessionId  = models.ForeignKey(Session)

    def to_dict(self):
        d = OrderedDict()
        d['id'] = self.id
        d['action'] = self.action
        d['deviceId'] = self.deviceId
        d['downTime'] = self.downTime
        d['edgeFlags'] = self.edgeFlags
        d['eventTime'] = self.eventTime
        d['metaState'] = self.metaState
        d['pressure'] = self.pressure
        d['size'] = self.size
        d['x'] = self.x
        d['xPrecision'] = self.xPrecision
        d['y'] = self.y
        d['yPrecision'] = self.yPrecision
        return d

    def to_heatmap(self):
        h =OrderedDict()
        h['x'] = self.x,
        h['y'] = self.y,
        return h

    def __unicode__(self):
        return "id:{id} action:{action}, deviceId={deviceId}, downTime={downTime}, edgeFlags={edgeFlags}, eventTime={eventTime}, metaStat={metaStat}, pressure={pressure}, size={size}, x:{x}, xPrecision={xPrecision}, y:{y}, yPrecision={yPrecision}".format(
            id = self.id,
            action = self.action,
            deviceId = self.deviceId,
            downTime = self.downTime,
            edgeFlags = self.edgeFlags,
            eventTime = self.eventTime,
            metaStat= self.metaState,
            pressure = self.pressure,
            size = self.size,
            x = self.x,
            xPrecision = self.xPrecision,
            y = self.y,
            yPrecision = self.yPrecision,            
        )