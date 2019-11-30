Schedule recurring backups with rsync and cron

```
Usage: backup_cron.py: [options...] <paths>
	-v, --verbose	Enable debug mode (ENV VAR: BACKUP_DEBUG). -v -v for very verbose.
	-h, --help	Display this info
	-o, --output <path>	The directory to copy paths to. (ENV VAR: BACKUP_OUTPUT_PATH)
	-c, --cron <tab definition>	The cron 'm h dom mon dow' e.g. '0 * * * *'
	-f, --force	Override existing cron job if conflict.
```

Copy $HOME/dev/backup_cron to $HOME/backup every minute
```
coconut-py3-run backup_cron.coco -o ~/backup -c "* * * * *" ~/dev/backup_cron/
```

Changing the schdule to every 30m (--force)
```
coconut-py3-run backup_cron.coco -o ~/backup -c "*/30 * * * *" -f ~/dev/backup_cron/
```

Taking in a list of source directories and files

```
coconut-py3-run backup_cron.coco -o ~/backup -c "*/30 * * * *" -f ~/dev/backup_cron/ ~/dev/inspect_shell.py ~/dev/otp
```

If run without a cron slice definition then it'll only sync now.
