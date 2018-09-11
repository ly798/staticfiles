#!/usr/bin/env bash
set -e

ENGINE="mysql"
VERSION="5.7"

if [ ! -n "$1" ] ;then
    echo "Error! Usage: bash trove_mysql_init.sh <image_id>";
    exit -1;
fi

IMAGE_ID="$1"

docker exec -it trove_api trove-manage datastore_update ${ENGINE} ''
docker exec -it trove_api trove-manage datastore_version_update ${ENGINE} ${VERSION} ${ENGINE} ${IMAGE_ID} '' 1
docker exec -it trove_api trove-manage db_load_datastore_config_parameters ${ENGINE} ${VERSION} /var/lib/kolla/venv/lib/python2.7/site-packages/trove/templates/{ENGINE}/validation-rules.json