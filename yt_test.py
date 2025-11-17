import urllib.request
import xmltodict
import smtplib

url = f"https://www.youtube.com/feeds/videos.xml?channel_id=UCHnyfMqiRRG1u-2MsSQLbXA"
data = urllib.request.urlopen(url)
data_read = data.read().decode('utf-8')
data_parsed = xmltodict.parse(data_read)

i = 0
print(data_parsed['feed']['entry'][i])
# se foi no dia, i +=1