from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


cnv = canvas.Canvas('meu_pdf.pdf')
cnv.line(0,208, 50, 208)
cnv.line(550,208, 600, 208)
cnv.line(0,416, 50, 416)
cnv.line(550,416, 600, 416)
cnv.line(0,632,50, 632)
cnv.line(550,632,600, 632)

cnv.setFont(psfontname= 'Times-Roman' ,size=9)


def first_line(ida, nome, datavenc, n_mens, valor,y):
    cont = 0
    x = 0
    while cont <=1:
        if cont ==1:
            x = 300
        cnv.drawString(152+x, 800+y, 'INFORMÁTICA' )
        cnv.drawString(150+x, 790+y, 'TURMA-CRATO' )
        cnv.drawString(20+x, 820+y, f'id: {ida}' )
        cnv.drawImage('img.jpeg',40+x, 780+y, 60, 30)  # imagem da empresa
        cnv.rect(35+x, 740+y, 240, 25) # aluno
        cnv.setFont(psfontname= 'Times-Roman' ,size=8)
        cnv.drawString(37+x, 758+y, 'Aluno ' )
        
        cnv.rect(35+x, 710+y, 240, 25) # mensalidade/ vencimento/ valor
        cnv.drawString(37+x, 728+y, 'Nº Mensalidade' )
        cnv.line(115+x,710+y, 115+x,735+y )
        cnv.drawString(117+x, 728+y, 'Vencimento' )
        cnv.line(195+x,710+y, 195+x,735+y )
        cnv.drawString(197+x, 728+y, 'Valor' )
        cnv.setFont(psfontname= 'Times-Roman' ,size=9)
        cnv.drawString(35+x, 669+y, 'Data___/___/_____' )
        cnv.drawString(170+x, 669+y, '___________________' )
        cnv.drawString(170+x, 658+y, '          Assinatura' )
        cnv.setFont(psfontname= 'Times-Roman' ,size=10)
        cnv.drawString(37+x, 746+y, nome)
        cnv.drawString(37+x, 714+y, n_mens )
        cnv.drawString(117+x, 714+y, datavenc )
        cnv.drawString(197+x, 714+y, f'{valor},00' )
        if cont == 0:
            cnv.line(300,664+y, 300,795+y ) #linha divisória
        cont+=1
           

first_line(34, 'qualquer nome ', '17/08/1992', '05', 60, 0)
first_line(34, 'qualquer nome', '24/04/1992', '05', 60, -208)
first_line(34, 'qualquer nome', '24/04/1992', '05', 60, -416)
first_line(34, 'qualquer nome', '24/04/1992', '05', 60, -632)


cnv.save()
