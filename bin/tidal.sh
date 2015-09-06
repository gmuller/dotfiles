#!/bin/zsh


jackd -dcoreaudio -dSoundflowerEngine:0 &
~/Dirt/dirt -s ~/Dropbox/audio/Samples/dirt --no-dirty-compressor &
atom ~/Dropbox/Apps/Tidal
