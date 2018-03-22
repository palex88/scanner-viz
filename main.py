import pandas as pd
import matplotlib.pyplot as plt


def run():
    pcap_data = pd.read_csv('packet_metadata.csv', index_col='No.')

    df = pcap_data.groupby('Protocol')['Protocol'].count()

    df.plot(kind='bar')

    plt.show()


if __name__ == '__main__':
    run()
