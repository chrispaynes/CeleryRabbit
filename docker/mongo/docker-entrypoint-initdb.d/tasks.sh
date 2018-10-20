#!/bin/bash
set -e

mongo <<EOF
use celerie_queue

db.tasks.drop()
db.createCollection("tasks")

EOF
