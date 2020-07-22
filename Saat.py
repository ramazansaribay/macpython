f = open("raw.txt", "r")
lines = f.readlines()
gcp = (lines [9::18])  # Ground Control Point Line.
time = (lines [14::18])  # The line including the time that GCP is created.
gcp = list(gcp)
time = list(time)
print(gcp)
print(time)
