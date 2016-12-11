## Collection of python scripts

** add_speed_data ** 

- This script takes a log file output that I've created and grokked with speedtest-cli, and adds the data into InfluxDB for later display with Grafana.

** speedtest-to-influxdb

- This script calls the speedtest-cli (now just called speedtest) used against speedtest.net and spits the ping latency, and download/upload metrics into InfluxDB. This script is ready to be modified for anyone's usage, just modify the initial variables in the script for your InfluxDB host.

