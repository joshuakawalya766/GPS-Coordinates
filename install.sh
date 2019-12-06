chmod 755 *
pip install pythonping
pip install gps3
pip install gps &&
python GPS.py>gpsdata.txt && 
chmod 755 *
python sendfiles.py
rm -r gpsdata.txt
