import socket, threading
import click
from datetime import datetime

@click.command()
@click.option('--target','-T',default='127.0.0.1',help='Target IP or Domain Name.')
@click.option('--ports','-P',is_flag=True, help='Use this flag to scan specific ports.')
def scanner(target,ports):
    click.secho('\n	Scanning Ports for: ', fg='green', nl=False)
    click.secho(target, fg='blue', bold=True)
    print()
    if(ports):
        prts=str(input("\n	=> Enter ports separated by comma (Eg: 21 , 20 , 40):  "))
        prts=prts.split(" , ")
        TIME=datetime.now()
        print("\n")
        for x in prts:
            if(connection(target, int(x))==0):
                click.secho("	=> ",nl=False,fg='blue',bold=True)
                click.secho("(*) ",nl=False,bold=True,fg='red')
                click.secho("Port: %s is " % (x),nl=False)
                click.secho("CLOSED",fg="red",bold=True)       
    else:
        click.secho("\n	Scanning ",fg='red',nl=False,bold=True)
        click.secho("All ",nl=False)
        click.secho("Ports...\n",fg='green', blink=True)
        threads = []
        TIME=datetime.now()
        for i in range(10000):
            th = threading.Thread(target=connection, args=(target, i))
            threads.append(th)
            threads[i].start()
        for i in range(10000):
            threads[i].join()
	
    click.secho("\nTotal Time Taken: ", bold=True, fg='red', nl=False)
    click.secho(str(datetime.now()-TIME), bold=True, fg='blue')

def connection(IP, PORT):
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Socket.settimeout(0.5)
    try:
        Socket.connect((IP, PORT))
        click.secho("	=> ",nl=False,fg='blue',bold=True)
        click.secho("(#) ",nl=False,fg='green')
        click.secho("Port: %s is " % (PORT),nl=False)
        click.secho("OPEN",fg="green",blink=True)
        return 1
    except:
        return 0

if __name__ == "__main__":
	scanner()
