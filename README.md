# ping_monitoring
Graphical monitoring pinging to server 

Get Started
---
After cloning the project, use command below to install dependencies.
> pipenv install

Then use the shell subcommand to activate virtualenv.
> pipenv shell

In order to run the code use:
> python3 pinging.py --host {hostname} --duration {duration}

you can use more command line options defined in section [CommandLine](#commandline)

duration could be one of
* h (hour) -> `1h`
* m (minute) -> `10m`
* s (second) -> `30s`

## CommandLine

**--host**

define the hostname or ip you want to ping from.

**-d / --duration**

the duration of pinging the host.

**--real-time**

disabled by default. use it if you want the plotter to plot in realtime.

**--save-file**

disabled by default. save the output of file in a name you define or the script's default name "Pinging {host}.txt"

**-o / --output**

use this option if you enabled "--save-file" and you want a custom name for the output file.

TODO
---
- [x] dependency management
- define interface to work with monitoring tools
- write unit tests
- add Dockerfile
- add ci pipelines
- add flake8 pipeline
