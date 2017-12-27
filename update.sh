#!/bin/bash
echo "Downloading latest version..."
mkdir SOFTWARE_UPDATE
cd SOFTWARE_UPDATE
git clone https://github.com/wipsdafox/carputer
cp *.py ../
cp *.json ../
cp *.sh ../
file=./post.sh
if [ -e "$file" ]; then
    echo "Running post-installation script..."
    chmod +x ./post.sh
    ./post.sh
fi
echo "Software updated. Cleaning up and restarting..."
cd ..
rm -rf SOFTWARE_UPDATE
python3 car.py
