!pip install FPDF
from fpdf import FPDF
import pandas as pd
#------------Variaveis
titulo="CERTIFICADO DE PARTICIPACAO"
subtitulo="Este certificado comprova que"
texto2="concluiu co mexito o curso de XXXXXXXXXXXXXXXX ministrado por "
texto3="Prof. XXXXXX entre xx/xx/xx e xx/xx/xx"
texto4="Com carga horaria de aproximadamente xx horas"
#------------Lista
nomes = ["Jose da Silva","Alvaro Carneiro","Zeca Barbosa"]

#------------Gerador
for nome in nomes:
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial",size=12)
  pdf.cell(200,10,txt=titulo,ln=1,align="C")

  pdf.text(65,95,titulo)
  pdf.text(67,120,subtitulo)
  pdf.text(70,145,nome)
  pdf.text(20,165,texto2)
  pdf.text(50,175,texto3)
  pdf.text(50,185,texto4)

  pdf.output(f"{nome}.pdf")
