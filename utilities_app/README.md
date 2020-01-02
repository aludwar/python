# Utilities webapp

This is a very basic python web form, utilizing flask, to insert monthly utilities data into InfluxDB. Once ingested, Grafana is used to graph the data. I then use this to trend my household utilities usage & cost.

I realise this is pretty rudimentary and probably could be accomplished in a simpler way using another API/method, but I wanted to experiment. With more regular python practice, I expect I'll look back at this code and laugh/cringe.

Here's an example:

![alt text](https://raw.githubusercontent.com/aludwar/python/master/utilities_app/utilities.png "Example utilities graph")

