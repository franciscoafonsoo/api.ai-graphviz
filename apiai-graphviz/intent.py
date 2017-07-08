class Intent:
    """
    TODO: verificar que o 'affectedContext' (aqui definido como contextOut),
    é uma lista de json's
    """

    def __init__(self, name, contextin, contextout, events, action):
        if isinstance(name, str): self.name = name
        if isinstance(contextin, list): self.contextin = contextin
        if isinstance(contextout, list): self.contextout = contextout
        if isinstance(events, list): self.events = events
        if isinstance(action, str): self.action = action
