# automatization_lnma_rct

## Instructions

Prerequisites:
- Docker >= 20.10

Steps to run:

1. On the same folder clone the next repos:
- https://github.com/jadm333/robotsearch
- https://github.com/covid19lnma/automatization_lnma_rct

2. Go to automatization_lnma_rct an create the next `.env` file and fill the fields:

Env file example:
```env
SENDER_ADDRESS=<>
RECEIVER_ADDRESS=<>
GH_TOKEN=<>
START_DATE=20221014
END_DATE=20221021
```

3. Run the following comand on terminal inside the automatization_lnma_rct repo:
```sh
bash run.sh
```

Opt. Step for Windows system:
1. Empty if necessary and create `download_data` folder inside `automatization_lnma_rct`
2. Run on terminal inside `automatization_lnma_rct` folder:
```sh
docker compose up -d
# Wait to finish
docker wait automatization_lnma_rct-job-1
# Wait to finish
docker compose down
```

4. Finally the download and process files will be inside `download_data`
