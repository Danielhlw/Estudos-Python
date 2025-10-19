aluno = {
    "professor": "Daniel",
    "idade": 30,
    "curso": "Python",

}

print(aluno["professor"])
print (aluno.get("idade"))
aluno["idade"] = 31
print(len(aluno))
del aluno["idade"]

for i in aluno:
    print(i, aluno[i])