import time
import pinging


if __name__ == "__main__":
    args = pinging.parse_args()
    ping_home = pinging.PingMonitoring(args.host, args.duration, custom_output=args.output_file)
    ping_home.realtime_monitoring(plot_realtime=args.real_time, save_file=args.save_file)
