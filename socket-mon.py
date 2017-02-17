import psutil

output = []
output = psutil.net_connections()
print output[10:]
process_map = {}

print "\"pid\",\"laddr\",\"raddr\",\"status\""

for val in output:
    if val.raddr:
        formatted_output = "\"{0}\",\"{1}@{2}\",\"{3}@{4}\",\"{5}\"".format(val.pid, val.laddr[0],val.laddr[1], val.raddr[0],val.raddr[1], val.status)
        if val.pid in process_map:
            process_map[val.pid].append(formatted_output)
        else:
            process_map[val.pid] = [formatted_output]

for key,value in sorted(process_map.iteritems(), key=lambda(k,v): len(v), reverse=True):
    for i in value:
        print i