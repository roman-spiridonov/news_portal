Sandbox news portal project based on Mail.ru course "Web Applications".

Prerequisites: 
* Create new python environment using `requirements.txt` or `environment.yml`.
	* For Anaconda, use:
	`
	conda create -n news_portal -f environment.yml
	`
	* For pip, use:
	`
	pip install -r requirements.txt
	`


* Collect static files

To start locally:
* Download and run centrifugo server: `centrifugo --config=config-cent.json -p 8003`
* Launch django `python manage.py runserver 8000`