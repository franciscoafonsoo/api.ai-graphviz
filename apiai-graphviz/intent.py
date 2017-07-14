"""
Class Intent:

Used to represent the relevant aspects of an API.AI Intent

Based on the json files inside the 'intent' folder from an agent export.
"""


class Intent:

    def __init__(self, fields):
        self.name = fields.get('name')
        self.events = fields.get('events')
        self.contextin = fields.get('contexts')
        self.action = fields.get('responses')[0].get('action')
        self.usersays = fields.get('userSays')

        # if alias entao alias
        # if not alias, text.
        # if neither, empty

        # for x in fields['userSays']:
        #   self.usersays.append(x['data'])

        self.contextout = list()

        for i in fields.get('responses')[0].get('affectedContexts'):
            if not i.get('lifespan') == 0:
                self.contextout.append(i.get('name'))

    def __str__(self) -> str:
        return self.name + self.contextin
