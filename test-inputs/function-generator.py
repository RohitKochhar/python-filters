# Output file (ex: "linear.txt")
s_OutputFile = "linear.txt"
# Signal length (ex: 100)
i_SignalLength = 100 
# Function
def fn(x):
    return f"{x}\n"

f = open("linear.txt", "w")
for i in range(0, i_SignalLength):
    f.write(fn(i))
f.close()