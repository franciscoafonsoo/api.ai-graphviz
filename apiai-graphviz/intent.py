"""
ficheiro.json: {    name    : string,    
                    contexts: Array (input),
                    UserSays: Array,
                    events  : Array,
                    
                    
"""


class Intent:

    def __init__(self, name, contextin, responses, events):
        self.name       = name
        self.events     = events
        self.contextin  = contextin
        self.responses  = responses
        self.action = responses[0].get('action')

        self.contextout = list()

        for i in responses[0]['affectedContexts']:
            if not i.get('lifespan') == 0:
                self.contextout.append(i.get('name'))

    def __str__(self) -> str:
        return self.name + self.contextin
