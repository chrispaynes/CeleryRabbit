.PHONY: rabbitConsole start tasks

rabbitConsole:
	python -m webbrowser -t "http://localhost:15672"

start: rabbitConsole
	docker-compose up

tasks:
	docker-compose exec celery bash -c "python3 -m celerie_queue.run_tasks"
