# deep-shrooms-backend

[model-repo](https://github.com/TuomoNieminen/deep-shrooms)  
[frontend](https://github.com/TeemuKoivisto/deep-shrooms-frontend)

Flask-backend for our Keras/Tensorflow model that predicts mushrooms based on pictures.

## API

### POST `/predict`
Params: `.jpg` file as `multipart/form-data`
Returns: JSON-object that has prediction value on its edibility 0 being unedible and 1 edible.
Example:
```
{
  "prediction": 0.658562958240509
}
```

## How to install

1) First install Python >3.5
2) You should have now pip so then install virtualenv: `pip install virtualenv` (or `pip3 install virtualenv` if you have also Python 2 installed eg. Mac OS X)
3) Create virtualenv environment: `virtualenv <name>`
4) Activate that environment: `source ./<name>/bin/activate`
5) Install requirements: `pip install -r requirements.txt`
6) And you're done!

Run the development server on localhost:9000 with `./dev`.

It will automatically refresh on any changes to the source code.