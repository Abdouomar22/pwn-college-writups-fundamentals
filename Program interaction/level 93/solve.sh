#!/bin/bash
    rm /tmp/fifo

    rm /tmp/fifo1

    mkfifo /tmp/fifo

    mkfifo /tmp/fifo1


    /challenge/embryoio_level93* < /tmp/fifo > /tmp/fifo1 &

    cat  /tmp/fifo1 &
    
    cat > /tmp/fifo
