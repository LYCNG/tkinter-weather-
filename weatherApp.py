import tkinter as  tk
from tkinter import font
from tkinter import ttk
import requests
import time
from PIL import ImageTk

from configparser import ConfigParser
config = ConfigParser()
config.read('config.cfg')
token = config.get('token', 'token')

Hight = 700
Width = 800

def test_get_weather(entry):    
    label['text']=entry

def get_weather(city):
    url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={token}&format=JSON"
    res = requests.get(url)
    city_list = res.json()['records']['location']

    def findict(list,cityname):
        for city_dict in list:
            if city_dict.get('locationName') == cityname:
                return city_dict

    def format_range(city_element):
        now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        name=city_element['locationName']
        cityelement = city_element['weatherElement']
        Maxtemp=cityelement[4]['time'][0]['parameter']['parameterName']
        Mintemp=cityelement[2]['time'][0]['parameter']['parameterName']
        describ=cityelement[0]['time'][0]['parameter']['parameterName']
        ans = 'Today_time: %s \nCity_Name: %s \nMax Temp: %sC \nMin Temp: %sC \nDescription: %s' % (now, name, Maxtemp, Mintemp, describ)
        return ans

    city_element=findict(city_list,city)
    label['text'] = format_range(city_element)

root= tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root,heigh=Hight,width=Width)
canvas.pack()

#PythonWork\\GUI_Application\\image\\sky.png
img=ImageTk.PhotoImage(file='.\\sky.png')
background_label=tk.Label(root,image=img)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight = 0.1,anchor='n')

#entry= tk.Entry(frame,font=('Courier',14))
#entry.place(relwidth=0.5,relheight = 1)

source=[
        '嘉義縣', '新北市', '嘉義市', '新竹縣', '新竹市', '臺北市', '臺南市',
        '宜蘭縣', '苗栗縣', '雲林縣', '花蓮縣', '臺中市', '臺東縣', '桃園市', 
        '南投縣', '高雄市', '金門縣', '屏東縣', '基隆市', '澎湖縣', '彰化縣',
        '連江縣'
        ]


Citylist= ttk.Combobox(frame,values=source,font = ('Courier', '18'))
root.option_add('*TCombobox*Listbox.font',('Courier', '18') )
Citylist.current(1)
Citylist.place(relwidth=0.65,relheight = 1)

button = tk.Button(frame,text='Get Weather',font=('Courier',14),command=lambda: get_weather(Citylist.get()))
button.place(relx=0.7,relwidth=0.3,relheight = 1)

#clearb = tk.Button(frame,text='clear',font=('Courier',14),command=clear)
#clearb.place(relx=0.85,relwidth=0.15,relheight = 1)

lowerframe=tk.Frame(root,bg='#80c1ff',bd=10)
lowerframe.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lowerframe,text='Please click Get Weather',font=('Courier',18),anchor='center',justify='left',bg='white')
label.place(relwidth=1,relheight = 1)

root.mainloop()


