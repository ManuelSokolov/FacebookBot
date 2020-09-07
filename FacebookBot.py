import sys
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class Bot:

    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(options=option)


    def loginFacebook(self,email,password):
       email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
       email_in.send_keys(email)

       pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
       pw_in.send_keys(password) #poe aqui a password

       login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_d"]')
       login_btn.click()

    def sendMessageFacebook(self, persons, message):
        # time to close notifications because i dont know how to close them
        time.sleep(10)
        for person in persons:
            sendMessageBtn = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/span/div/div[1]')
            sendMessageBtn.click()
            time.sleep(3)
            message_to = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input')
            message_to.send_keys(person)
            time.sleep(10)
            person_click = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/div[1]/li/div/div[1]/div')
            person_click.click()
            time.sleep(5)
            person_send = self.driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.poy2od1o.i09qtzwb.n7fi1qx3 > div.l9j0dhe7.fh5enmmv > div.l9j0dhe7.tkr6xdv7 > div.j83agx80.l9j0dhe7.du4w35lb.aovydwv3.do00u71z > div > div > div > div > div > div > div.rj1gh0hx.buofh1pr.j83agx80.cbu4d94t.l9j0dhe7.du4w35lb > div > div.pfnyh3mw > form > div > div.j83agx80.l9j0dhe7.aovydwv3.ni8dbmo4.stjgntxs.nred35xi.n8tt0mok.hyh9befq > div.aovydwv3.j83agx80.buofh1pr.ni8dbmo4.cxgpxx05.sj5x9vvc.qio8uep8.l9j0dhe7 > div.orhb3f3m.h905i5nu.jinzq4gt.emzo65vh.j83agx80.e5nlhep0.ecm0bbzt.h4z51re5.gvyehdmr.mu0vl6fp.msuhji6j.iqy7zqfr.rj1gh0hx.cbu4d94t.buofh1pr.ni8dbmo4.ll8tlv6m.b3i9ofy5.oo9gr5id.flx89l3n.dpja2al7.hedjyaoh > div > div > div > div > div._5rpb > div > div > div > div')
            person_send.send_keys(message)
            send_message = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div')
            send_message.click() #to send message
            time.sleep(3)
            #close = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div/svg')
            close = self.driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.poy2od1o.i09qtzwb.n7fi1qx3 > div.l9j0dhe7.fh5enmmv > div.l9j0dhe7.tkr6xdv7 > div.j83agx80.l9j0dhe7.du4w35lb.aovydwv3.do00u71z > div > div > div > div > div > div > div.pfnyh3mw.l9j0dhe7.tkr6xdv7 > div > div > div.j83agx80.bp9cbjyn.pfnyh3mw.cgat1ltu > span:nth-child(4) > div > svg')
            close.click()

    #readMessage to finish
    def readMessage(self):
        message_received = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div[3]div[1]/div/div[3]/div/div[12]/div[4]/div[1]/div/div/div/div[1]/div/div')  # xpath of element
        text_obtained = message_received.text  # dont know what to put here
        print(str(text_obtained))


bot = Bot()
bot.driver.get("https://www.facebook.com/")

#complete with your email and password
bot.loginFacebook("email@email.com", "password")

#insert the names of the friends you want to send message
persons = ["friend name 1" ,"friend name 2"]

#insert the message you want to send
message = "hello world"
bot.sendMessageFacebook(persons, message)


