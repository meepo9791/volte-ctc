from scapy.all import *
from scipy.stats import kstest
from scipy.stats import ks_2samp
import scipy.stats
import numpy as np
from scipy.stats import entropy

def rdipd(pcapname):
    packets = rdpcap(pcapname)
    time_intervals = []

    previous_timestamp = None
    for packet in packets:
        if packet.haslayer(Raw):
            timestamp = packet.time
            if previous_timestamp is not None:
                time_interval = timestamp - previous_timestamp
                #time_intervals.append(float(time_interval))
                time_intervals.append(time_interval)
            previous_timestamp = timestamp
    #print(time_intervals)
    return time_intervals

p = rdipd('test.pcap')
print(p)
q = rdipd('modified_test.pcap.')
print(q)
print(ks_2samp(p,q))

p = np.asarray(p, dtype=np.float64)
q = np.asarray(q, dtype=np.float64)
print(entropy(p, q))