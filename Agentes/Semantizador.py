from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.acl.filters import Filter
from sys import argv



class Semantizador(Agent):
    def __init__(self, aid):
        super(Semantizador, self).__init__(aid=aid, debug=False)

    def react(self, message):
        super(Semantizador, self).react(message)
        if format(message.sender.name) == "Reconhecedor_Voz@localhost:21000":
            display_message(self.aid.localname, message.content)


if __name__ == '__main__':

    agents = list()
    port = int(argv[1])
    Semantizador_Agent = Semantizador(AID(name='Semantizador@localhost:{}'.format(port)))
    agents.append(Semantizador_Agent)


    start_loop(agents)