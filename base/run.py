#! /usr/bin/env python

from {{ PROJECT }} import app

app.config.from_object('{{ PROJECT_NAME }}.conf.local.settings')
app.run()
