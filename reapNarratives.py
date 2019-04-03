#!/usr/bin/python

import requests
import sys
import json
#import psutil
import pprint
import docker
import subprocess
import pickle
import time

import urllib3
# there is a way to only disable InsecurePlatformWarning but I can't find it now
urllib3.disable_warnings()

pp = pprint.PrettyPrinter(indent=4)

def read_pickle_data(filename):
    fh = open (filename)
    data = pickle.load(fh)
    fh.close()
    return data

def save_pickle_data(filename):
    fh = open (filename, 'w')
    data = pickle.dump(fh)
    fh.close()
    
def est_connections():

    filename='proxymap.pickle'
    connectionMap = read_pickle_data(filename)
    timestamp = time.time()

    containerName='r-next-core-nginx-1-edfd1207'
    netstatOut = subprocess.check_output(['docker','exec',containerName,'netstat','-nt'])
    for line in netstatOut.split('\n'):
        if 'ESTABLISHED' not in line:
            continue
        splitLine = line.split()
        connectionMap[splitLine[4]] = timestamp

#    dockerClient = docker.from_env()
#    print dockerClient
#    nginxContainer = dockerClient.containers.get(containerName)
#    allConnections = nginxContainer.exec_run('netstat -nt')
#    allConnections = psutil.net_connections()
#    for conn in allConnections:
#        pp.pprint(conn)

    return connectionMap

def get_proxy_map(proxyMapUrl):
    proxy_map = requests.get(proxyMapUrl)
    return proxy_map.json()

def marker(proxyMap):
    estConnections = est_connections()
    for session in proxyMap:
        print session['last_ip']

def main():
    proxyMapUrl='https://next.kbase.us/proxy_map'
    marker(get_proxy_map(proxyMapUrl))
#    pp.pprint(get_proxy_map(proxyMapUrl))
    pp.pprint(est_connections())

if __name__ == "__main__":
    main()
