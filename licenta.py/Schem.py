import schemdraw
import schemdraw.elements as elm

''''''''''
d = schemdraw.Drawing()
d.add(elm.Resistor(label='100K$\Omega$'))
d.add(elm.Capacitor(d='down', botlabel='0.1$\mu$F'))
d.add(elm.Line(d='left'))
d.add(elm.Ground)
d.add(elm.SourceV(d='up', label='100V'))
d.draw()
d.save('schematic.svg')
'''

d=schemdraw.Drawing()
d.add(elm.Resistor(label="R1"))
d.add(elm.Resistor(label="R2"))
d.draw()
d.save('static/Img/Img_Teoria/rezistor_serial.png')
#paralel resistor
#paralel=schemdraw.Drawing()
#paralel.add(elm.Resistor(label='R1'))
#paralel.add(elm.Line(d='up'))
#paralel.add(elm.Resistor(label='R2',d="left"))
#paralel.add(elm.Line(d='down'))



#paralel.add(elm.Line(d='right'),)

#paralel.draw()
#paralel.save('static/Img/Img_Teoria/rezistor_paralel.png')


#condesator = schemdraw.Drawing()
#condesator.add(elm.Label(label='Serial',d='up'))
#condesator.add(elm.Capacitor(label='C1'))
#condesator.add(elm.Line(d='left'))
#condesator.add(elm.Capacitor(label='C2'))
#condesator.draw()
#condesator.save('static/Img/Img_Teoria/capacitor_serial_schema.png')

#paralel condesator
paralelcondesator=schemdraw.Drawing()
paralelcondesator.add(elm.Capacitor(label='C1'))
paralelcondesator.add(elm.Line(d='up',label='paralel'))
paralelcondesator.add(elm.Capacitor(label='C2',d="left"))
paralelcondesator.add(elm.Line(d='down'))
paralelcondesator.draw()
paralelcondesator.save('static/Img/Img_Teoria/capacitor_paralel_schema.png')


#porti.add(elm.logic.And)
#porti.add(elm.logic.Nand(inputs=3))
#porti.draw()

#bobina=schemdraw.Drawing()
#bobina.add(elm.Inductor(label='L1'))
#bobina.add(elm.Line(d='right'))
#bobina.add(elm.Inductor(label='L2'))
#bobina.draw()

#bobina=schemdraw.Drawing()
#bobina.add(elm.Inductor(label='L1'))
##bobina.add(elm.Line(d='right'))
#bobina.add(elm.Line(d="down"))
#bobina.add(elm.Line())
#bobina.add(elm.Inductor(label='L2',d='left'))
#bobina.add(elm.Line(d="up"))
#bobina.add(elm.Line(d="up"))
#bobina.draw()
#bobina.save('static/Img/Img_Teoria/bobina_schema.png')



