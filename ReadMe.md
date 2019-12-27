# Runway Assignment

## Setup 

Follow instructions here:  https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/ 

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

pipenv install all the stuff.

## Training to read lic plates
https://stackoverflow.com/questions/55349307/how-to-tune-tesseract-for-identifying-number-plate-of-a-car-more-accurately

Data generation:
pip install trdg

## Grouping Text

[ICDAR2013 HNLA2013](https://www.primaresearch.org/www/assets/papers/ICDAR2013_Antonacopoulos_HNLA2013.pdf) Describes several methods.  Need to find papers on invidual methods.
 
 This looks better: https://datascience.stackexchange.com/questions/47302/how-can-i-detect-blocks-of-text-from-scanned-document-images


## Trouble

### pip install pipenv

error:
```
 pip install pipenv
Traceback (most recent call last):
  File "/usr/bin/pip3", line 9, in <module>
    from pip import main
ImportError: cannot import name 'main'
```

solution:
```
export PATH="${HOME}/.local/bin:$PATH"
```
