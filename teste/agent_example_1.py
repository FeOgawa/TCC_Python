

from pade.misc.utility import display_message, start_loop, call_later
from pade.acl.messages import ACLMessage, AID
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from sys import argv
import aiml

class AgenteHelloWorld(Agent):
    def __init__(self, aid):
        super(AgenteHelloWorld, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World!')

        #teste AIML
        kernel = aiml.Kernel()
        kernel.learn("Auxiliar/std-startup.xml")
        kernel.respond("LOAD AIML B")
        resposta = "WHAT ARE YOU"
        display_message(self.aid.localname, kernel.respond(resposta))

        #teste mensagem
        display_message(self.aid.localname, 'Enviando Mensagem...')
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID('timed_agent'))
        message.set_content('Ola Agente')
        self.send(message)


if __name__ == '__main__':

    agents_per_process = 1
    c = 0
    agents = list()
    for i in range(agents_per_process):
        port = int(argv[1]) + c
        agent_name = 'agent_hello_{}@localhost:{}'.format(port, port)
        agente_hello = AgenteHelloWorld(AID(name=agent_name))
        agents.append(agente_hello)
        c += 1000

    start_loop(agents)