# Scanner Vizualizer

This program takes in pcap data from Wireshark, and displays a count of the different packet types that were sent in the given file.

It uses Pandas to group and count the data, and then uses Matplotlib to chart the data in a bar chart.

On macOS there is an additional required step to be able to show the cart from a terminal. With Matplotlib installed via pip, you need to create a file `matplotlibrc` in `~/.matplotlib` and add `backend: TkAgg` to the file. Read more about this [here](https://stackoverflow.com/a/21789908/6664785).

Written in Python 3.  

**Note:** Right now the program takes in a static file.

**Usage:** In terminal `python main.py`

**Required Libraries:**
* Pandas
* Matplotlib