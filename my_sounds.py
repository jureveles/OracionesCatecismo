from kivy.core.audio import SoundLoader 

#Audios for the prayers in Spanish

import GlobalShared

def stop_sounds_reset(self,factor):
    if GlobalShared.p_sound == "Yes":
        GlobalShared.p_sound = "No"
        
        if factor == '01' and self.sound01: self.sound01.stop()
        if factor == '02' and self.sound02: self.sound02.stop()
        if factor == '03' and self.sound03: self.sound03.stop()
        if factor == '04' and self.sound02: self.sound04.stop()
        if factor == '05' and self.sound05: self.sound05.stop()
        if factor == '06' and self.sound06: self.sound06.stop()
        if factor == '07' and self.sound07: self.sound07.stop()
        if factor == '08' and self.sound08: self.sound08.stop()
        
        if factor == '01E' and self.sound01E: self.sound01E.stop()
        if factor == '02E' and self.sound02E: self.sound02E.stop()
        if factor == '03E' and self.sound03E: self.sound03E.stop()
        if factor == '04E' and self.sound02E: self.sound04E.stop()
        if factor == '05E' and self.sound05E: self.sound05E.stop()
        if factor == '06E' and self.sound06E: self.sound06E.stop()
        if factor == '07E' and self.sound07E: self.sound07E.stop()
        if factor == '08E' and self.sound08E: self.sound08E.stop()
        
