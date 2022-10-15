from flask import Flask
import sqlite3
import json

conUniversityData = sqlite3.connect("../dataBase/university_data.db", check_same_thread=False)
curUniversityData = conUniversityData.cursor()
app = Flask(__name__)
@app.route("/api/professor_id/<profid>")
def buscaProfessor(profid):
    curUniversityData.execute(f"SELECT * FROM prof WHERE prof_id='{profid}'")
    fetchBusca = curUniversityData.fetchall()
    teachingability = fetchBusca[0][2]
    populariy = fetchBusca[0][1]
    curUniversityData.execute(f"SELECT * FROM RA WHERE prof_id='{profid}'")
    fetchBuscaAlunos = curUniversityData.fetchall()
    quantidadeAlunos = len(fetchBuscaAlunos)
    for aluno in fetchBuscaAlunos:
        curUniversityData.execute(f"SELECT * FROM registration WHERE student_id='{aluno[2]}'")
        fetchBuscaCursos = curUniversityData.fetchall()  
        arrayCursos = [] 
        for curso in fetchBuscaCursos:
            arrayCursos.append(f"{curso[0]}")
    totalCursos = len(arrayCursos)
    dadosProf = {
      "prof_id": profid,
      "teachingability": teachingability,
      "populariy": populariy,
      "quantidadeAlunos": quantidadeAlunos,
      "quantidadeCursos": totalCursos,
      "cursos": arrayCursos
    }
    return json.dumps(dadosProf)
app.run(port=8080)
