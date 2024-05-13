#!/bin/bash
signals=(SIGUSR2 SIGABRT SIGUSR2 SIGUSR2 SIGHUP) # take this signals from output of other script
for item in "${signals[@]}"; do
    kill -$item 1857 # get the pid and past it here
    sleep 1
done
