#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
import webbrowser
import requests
# code by ruks
screen_helper = """
Screen:    
    BoxLayout:
        MDBottomAppBar:    
            MDToolbar:
                title: 'RUKS'
                icon: 'language-python'
                type: 'bottom'                
                on_action_button: app.wbn()
                MDIconButton:
                	icon: "youtube"
                	pos:5,1180
                	type: 'bottom'
                	on_release: app.youtube()	        
	            MDIconButton:
	            	icon: "telegram"
	            	pos:0,1180
	            	type: 'bottom'
	            	on_release: app.wbn()                       
"""
# code by ruks
username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"    
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:250
"""
# code by ruks
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ='Light'
        self.theme_cls.primary_palette = "Purple"
        screen = Screen()
        # code by ruks
        self.username = Builder.load_string(username_input)
        K1 = Builder.load_string(screen_helper)        
        button = MDRectangleFlatButton(text='Check up',          pos_hint={'center_x': 0.5, 'center_y': 0.5},on_release=self.show_data)                                       
        screen.add_widget(self.username)
        screen.add_widget(button)
        # code by ruks
        screen.add_widget(K1)        
        return screen
    def show_data(self ,obj):
        if self.username.text is not "":
            da = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7','content-length': '61','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/emailsignup/','sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36','x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M','x-instagram-ajax': '72bda6b1d047','x-requested-with': 'XMLHttpRequest'},data={'email' : 'a@gmail.com','username': f'{self.username.text}','first_name': 'AA','opt_into_one_tap': 'false'}).text
            if ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in  da:
            	user_error=(' Available :'+self.username.text)
            else:
            	# code by ruks
            	user_error=(' not available :'+self.username.text)
                 
        else:
            user_error = "Please enter a username"
        self.dialog = MDDialog(title='Username check',
                               text=user_error, size_hint=(0.8, 1),                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)
                                        ]
                               )
        self.dialog.open()
    def close_dialog(self, obj):
    	self.dialog.dismiss()
    def wbn(self):
    	# code by ruks
    	webbrowser.open('https://t.me/DIBIBl')
    def youtube(self):
    	webbrowser.open('https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA')		
DemoApp().run()
