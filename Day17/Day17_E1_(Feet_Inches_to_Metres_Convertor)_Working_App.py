import PySimpleGUI as sg

label1 = sg.Text("Enter Feet: ")
input_box1 = sg.InputText(tooltip="Type Feet to convert", key="feet")

label2 = sg.Text("Enter Inches: ")
input_box2 = sg.InputText(tooltip="Type Inches to convert", key="inches")

convert_button = sg.Button("Convert to Meters")
message = sg.Text(key="output")

window = sg.Window("Convertor", layout=[[label1, input_box1],
                                        [label2, input_box2],
                                        [convert_button, message]])
while True:
    events, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    metres = feet * 0.305 + inches * 0.0254
    output = f"{metres} metres"
    window["output"].update(output)

window.close()

