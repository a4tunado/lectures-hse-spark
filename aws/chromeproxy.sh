#!/bin/bash

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --user-data-dir="$HOME/chrome-with-proxy" --proxy-server="socks5://localhost:8157"
