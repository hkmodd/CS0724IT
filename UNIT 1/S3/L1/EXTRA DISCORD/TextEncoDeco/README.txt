Per compilare exe

pyinstaller --onefile --noconsole --icon=TextDecoEnco.png --add-data "logo.png;." --add-data "processed_corpus.txt;." TextEncoDeco_CorpusIntegrated.py

pyinstaller --onefile --noconsole --icon=TextDecoEnco.png --add-data "logo.png:." --add-data "processed_corpus.txt:." TextEncoDeco_CorpusIntegrated.py
