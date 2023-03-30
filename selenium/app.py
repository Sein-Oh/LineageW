import json
import PySimpleGUI as sg

def load_data(file_name: str) -> dict:
    with open(file_name, "r", encoding="UTF-8") as f:
        data = json.load(f)
        return data

def update_data(window: sg.Window, data: dict) -> None:
    for i in range(1, 6):
        window[f"slot_{i}_label"].update(data["PLAYER-1"][f"SLOT-{i}"]["LABEL"])

toggle_off = b"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"
toggle_on = b"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"

sg.theme("Default1")

viewer = [
    [sg.Text("HP:미확인", key="lbl_hp", size=(10, None)), sg.Image(size=(200, 6), key="img_hp")],
    [sg.Text("MP:미확인", key="lbl_mp", size=(10, None)), sg.Image(size=(200, 6), key="img_mp")],
]

control = [
    [sg.Text("슬롯1", key="slot_1_label", size=(8, 1)), sg.Im(toggle_off, key='slot_1_toggle', enable_events=True , metadata=False)],
    [sg.Text("슬롯2", key="slot_2_label", size=(8, 1)), sg.Im(toggle_off, key='slot_2_toggle', enable_events=True , metadata=False)],
    [sg.Text("슬롯3", key="slot_3_label", size=(8, 1)), sg.Im(toggle_off, key='slot_3_toggle', enable_events=True , metadata=False)],
    [sg.Text("슬롯4", key="slot_4_label", size=(8, 1)), sg.Im(toggle_off, key='slot_4_toggle', enable_events=True , metadata=False)],
    [sg.Text("슬롯5", key="slot_5_label", size=(8, 1)), sg.Im(toggle_off, key='slot_5_toggle', enable_events=True , metadata=False)]
]


layout = [
    [sg.Frame("모니터링", viewer, expand_x=True)],
    [sg.Frame("기능선택", control, expand_x=True)]
]

window = sg.Window(
    "Lineage W",
    layout,
    finalize=True
)

update_data(window, load_data("userdata.json"))

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break

    elif "toggle" in event:
        #run 버튼의 메타데이터를 바꾸고 이를 이용해 이미지를 토글한다.
        window[event].metadata = not window[event].metadata
        if window[event].metadata:
            print("앱을 실행합니다.")
            window[event].update(toggle_on)
        else:
            print("앱 실행을 중지합니다.")
            window[event].update(toggle_off)

        

window.close()
