"""
    laus deo
    pining program and monitor it realtime
    Eng: P.Zahedi
    E-mail: p.zahedi@live.com
    Github: pouyazhd
"""
import argparse
import time
import datetime

from ping3 import ping
from threading import Thread
from matplotlib import pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(__name__)
    parser.add_argument("--host", default="1.1.1.1", type=str, dest="host", help="hostname to ping")
    parser.add_argument("-d", "--duration", default="1h", type=str, dest="duration", help="duration of ping in hours")
    parser.add_argument("--real-time", action="store_true", dest="real_time", help="realtime update of plot")
    parser.add_argument("--save-file", action="store_true", dest="save_file", help="save file to output")
    parser.add_argument("-o", "--output", required=False, dest="output_file", help="the output file if saving to file is enabled.")
    return parser.parse_args()


def parse_duration(duration):
    if len(duration) == 0:
        return None, "duration is empty"
    times = {
        "h": 60 * 60,
        "m": 60,
        "s": 1
    }
    if duration[-1] not in times.keys():
        return None, "unknown time acronym. use one of \"{}\"".format(", ".join(times.keys()))
    return int(duration[:-1]) * times[duration[-1]], None


class PingMonitoring:
    """
    duration:
        could be one of:
        1) hour
            - 10h
        2) minute
            - 10m
        3) second
            - 10s
    """
    def __init__(self, host_name, duration, custom_output=""):
        self.host_name = host_name
        self.duration_seconds, error = parse_duration(duration)
        if error:
            raise Exception(error)
        self.output_file = custom_output if custom_output else f"Pinging {self.host_name}.txt"
        self.report_time, self.result = list(), list()
        self.ping_thread = Thread(target=self.pinging)
        self.plot_thread = Thread(target=self.plotting)
        self.save_to_file = Thread(target=self.write_results)

    def pinging(self):
        counter = 0
        while counter < self.duration_seconds:
            self.result.append(ping(self.host_name))
            current_time = datetime.datetime.now()
            self.report_time.append(
                f"{current_time.hour}:{current_time.minute}:{current_time.second}.{current_time.microsecond}"
            )

            time.sleep(1)
            counter += 1

    def plotting(self):
        for i in range(0, self.duration_seconds, 10):
            plt.plot(self.report_time, self.result, c='green')
            plt.xlabel('time')
            plt.xticks(ticks=[])
            plt.ylabel('ping time')
            plt.title(f"ping from {self.host_name}")
            plt.pause(10)
        plt.show()

    def write_results(self):
        with open(self.output_file, "w+") as fd:
            fd.write(str(self.report_time[len(self.report_time) - 1]) + "\t" + str(self.result[len(self.result) - 1]))

    def realtime_monitoring(self, plot_realtime=False, save_file=True):
        """
        TODO: add multihost monitoring
        real time monitoring for pinging host_name in special time
        time is based on hour
        """
        self.ping_thread.start()

        if plot_realtime:
            self.plot_thread.start()

        if save_file:
            self.save_to_file.start()
