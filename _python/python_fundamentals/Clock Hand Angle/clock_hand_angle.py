#define the function convert the clock to the angles by degrees?
def clockHandAngles(time):
    y=time.split(":")
    hours=int(y[0])*30
    minutes=int(y[1])*6
    seconds=int(y[2])*6
    print=("Hours: {} degrees".format(hours))
    print=("Minutes: {} degrees".format(minutes))
    print=("Seconds: {} degrees".format(seconds))
clockHandAngles("06:30:10")