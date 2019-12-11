import datetime

class Train:
    def __init__(self, a, b, c, n, num, quan_stop, guan_railcarr, depart_time_h, depart_time_min, arrival_time_h, arrival_time_min):
        self.a = a
        self.b = b
        self.c = c
        self.n = n
        self.num = num
        self.quan_stop = quan_stop
        self.guan_railcarr = guan_railcarr
        self.depart_time_h = send_time_h
        self.depart_time_min = send_time_min
        self.arrival_time_h = arrival_time_h
        self.arrival_time_min = arrival_time_min
d = dict()
n = 1
while n != 0:
    num = int(input("\nInput num train: "))
    quan_stop = int(input("Input quan_stop t"+str(num)+": "))
    guan_railcarr = int(input("Input guan_railcarr t"+str(num)+": "))
    depart_time_h = int(input("Input send_time_h t"+str(num)+": "))
    depart_time_min = int(input("Input send_time_min t"+str(num)+": "))
    arrival_time_h = int(input("Input arrival_time_h t"+str(num)+": "))
    arrival_time_min = int(input("Input arrival_time_min t"+str(num)+": "))
    a = datetime.datetime.strptime(str(depart_time_h)+str(depart_time_min), '%H%M')
    b = datetime.datetime.strptime(str(arrival_time_h)+str(arrival_time_min), '%H%M')
    c = str(b-a)
    
    d.update({
        num: {
            "Number of tran: ": num,
            "Quantity of stops of tran: ": quan_stop,
            "Quantity of railway carriage of tran: ": guan_railcarr,
            "Departure time of tran - ": str(a.time()),
            "Arrival time of tran - ": str(b.time()),
            "Travel time - ": c
            }
            })
    n = int(input("Next? - 0 or 1 - "))

print ("\n",d)


















#print("\n","Number of tran: ", num)
#print("\n","Quantity of stops of tran: ", quan_stop)
#print("\n","Quantity of railway carriage of tran: ", guan_railcarr)
#print("\n","Departure time of tran - ", depart_time_h,":",depart_time_min)
#print("\n","Arrival time of tran - ", arrival_time_h,":",arrival_time_min)

#print("Travel time - ",b-a)
