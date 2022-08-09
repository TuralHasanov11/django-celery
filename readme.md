```

```
Run but hold (not execute): celery -A proj worker  -l info --pool=solo
Run and execute: celery -A proj worker  -l info -P gevent
```