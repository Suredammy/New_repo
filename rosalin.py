def dna():
    with open(input("Enter file name: "), "r") as o:
        content = o.read()
        a = content.count("A")
        c = content.count("C")
        g = content.count("G")
        t = content.count("T")
    return f"{a} {c} {g} {t}"



from Bio.Seq import Seq
def transcribe(data = None):
    if data == None:
        with open(input("Enter file name: "), "r") as f:
            content = Seq(f.read())
    else:
        content = Seq(input)
    return content.transcribe()

print(transcribe())

