#!/bin/bash

# Setup DB and static files
karrio migrate || exit
karrio collectstatic --noinput 1> /dev/null || exit

# Setup Default super admin
(echo "
from decouple import config
from django.contrib.auth import get_user_model
if not any(get_user_model().objects.all()):
   ADMIN_EMAIL = config('ADMIN_EMAIL')
   ADMIN_PASSWORD = config('ADMIN_PASSWORD')
   get_user_model().objects.create_superuser(ADMIN_EMAIL, ADMIN_PASSWORD)
" | karrio shell) || exit


# Start services
if [[ "$DETACHED_WORKER" == "False" ]];
then
	set -e # turn on bash's job control
	trap 'kill 0' INT

	gunicorn --config gunicorn-cfg.py karrio.server.asgi -k karrio.server.workers.UvicornWorker &
	/bin/bash ./worker.sh &

	wait -n

else
	gunicorn --config gunicorn-cfg.py karrio.server.asgi -k karrio.server.workers.UvicornWorker
fi
