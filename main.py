#!usr/bin/env/python

# File:           main.py
# Author:         Alex Thompson
# Github:         palex88
# Date Created:   2018-03-19
# Date Modified:  2018-03-21
# Python Version: 3.6
#
# Purpose:        This is a program that visualizes pcap data obtained from Wireshark. It plots the count of the types
#                 of packets and plots them in a bar graph.


import pandas as pd
import matplotlib.pyplot as plt


def run():
    """
    Main function run that visualizes the data.
    
    :return:
    """
    pcap_data = pd.read_csv('packet_metadata.csv', index_col='No.')

    df = pcap_data.groupby('Protocol')['Protocol'].count()

    df.plot(kind='bar')

    plt.show()


if __name__ == '__main__':
    run()
