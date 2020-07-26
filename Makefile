install:
	pip3 install opencv-python
	pip3 install numpy
	# pip3 install pickle

clean:
	rm -r __pycache__

run:
	python3 FacialActivity.py

train:
	python3 training_faces.py
