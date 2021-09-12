# ping_monitoring
Graphical monitoring pinging to server 

use it:
---
`python3 pinging.py hostname duration`
hostname: ip or hostname you want to ping from
duration: time duration based on hour 

Example: `python3 pinging.py 192.168.1.1 1`

Get Started
---
after cloning the project, use:
> pipenv install
to install dependencies. then use the shell to run the code.
> pipenv shell

TODO
---
- [x] dependency management
- [] define interface to work with monitoring tools
- [] write unit tests
- [] add Dockerfile
- [] add ci pipelines
- [] add flake8 pipeline
