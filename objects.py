class member:

    def __init__(self, username, name, age, p_languages, interests, events, education):
        self.username
        self.name = name
        self.age = age
        self.p_languages = list()
        self.interests = list()
        self.events = list()
        self.education = education
        self.rs = dict{}

    # will add to list of events signed up
    def signUp(self, event):
        self.events.append(event)

    # add to a list of right swipes
    def rightSwipe(self, member):


class event:

    # constructor for events
    def __init__(self, latitude, longitude, max_capacity, group_size, duration, description, teams):
        # self.where = some way of converting latitude and logitude to a location i can put on a map
        self.max_cap = max_capacity
        self.group_size = group_size
        self.duration = duration
        self.description = description
        self.teams = teams 
