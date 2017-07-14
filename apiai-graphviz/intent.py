class Intent:
    def __init__(self, a: dict):
        """ Atributs for the Intent Object. Note: only using relevant atributes to build the graph

        :param a: dictionary created from a API.AI Intent JSON
        """

        self.name = a.get('name')

        self.events = [x.get('name') for x in a.get('events')]

        # check for first node
        sub = '_WELCOME'
        self.first = True if [s for s in self.events if sub in s] else False

        self.contextin = sorted(a.get('contexts'))

        self.action = a.get('responses')[0].get('action')

        self.usersays = [x.get('data')[0] for x in a.get('userSays')]

        self.usersays = [x.get('text') if len(x) == 1 else x.get('alias') for x in self.usersays]

        self.contextout = sorted([i.get('name') for i in a.get('responses')[0].get('affectedContexts')
                                  if not i.get('lifespan') == 0])

    @staticmethod
    def find_first(l: list) -> object:
        return [x for x in l if not x.contextin]

    def __str__(self) -> str:
        return self.name

    def __eq__(self, o: object) -> bool:
        """
        I'm thinking comparing output context with input context here

        :param o: Intent Object
        :return: True if contextin == contextout
        """

        return self.contextin[:len(o.contextout)] == o.contextout

        # return super().__eq__(o)