def on_button_release(self,factor):
        if factor == '01':
            self.get_screen('screen_one').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '01s':
            self.get_screen('screen_one').ids.my_image_stop.source = '3D_STOP_01.png'
            
        elif factor == '02':
            self.get_screen('screen_two').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '02s':
            self.get_screen('screen_two').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '03':
            self.get_screen('screen_three').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '03s':
            self.get_screen('screen_three').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '04':
            self.get_screen('screen_four').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '04s':
            self.get_screen('screen_four').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '05':
            self.get_screen('screen_five').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '05s':
            self.get_screen('screen_five').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '06':
            self.get_screen('screen_six').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '06s':
            self.get_screen('screen_six').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '07':
            self.get_screen('screen_seven').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '07s':
            self.get_screen('screen_seven').ids.my_image_stop.source = '3D_STOP_01.png'
    
        elif factor == '08':
            self.get_screen('screen_eight').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '08s':
            self.get_screen('screen_eight').ids.my_image_stop.source = '3D_STOP_01.png'

 
        elif factor == '01E':
            self.get_screen('screen_oneE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '01Es':
            self.get_screen('screen_oneE').ids.my_image_stop.source = '3D_STOP_01.png'
            
        elif factor == '02E':
            self.get_screen('screen_twoE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '02Es':
            self.get_screen('screen_twoE').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '03E':
            self.get_screen('screen_threeE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '03Es':
            self.get_screen('screen_threeE').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '04E':
            self.get_screen('screen_fourE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '04Es':
            self.get_screen('screen_fourE').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '05E':
            self.get_screen('screen_fiveE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '05Es':
            self.get_screen('screen_fiveE').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '06E':
            self.get_screen('screen_sixE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '06Es':
            self.get_screen('screen_sixE').ids.my_image_stop.source = '3D_STOP_01.png'

        elif factor == '07E':
            self.get_screen('screen_sevenE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '07Es':
            self.get_screen('screen_sevenE').ids.my_image_stop.source = '3D_STOP_01.png'
    
        elif factor == '08E':
            self.get_screen('screen_eightE').ids.my_image_play.source = '3D_PLAY_01.png'
        elif factor == '08Es':
            self.get_screen('screen_eightE').ids.my_image_stop.source = '3D_STOP_01.png'
            

def on_button_play(self,factor):
        if GlobalShared.p_sound == "No":
            GlobalShared.p_sound = "Yes"
           
            if factor == '01':
                self.sound01 = SoundLoader.load('audios/01_sound.mp3')
                self.get_screen('screen_one').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound01.play()
                
            elif factor == '02':
                self.sound02 = SoundLoader.load('audios/02_sound.mp3')
                self.get_screen('screen_two').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound02.play()
            
            elif factor == '03':
                self.sound03 = SoundLoader.load('audios/03_sound.mp3')
                self.get_screen('screen_three').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound03.play()
                
            elif factor == '04':
                self.sound04 = SoundLoader.load('audios/04_sound.mp3')
                self.get_screen('screen_four').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound04.play()
                
            elif factor == '05':
                self.sound05 = SoundLoader.load('audios/05_sound.mp3')
                self.get_screen('screen_five').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound05.play()
            
            elif factor == '06':
                self.sound06 = SoundLoader.load('audios/06_sound.mp3')
                self.get_screen('screen_six').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound06.play()
                
            elif factor == '07':
                self.sound07 = SoundLoader.load('audios/07_sound.mp3')
                self.get_screen('screen_seven').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound07.play()
                
            elif factor == '08':
                self.sound08 = SoundLoader.load('audios/08_sound.mp3')
                self.get_screen('screen_eight').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound08.play()
                
            elif factor == '01E':
                self.sound01E = SoundLoader.load('audios/01E_sound.mp3')
                self.get_screen('screen_oneE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound01E.play()
                
            elif factor == '02E':
                self.sound02E = SoundLoader.load('audios/02E_sound.mp3')
                self.get_screen('screen_twoE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound02E.play()
            
            elif factor == '03E':
                self.sound03E = SoundLoader.load('audios/03E_sound.mp3')
                self.get_screen('screen_threeE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound03E.play()
                
            elif factor == '04E':
                self.sound04E = SoundLoader.load('audios/04E_sound.mp3')
                self.get_screen('screen_fourE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound04E.play()
                
            elif factor == '05E':
                self.sound05E = SoundLoader.load('audios/05E_sound.mp3')
                self.get_screen('screen_fiveE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound05E.play()
            
            elif factor == '06E':
                self.sound06E = SoundLoader.load('audios/06E_sound.mp3')
                self.get_screen('screen_sixE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound06E.play()
                
            elif factor == '07E':
                self.sound07E = SoundLoader.load('audios/07E_sound.mp3')
                self.get_screen('screen_sevenE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound07E.play()
                
            elif factor == '08E':
                self.sound08E = SoundLoader.load('audios/08E_sound.mp3')
                self.get_screen('screen_eightE').ids.my_image_play.source = '3D_PLAY_02.png'
                self.sound08E.play()
                

def on_button_stop(self,factor):
    if GlobalShared.p_sound == "Yes":
        GlobalShared.p_sound = "No"
        if factor == '01' and self.sound01:
            self.get_screen('screen_one').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound01.stop()
                
        elif factor == '02' and self.sound02:
            self.get_screen('screen_two').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound02.stop()
                
        elif factor == '03' and self.sound03:
            self.get_screen('screen_three').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound03.stop()
                
        elif factor == '04' and self.sound04:
            self.get_screen('screen_four').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound04.stop()
                
        elif factor == '05' and self.sound05:
            self.get_screen('screen_five').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound05.stop()
                
        elif factor == '06' and self.sound06:
            self.get_screen('screen_six').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound06.stop()
                
        elif factor == '07' and self.sound07:
            self.get_screen('screen_seven').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound07.stop()
                
        elif factor == '08' and self.sound08:
            self.get_screen('screen_eight').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound08.stop()
                
        elif factor == '01E' and self.sound01E:
            self.get_screen('screen_oneE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound01E.stop()
                
        elif factor == '02E' and self.sound02E:
            self.get_screen('screen_twoE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound02E.stop()
                
        elif factor == '03E' and self.sound03E:
            self.get_screen('screen_threeE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound03E.stop()
                
        elif factor == '04E' and self.sound04E:
            self.get_screen('screen_fourE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound04E.stop()
                
        elif factor == '05E' and self.sound05E:
            self.get_screen('screen_fiveE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound05E.stop()
                
        elif factor == '06E' and self.sound06E:
            self.get_screen('screen_sixE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound06E.stop()
                
        elif factor == '07E' and self.sound07E:
            self.get_screen('screen_sevenE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound07E.stop()
                
        elif factor == '08E' and self.sound08E:
            self.get_screen('screen_eightE').ids.my_image_stop.source = '3D_STOP_02.png'
            self.sound08E.stop()
                
                
        