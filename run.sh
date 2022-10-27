rm -rf download_data
mkdir -p download_data
docker compose up -d
docker wait automatization_lnma_rct-job-1
docker compose down
