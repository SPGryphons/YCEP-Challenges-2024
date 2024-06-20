# YCEP 2024 Challenge Submissions

This repository contains the challenges for YCEP 2024

## Navigation

Each challenge in the [challenges](./challenges/) directory is categorised by its respective category, with the following subdirectories:

- `service` - Contains the service files for the challenge.
- `solution` Contains the solution files for the challenge, usually has a writeup called `README.md` or `writeup.md`.
- `dist` - Contains the files to be given to the participants.

## Deployment

Hosted challnegs can be deployed via the provided [docker-compose.yml](./docker-compose.yml) file, hosted challenges are split into three docker profiles: `wave1`, `wave2` and `wave3`.

### Deploying a Specific Challenge

To deploy a challenge, run the following command:
```
docker compose up -d [service_name]
```

### Deploying a Wave

To deploy a wave, run the following command:
```
docker compose --profile wave[1/2/3] up -d
```

### Deploying ALL Challenges

You can deploy multiple or all profiles at once by running the following command:
```
docker compose --profile wave1 --profile wave2 --profile wave3 up -d
```