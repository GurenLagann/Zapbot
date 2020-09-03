from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver
import time

class WhatsappBot:
  def __init__(self):
    self.bot = ChatBot('TW Bot')

    conv = [
      'Oi', 
      'Olá', 
      'Tudo bem?', 
      'Tudo ótimo', 
      'Você gosta de programar?', 
      'Sim, eu programo em Python'
    ] 

    self.bot.set_trainer(ListTrainer)
    self.bot.train(conv)

    self.messagem = "Pois não, pode falar"
    self.person = ["Leandro", "Roberta (King Arthur)"]
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    self.driver =  webdriver.Chrome(executable_path=r'./chromedriver')
  
  def EnviarMensagens(self):
    self.driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    per =  self.driver.find_element_by_xpath(f"//span[@title='Leandro']")
    time.sleep(5)
    per.click()
    chat_bot =  self.driver.find_element_by_class_name('_3uMse')
    time.sleep(5)
    chat_bot.click()
    chat_bot.send_keys(self.messagem)
    send = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    time.sleep(5)
    send.click()
    time.sleep(5)        
    while True:
      teste =  self.driver.find_element_by_class_name('_274yw').text
      time.sleep(5)
      pergunta = str(teste)
      print(pergunta)
      resposta = self.bot.get_response(pergunta)
      if float(resposta.confidence) > 0.5:
          chat_bot.click()
          chat_bot.send_keys(resposta)
          send.click()
          time.sleep(5)
      else:
          chat_bot.click()
          chat_bot.send_keys('desculpe, estou aprendendo ainda')
          time.sleep(5)
          send.click()
          time.sleep(5)

teste = WhatsappBot()
teste.EnviarMensagens()

        

