"""
Class Intent:

Used to represent the relevant aspects of an API.AI Intent

based on:

file.json: {    name    : string,
                    contexts: Array (input),
                    UserSays: Array,
                    events  : Array,
                    }



            if 'alias' in x:
                self.usersays.append(x['alias'])
            elif 'text' in x:
                self.usersays.append(x['text'])
"""


class Intent:

    def __init__(self, fields):
        self.name = fields['name']
        self.events = fields['events']
        self.contextin = fields['contexts']
        self.action = fields['responses'][0].get('action')
        self.usersays = list()

        # if alias entao alias
        # if not alias, text.
        # if neither, empty

        # for x in fields['userSays']:
        #   self.usersays.append(x['data'])

        self.contextout = list()

        for i in fields['responses'][0]['affectedContexts']:
            if not i.get('lifespan') == 0:
                self.contextout.append(i.get('name'))

    def __str__(self) -> str:
        return self.name + self.contextin
