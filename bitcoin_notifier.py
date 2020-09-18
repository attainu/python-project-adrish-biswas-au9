import requests
import sys
import time
import datetime
import locale
locale.setlocale(locale.LC_MONETARY, 'en_IN') #Setting Indian Locale

#"email_update,telegram_update" commands to be entered in --set-destination command  
class BitcoinPriceAlert:
    def __init__(self): #Default values are set here
        self.threshold_flag = True
        #values for checking are provided as comments beside the default values.
        self.threshold = 829000#810000
        self.interval = 2#60*60*24
        self.duration = 20#7*24*60*60
        self.destination = 'email_update'
        self.message_bunch = 5
        valid_arguments = ['--set-threshold','--set-interval','--set-duration','--set-destination','--set-message-bunch','--help']
        arguments = (sys.argv)[1:] #extarcting the command arguments
        
        if '--help' in arguments:#printing help message if --help is entered
            print('bitcoin_notifier.py - To receive notifications on target application regarding bitcoin prices.')
            print('usage: bitcoin_notifier.py [--set-threshold <value>] [--set-interval <value>] [--set-destination <value>] [--set-duration <value>]')
            print('Options :')
            print('--set-threshold \t\t sets the threshold value in rupees for the emergency sms updates')
            print('--set-interval \t\t\t sets the interval in secs for daily updates')
            print('--set-duration \t\t\t sets the duration value in secs for the entire script')
            print('--set-destination \t\t sets the destination app for daily updates')
            print('--set-message-bunch \t\t sets the number of messages to be bunched at an interval')
            print('--help \t\t\t\t print this help and exit')
            exit()

        for arg in arguments:#checking for valid commands and updating the default values
            if arg == valid_arguments[0]:
                self.threshold = int(arguments[arguments.index(arg)+1])
            if arg == valid_arguments[1]:
                self.interval = int(arguments[arguments.index(arg)+1])
            if arg == valid_arguments[2]:
                self.duration = int(arguments[arguments.index(arg)+1])
            if arg == valid_arguments[3]:
                self.destination = arguments[arguments.index(arg)+1]
            if arg == valid_arguments[4]:
                self.message_bunch = int(arguments[arguments.index(arg)+1])

    def getBitcoinPrice(self):#Fetching json and returning the formatted values for daily updates and sending in case of emrgency sms update
        iftt_threshold_url = 'https://maker.ifttt.com/trigger/sms_emergency/with/key/eMXOLXctktmrABB64fpeIPyycb7j8NyjffPfYgf3gIK' #url for emergency updates
        coin_api_url='https://api.coindesk.com/v1/bpi/currentprice.json'
        usd_to_inr_url='http://www.floatrates.com/daily/inr.json'
        response_inr=requests.get(usd_to_inr_url)#Fetching json
        usd_to_inr_json=response_inr.json()
        response=requests.get(coin_api_url)
        coin_api_url_json = response.json()#Fetching json
        rate_usd_to_inr=usd_to_inr_json['usd']['inverseRate']
        price = coin_api_url_json['bpi']['USD']['rate']
        price_string_usd=price.replace(',', '')
        price_float_inr=float(price_string_usd)*rate_usd_to_inr#conversion from usd to inr
        self.threshold_flag
        if self.threshold_flag and price_float_inr >= self.threshold:#checking thr threshold
            json_to_be_sent = {'value1':locale.currency(price_float_inr, grouping=True)}#formatting the numbers in Indian system
            requests.post(iftt_threshold_url,json=json_to_be_sent)#sending emergency sms
            self.threshold_flag = False

        print('loading...')
        return locale.currency(price_float_inr, grouping=True)#formatting the numbers in Indian system and returning for daily updates


    def formatAndSendPrices(self,bitcoin_history, event_name):
        iftt_daily_url=('https://maker.ifttt.com/trigger/{}/with/key/eMXOLXctktmrABB64fpeIPyycb7j8NyjffPfYgf3gIK').format(event_name)#formatting the url depending on the destination app chosen by the user.
        rows = []
        for bitcoin_price in bitcoin_history:
            date = bitcoin_price['date'].strftime("%D/%M/%Y, %H:%M:%S") #creating the current date and time
            price = bitcoin_price['price']

            row = '{}: </b>{}</b>'.format(date, price) #Putting each in separate lines by using html <br> tag
            rows.append(row)
        price_passed={'value1':'<br>'.join(rows)}
        print("Sent")
        requests.post(iftt_daily_url,json=price_passed)#sending daily update to target application

    def main(self):
        stop_time = time.time() + self.duration
        while time.time() < stop_time:#checking if the duration has been crossed or not
            price_arr = []
            for i in range(self.message_bunch):
                price_arr.append({'date': datetime.datetime.now(), 'price': self.getBitcoinPrice()})#storing the values as a single set and calling the getBitcoinPrice() function
                time.sleep(self.interval)# waiting for the interval
            self.formatAndSendPrices(price_arr,self.destination)#Function call to format the data and send the daily update

if __name__ == "__main__":#calling the main function
    obj = BitcoinPriceAlert()
    obj.main()