# Apache Logs
Our website's logs have been acting strange. We suspect a malicious actor may have uploaded a webshell. Dive into the logs and find evidence of their activity. 
The flag is the IP Address of the user who uploaded the file. E.g. YCEP24{14.31.142.9}

## Summary
- **Author:** Mah Wen Qiang
- **Category:** web
- **Difficulty:** forensics
- **Discord:** kiraishagaming

## Hints
- `Unexpected PUT Requests: Add PUT requests to directories where uploads shouldn't typically occur...` (50 points)

## Files
- [apache.log](dist\apache.log)

## Flags
- `YCEP24{99.102.58.17}` (static)

## Services
| Service | Port | Type |
| ------- | ---- | ---- |
None
