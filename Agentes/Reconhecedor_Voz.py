from pade.misc.utility import display_message, start_loop, call_later
from pade.behaviours.protocols import TimedBehaviour
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.acl.filters import Filter
from sys import argv




class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        display_message(self.agent.aid.localname, 'Enviando Mensagem...')
        self.agent.sending_message
    

class Reconhecedor_Voz(Agent):
    def __init__(self, aid):
        super(Reconhecedor_Voz, self).__init__(aid=aid, debug=False)
        comp_temp = ComportTemporal(self, 4.0)
        self.behaviours.append(comp_temp)
        

    def sending_message(self):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_sender(AID('Reconhecedor_Voz'))
        message.add_receiver(AID('Semantizador'))
        message.set_content('Ola')
        self.send(message)


if __name__ == '__main__':

    agents = list()
    port = int(argv[1])
    port += 1000
    Reconhecedor_Voz_agent = Reconhecedor_Voz(AID(name='Reconhecedor_Voz@localhost:{}'.format(port)))
    agents.append(Reconhecedor_Voz_agent)

    start_loop(agents)