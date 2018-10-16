
class company_ubsusers(object):

    def __init__(self, name, quota, used):
        self.name = name
        self.quota = quota
        self.used = used

    def __str__(self):
        return   " name: " + self.name + " used: " + str(self.used) + " quota: " + str(self.quota)

    def __repr__(self):
        return " name: " + self.name + " used: " + str(self.used) + " quota: " + str(self.quota)
