from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


cnv = canvas.Canvas('meu_pdf.pdf')
cnv.drawString(0,208,'a')
cnv.drawString(0,416,'a')
cnv.drawString(0,624,'a')
cnv.drawString(593,840,'.')
cnv.setFont(psfontname= 'Times-Roman' ,size=9)


def first_line(ida, nome, datavenc, n_mens, valor):
    cnv.drawString(152, 800, 'INFORMÁTICA' )
    cnv.drawString(150, 790, 'TURMA-CRATO' )
    cnv.drawString(20, 820, f'id: {ida}' )
    cnv.drawImage('img.jpeg',40, 780, 60, 30)  # imagem da empresa
    cnv.rect(35, 740, 240, 25) # aluno
    cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    cnv.drawString(37, 758, 'Aluno ' )
    
    cnv.rect(35, 710, 240, 25) # mensalidade/ vencimento/ valor
    cnv.drawString(37, 728, 'Nº Mensalidade' )
    cnv.line(115,710, 115,735 )
    cnv.drawString(117, 728, 'Vencimento' )
    cnv.line(195,710, 195,735 )
    cnv.drawString(197, 728, 'Valor' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(35, 669, 'Data___/___/_____' )
    cnv.drawString(170, 669, '___________________' )
    cnv.drawString(170, 658, '          Assinatura' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=10)
    cnv.drawString(37, 746, nome)
    cnv.drawString(37, 714, n_mens )
    cnv.drawString(117, 714, datavenc )
    cnv.drawString(197, 714, f'{valor},00' )
    
    cnv.line(300,664, 300,795 ) #linha divisória
    
    cnv.drawString(452, 800, 'INFORMÁTICA' )
    cnv.drawString(450, 790, 'TURMA-CRATO' )
    cnv.drawString(320, 820, f'id: {ida}' )
    cnv.drawImage('img.jpeg',340, 780, 60, 30)  # imagem da empresa
    cnv.rect(335, 740, 240, 25) # aluno
    cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    cnv.drawString(337, 758, 'Aluno ' )
    
    cnv.rect(335, 710, 240, 25) # mensalidade/ vencimento/ valor
    cnv.drawString(337, 728, 'Nº Mensalidade' )
    cnv.line(415,710, 415,735 )
    cnv.drawString(417, 728, 'Vencimento' )
    cnv.line(495,710, 495,735 )
    cnv.drawString(497, 728, 'Valor' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(335, 669, 'Data___/___/_____' )
    cnv.drawString(470, 669, '___________________' )
    cnv.drawString(470, 658, '          Assinatura' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=10)
    cnv.drawString(337, 746, nome)
    cnv.drawString(337, 714, n_mens )
    cnv.drawString(417, 714, datavenc )
    cnv.drawString(497, 714, f'{valor},00' )
    
    
    

def second_line(ida, nome, datavenc, n_mens, valor):
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(152, 584, 'INFORMÁTICA')
    cnv.drawString(150, 574, 'TURMA-CRATO' )
    cnv.drawString(20, 604, f'id: {ida}' )
    cnv.drawImage('img.jpeg',40, 564, 60, 30)  # imagem da empresa
    cnv.rect(35, 524, 240, 25) # aluno
    cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    cnv.drawString(37, 542, 'Aluno ' )
    
    cnv.rect(35, 494, 240, 25) # mensalidade/ vencimento/ valor
    cnv.drawString(37, 512, 'Nº Mensalidade' )
    cnv.line(115,494, 115,519 )
    cnv.drawString(117, 512, 'Vencimento' )
    cnv.line(195,494, 195,519 )
    cnv.drawString(197, 512, 'Valor' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(35, 453, 'Data___/___/_____' )
    cnv.drawString(170, 453, '___________________' )
    cnv.drawString(170, 442, '          Assinatura' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=10)
    cnv.drawString(37, 530, nome)
    cnv.drawString(37, 498, n_mens )
    cnv.drawString(117, 498, datavenc )
    cnv.drawString(197, 498, f'{valor},00' )
    
    cnv.line(300,448, 300,579 ) #linha divisória
    
    # cnv.drawString(452, 800, 'INFORMÁTICA' )
    # cnv.drawString(450, 790, 'TURMA-CRATO' )
    # cnv.drawString(320, 820, f'id: {ida}' )
    # cnv.drawImage('img.jpeg',340, 780, 60, 30)  # imagem da empresa
    # cnv.rect(335, 740, 240, 25) # aluno
    # cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    # cnv.drawString(337, 758, 'Aluno ' )
    
    # cnv.rect(335, 710, 240, 25) # mensalidade/ vencimento/ valor
    # cnv.drawString(337, 728, 'Nº Mensalidade' )
    # cnv.line(415,710, 415,735 )
    # cnv.drawString(417, 728, 'Vencimento' )
    # cnv.line(495,710, 495,735 )
    # cnv.drawString(497, 728, 'Valor' )
    # cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    # cnv.drawString(335, 644, 'Data___/___/_____' )
    # cnv.drawString(470, 644, '___________________' )
    # cnv.drawString(470, 633, '          Assinatura' )
    # cnv.setFont(psfontname= 'Times-Roman' ,size=10)
    # cnv.drawString(337, 746, nome)
    # cnv.drawString(337, 714, n_mens )
    # cnv.drawString(417, 714, datavenc )
    # cnv.drawString(497, 714, f'{valor},00' )    

def third_line(id, nome, datavenc):
    cnv.drawString(172, 800, 'INFORMÁTICA' )
    cnv.drawString(170, 790, 'TURMA-CRATO' )
    cnv.drawString(40, 820, 'id:' )
    cnv.drawImage('img.jpeg',60, 780, 60, 30)  # imagem da empresa
    cnv.rect(55, 740, 240, 25) # aluno
    cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    cnv.drawString(57, 758, 'Aluno' )
    cnv.rect(55, 710, 240, 25) # mensalidade/ vencimento/ valor
    cnv.drawString(57, 728, 'Nº Mensalidade' )
    cnv.line(135,710, 135,735 )
    cnv.drawString(137, 728, 'Vencimento' )
    cnv.line(215,710, 215,735 )
    cnv.drawString(217, 728, 'Valor' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(55, 644, 'Data___/___/_____' )
    cnv.drawString(190, 644, '___________________' )
    cnv.drawString(190, 633, '          Assinatura' )

def fourth_line(id, nome, datavenc):
    cnv.drawString(172, 800, 'INFORMÁTICA' )
    cnv.drawString(170, 790, 'TURMA-CRATO' )
    cnv.drawString(40, 820, 'id:' )
    cnv.drawImage('img.jpeg',60, 780, 60, 30)  # imagem da empresa
    cnv.rect(55, 740, 240, 25) # aluno
    cnv.setFont(psfontname= 'Times-Roman' ,size=8)
    cnv.drawString(57, 758, 'Aluno' )
    cnv.rect(55, 710, 240, 25) # mensalidade/ vencimento/ valor
    cnv.drawString(57, 728, 'Nº Mensalidade' )
    cnv.line(135,710, 135,735 )
    cnv.drawString(137, 728, 'Vencimento' )
    cnv.line(215,710, 215,735 )
    cnv.drawString(217, 728, 'Valor' )
    cnv.setFont(psfontname= 'Times-Roman' ,size=9)
    cnv.drawString(55, 644, 'Data___/___/_____' )
    cnv.drawString(190, 644, '___________________' )
    cnv.drawString(190, 633, '          Assinatura' )            

first_line(34, 'ruben sa brito', '24/04/1995', '05', 60)
second_line(34, 'ruben sa brito', '24/04/1995', '05', 60)
cnv.showPage()
cnv.drawString(0,200, 'a')


cnv.save()
