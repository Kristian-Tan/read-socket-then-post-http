# read-socket-then-post-http

## About
Command line utility to connect to a TCP socket as client, then read (using `sock.recv`) the lines, then do `HTTP POST` to specified endpoint

## Usage
```./read-socket-then-post-http.py (socket-host) (socket-port) (socket-buffer-size) (http-endpoint) (http-headers-json)```
- `socket-host` = host of the socket to read from (e.g.: ip address/FQDN, example: `192.168.1.2`)
- `socket-port` = port of the socket to read from (e.g.: socket number, example: `22`)
- `socket-buffer-size` = buffer size for socket read operation (example: `4092`)
- `http-endpoint` = http endpoint to POST the line that was read from socket (example: `https://example.com`)
- `http-headers-json` = additional http headers in JSON format, useful if your endpoint needs authentication (example: `'{"Authorization": "Bearer mytoken"}'`)

example:
```bash
./read-socket-then-post-http.py \
  192.168.1.2 \
  22 \
  4092 \
  https://example.com \
  '{"Authorization": "Bearer mytoken"}' \

```
