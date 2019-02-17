README

General Getting Started
1. Open a terminal and cd into web folder
2. Run 'sudo python topology-runner-server.py 8081'
3. Open new terminal window 
4. cd into externalVMHDD/floodlight
5. run java -jar target/floodlight.jar
6. Open index.html in web folder

Notes from 09/02/2019
*Run floodlight first before the python server
*Iperf bandwidth testing runs to completeion first
*It can only be run once, second trial leads to error as the file will aready exist.
*Need to find a way to delete the file at the end of a run so as to be able to run it more than once on command.
*Need to incorporate it into the GUI so that user can run it on multiple topologies

Notes from 17/02/2019

