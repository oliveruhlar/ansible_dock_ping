from subprocess import PIPE, Popen, run

def create_u_con():
    process = Popen(['sudo','docker', 'run', '-dt', '--rm', '--detach', 'ubuntu_con'], 
                           stdout=PIPE,
                           universal_newlines=True,
                           shell=True)
    return(process.stdout.readline()[0:12:1])

def get_con_ip(con_id):
    process = Popen(['sudo','docker', 'inspect', '-f', '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}',con_id], 
                           stdout=PIPE,
                           universal_newlines=True,
                           shell=True)
    return(process.stdout.readline()[:-1])


def print_ping(con1,con2_ip):
    p = Popen(['sudo','docker', 'exec', con1, 'ping','-c', '3', con2_ip], 
                        stdout=PIPE,
                        universal_newlines=True,
                        shell=True)
    return p.communicate()[0]

#build image
run("sudo docker build -t ubuntu_con .",shell=True)

#create containers
con1 = create_u_con()
con2 = create_u_con()
run("sudo docker ps",shell=True)

#ip address of containers in bridged network
con1_ip = get_con_ip(con1)
con2_ip = get_con_ip(con2)

#pinging
print('\n')
print("con1: ping -c 100 con2",'\n')
print(print_ping(con1,con2_ip))
print('\n')
print("con1: ping -c 100 con2",'\n')
print(print_ping(con2,con1_ip))

#stop containers (auto remove)
run("sudo docker stop "+con1,shell=True)
run("sudo docker stop "+con2,shell=True)