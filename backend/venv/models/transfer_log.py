from venv.resourses.res import transfer_data_volume

class transfer_log(object):

    def __init__(self, date, name, resourses, company_id):
        self.date = date
        self.name = name
        self.resourses = resourses
        self.transferred = transfer_data_volume()
        self.company_id = company_id

    def __str__(self):
        return  "date: " + self.date + " name: " + self.name + " transferred: " + str(self.transferred)

    def __repr__(self):
        return  "date: " + self.date + " name: " + self.name + " transferred: " + str(self.transferred)