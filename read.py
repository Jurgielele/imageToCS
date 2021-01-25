import pytesseract
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(event.src_path)
        cs = '''
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO; 


namespace img_to_txt
{{
    class Program
    {{
        static void Main(string[] args)
        {{
            {t}
        }}
    }}
}}'''.format(t=text)
        text_file= open(r'ścieżka do pliku .cs', 'w', encoding='UTF-8')
        n = text_file.write(cs)
        text_file.close()

observer = Observer()
event_handler = Handler()
observer.schedule(event_handler, path=r'ścieżka do folderu, gdzie wrzucasz zdjęcia')
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    

observer.join()