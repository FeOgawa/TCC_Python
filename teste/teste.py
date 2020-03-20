import aiml

kernel = aiml.Kernel()
kernel.learn("Auxiliar/basic_chat.aiml")
print(kernel.respond("HELLO"))

