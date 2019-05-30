
from __future__ import print_function
import torch
import multiprocessing as mp
import psutil

x = torch.rand(5, 3)
print(x)


print("Number of processors: ", mp.cpu_count())

avg_cpu_use_percent = psutil.cpu_percent(percpu=False)
print("Percent CPU usage: ",avg_cpu_use_percent)

# pull percent RAM used
ram_usage = psutil.virtual_memory().percent
print("Percent RAM usage: ", ram_usage)
x=input("What is your name? ")
print("Hello", x)