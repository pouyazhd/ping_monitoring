'''
laus deo 
pining program and monitor it realtime 
Eng: P.Zahedi
E-mail: p.zahedi@live.com
Github: pouyazhd
'''

from matplotlib import ticker
from ping3 import ping
import datetime
import time
import matplotlib.pyplot as plt
from threading import Thread

class ping_monitoring():
    def __init__(self,host_name,duration):
        self.host_name = host_name
        self.duration = duration*3600
        
        self.save_filename= 'Pinging '+self.hostname+".txt"

        self.report_time =[]
        self.result=[]

        self.ping_thread=Thread(target=self.pinging)
        self.plot_thread=Thread(target=self.plotting)
        self.save_to_file=Thread(target=self.wirte_results)

    def pinging(self):
        i=0
        while(i<self.duration):
            self.result.append(ping(self.host_name))
            current_time=datetime.datetime.now()
            self.report_time.append(str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)+"."+str(current_time.microsecond))
            
            time.sleep(1)
            i+=1
        

    def plotting(self):
        
        for i in range(0,self.duration,10):
            # self.pinging()
            plt.plot(self.report_time,self.result, c='green')
            plt.xlabel('time')
            plt.xticks(ticks=[])
            plt.ylabel('ping time')
            plt.title('ping from '+str(self.host_name))
            plt.pause(10)
        plt.show()

    def wirte_results(self):
        fid=open(self.save_filename,"w+")
        fid.write(str(self.report_time[len(self.report_time)-1])+"\t"+str(self.result[len(self.result)-1]))
        fid.close()

    def realtime_monitoring(self,Plot_realtime=False, SaveFile=True):
        '''
        real time monitoring for pinging host_name in special time
        time is based on hour
        '''
        self.ping_thread.start()

        if Plot_realtime == True:
            self.plot_thread.start()    

        if SaveFile == True:
            self.save_to_file.start()
