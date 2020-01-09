# Screen-OCR

## Setup 

Follow instructions here:  https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/ 

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

pipenv install all the stuff.

## Training to read lic plates
https://stackoverflow.com/questions/55349307/how-to-tune-tesseract-for-identifying-number-plate-of-a-car-more-accurately

Data generation:
pip install trdg

## Grouping Text Text Localization

[ICDAR2013 HNLA2013](https://www.primaresearch.org/www/assets/papers/ICDAR2013_Antonacopoulos_HNLA2013.pdf) Describes several methods.  Need to find papers on invidual methods.
 
 This looks better: https://datascience.stackexchange.com/questions/47302/how-can-i-detect-blocks-of-text-from-scanned-document-images

WIP https://github.com/mvoelk/ssd_detectors

Object detection 2 stage R-CNN vs 1 stage    https://arxiv.org/pdf/1708.02002.pdf   (1)


Training YOLOv3  https://www.learnopencv.com/training-yolov3-deep-learning-based-custom-object-detector/ .
This page contains formats for the training data.

## EAST Model

Lots of tutorials, but most of them forget to mention where to get the model data!

https://raw.githubusercontent.com/oyyd/frozen_east_text_detection.pb/master/frozen_east_text_detection.pb

## hsv

https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/

this might help the text localization problem:
https://stackoverflow.com/questions/24385714/detect-text-region-in-image-using-opencv


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
