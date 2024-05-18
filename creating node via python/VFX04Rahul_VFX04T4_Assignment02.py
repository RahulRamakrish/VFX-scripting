#sorting knobs in dictionary
selected_knobs= {"rotate":0, "scale":1,"translate":(0,0),"motionblur":0,"center":(1024,778)}
my_knobs=sorted(selected_knobs.keys())
smart_knobs={}
for key in my_knobs:
    smart_knobs[key]=selected_knobs[key]

#Creating boolean knobs
for i in smart_knobs.keys():
    my_node=nuke.thisNode()
    bol_knobs=nuke.Boolean_Knob(i+"check",i)
    bol_knobs.setFlag(nuke.STARTLINE)
    my_node.addKnob(bol_knobs)
    bol_knobs.setValue(True)

my_node=nuke.thisNode()
my_node.knob("label").setValue(" ")

#Assigning a variable to knobChanged
callback_node=my_node.knob("knobChanged")


#creating condition for knobchanged
callback_operation="""
my_node = nuke.thisNode()
my_node.knob("label").setValue(" ")

label_string=" "
for name,value in smart_knobs.items():
#checking if the default value is different
    if(my_node.knob(name).value()!=value ):

#checking if the user created boolean knob for the knob in transform is on
        if(my_node.knob(name+"check").value()):

#assigning the changed knobs to variable
            label_string=label_string+str(name)+" : "+ str(my_node.knob(name).value())+"\\n"

#setting the value of label to value inside variable label string 
my_node.knob("label").setValue(str(label_string))
"""

#passing the condition to the knobchanged
callback_node.setValue(callback_operation)

#disabling the python button
my_node.knob("Smart_Knobs").setEnabled(False)

#disabling the label
my_node.knob("label").setEnabled(False)
