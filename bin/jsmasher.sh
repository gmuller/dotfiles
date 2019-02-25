#!/bin/zsh

LOG_DIR=~/Dropbox/logs/mobile_logs
BACKUP_DIR=~/Dropbox/logs/back

for f in `ls $LOG_DIR`
  do
  jrnl `date -r $LOG_DIR/$f +"%m/%d/%Y at %H:%M"`: `cat $LOG_DIR/$f`;
  mv $LOG_DIR/$f $BACKUP_DIR/;
done
