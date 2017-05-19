import commands

def get_cpu_temp():
  tempfile = open("/sys/class/thermal/thermal_zone0/temp") 
  cpu_temp = tempfile.read()
  tempfile.close()
  return float(cpu_temp)/1000

def get_gpu_temp():
  gpu_temp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp= ', '').replace('C', '')
  return (gpu_temp)

def main():
  print "Temperatura CPU: ", get_cpu_temp() 
  print "Temperatura GPU: ", get_gpu_temp()

if __name__ == '__main__':
  main()
