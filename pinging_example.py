import sys
import pinging 
if __name__ == "__main__":
    hostname = sys.argv[1]
    # hostname= "192.168.1.1"
    duration = int(sys.argv[2])
    # duration = 1
    ping_home= pinging.ping_monitoring(hostname,duration)
    ping_home.realtime_monitoring(Plot_realtime=True, SaveFile=True)
