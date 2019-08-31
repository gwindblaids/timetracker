#!/bin/bash

# compile py files from ui
pyuic5 ./grafic/design.ui -o ./src/main_window.py
pyuic5 ./grafic/select_user.ui -o ./src/select_user.py
pyuic5 ./grafic/user_form.ui -o ./src/user_form.py
pyuic5 ./grafic/about_us.ui -o ./src/about_us.py

echo "Build complete"
