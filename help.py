from StorageReader import ReadStorage

r = ReadStorage("data.csv")
p = r.getContent()

print(p)
