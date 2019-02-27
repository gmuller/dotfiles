jrnlimport () {
    echo `stat -f %Sm -t '%d %b %Y at %H:%M: ' $1` `cat $1` | jrnl
}
