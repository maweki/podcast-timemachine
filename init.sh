virtualenv venv
source venv/bin/activate
pip install uwsgi flask python-dateutil

sudo cp podcast-timemachine.service /etc/systemd/system/podcast-timemachine.service
sudo systemctl daemon-reload
sudo systemctl enable podcast-timemachine.service
sudo systemctl restart podcast-timemachine.service
