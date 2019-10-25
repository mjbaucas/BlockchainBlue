import math
import collections

if __name__ == "__main__":
    file_A = open("message_records2A.txt", "r")
    file_B = open("message_records2B.txt", "r")
    #file_C = open("message_records3C.txt", "r")
    #file_D = open("message_records6D.txt", "r")
    #file_E = open("message_records6E.txt", "r")
    #file_F = open("message_records6E.txt", "r")

    
    record = {}
    packet_count = 0
    for file_ in [file_A, file_B]:
        for line in file_.readlines():
            section = line.split(" ")
            timestamp = section[2]
            value = int(timestamp)%1554340700
            index = math.floor(value/180)
            if index*300 in record:
                record[index*300].append(section[:-1])
            else:
                record[index*300] = [section[:-1]] 
            packet_count+=1

    data = {}
    for key, values in record.items():
        counter = 0
        for value in values:
            if value[3] == "1":
                counter+=1
        data[key] = counter/len(values)
    
    print(data)
    print(packet_count)

    file_X = open("message_records_2X.csv", "w")
    for key in sorted(data.keys()):
        file_X.write(str(key) + ", " + str(data[key]) + "\n")
    
    file_A.close()
    file_B.close()
    #file_C.close()
    #file_D.close()
    #file_E.close()
    #file_F.close()
    file_X.close()