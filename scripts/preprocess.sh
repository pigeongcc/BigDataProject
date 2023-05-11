#!/bin/bash

# setup a Python virtual environment
sudo rm -rf bd_project_team_9
virtualenv bd_project_team_9
source bd_project_team_9/bin/activate
pip install pandas
pip install pylint
pip install pyspark
pip install streamlit
pip install altair
pip install numpy
pip install ipython

# download dataset files from source (Kaggle)
echo
echo "Downloading 1/3: users_export.csv - Cancelled after EDA query 1 conclusion."
# wget -nc -O data/users_export.csv "https://storage.googleapis.com/kagglesdsdata/datasets/1300195/3341890/users_export.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230502%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230502T135026Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2408cb5d9dbc811cb13df62535091a7d43e554aaa7af74090c9acd52fefe42b24c4582bd98a0d5b50fc2695455cfc9b7aabf4753b562c04c2622cc0d9c85d880422a8d7e25e467724b6b939911b264b17d589c061786027441082baebba3afec2785dd3f42307202de2bdd8545f4a9b3b918912567ffccbcbc7ff6d69ee3fef23a744848e6b6323b33bc2be3c4d04c39e3f3070928c4b36c5d0859527288ccbd5716950eea098de0301dd4a82763c86d6cf5f0722d9d664fd7923174bbef966c1b40b57834be06401e8b4436d89cab36711119acaf78f4702028f1288a9186f2c624b50b2321488a441bf4bcd387cb9a06e0a666d4532742e3c441326eddd175"

echo "Downloading 2/3: ratings_export.csv.zip ..."
wget -nc -O data/ratings_export.csv.zip "https://s439sas.storage.yandex.net/rdisk/0432a3d62d220cfb49d0ba86a8d2e3c08cd8b5167bc1d17297b82ebbc9a2af9e/645d03ff/2XmmQhLjACLa8ObwNQnTIbZmSGJsLJy8CFmYnkrivH1pyG_QP6UzicQy0ZLlbFrPmgkL-iy47Kq8vzHGLUAOVA==?uid=311020858&filename=ratings_export.csv.zip&disposition=attachment&hash=&limit=0&content_type=application%2Fzip&owner_uid=311020858&fsize=137679230&hid=8ac676e9462f5acfe779aba5e34677e7&media_type=compressed&tknv=v2&etag=515ee201d1cc594416be5c8ed6ce29eb&rtoken=9kGmNHnxT7hU&force_default=yes&ycrid=na-706d1c9bbb44dfa79dc87645a8bb2232-downloader17e&ts=5fb6c4e39bdc0&s=3b7e9cb698351d149bc3fd44e3856a81a0dd207b5b1740f0c54f69df1342c4c3&pb=U2FsdGVkX1_FimVkaSLygdrAyYhrsID0knyNNq88iAOGClgxQzzYB4EFv0uznxRqaPL9lK7GFdkzahA8oVEpEjb8uYRcgWFFcjmECm9MQPM"
# extract the zip archive
unzip -n data/ratings_export.csv.zip -d data

echo "Downloading 3/3: movie_data.csv.zip ..."
wget -nc -O data/movie_data.csv.zip "https://s352vla.storage.yandex.net/rdisk/190e2b614d5ed6bde2e71a59db8aa596e85e516f8c49b278d07239cfa6c9e800/645d03f3/2XmmQhLjACLa8ObwNQnTIW9nTslfXqOwNR9dtUm-APtHCzekBEtJYf4W-Q-Epi3q_4dt93i6bIn_tV3MO0Tyqg==?uid=311020858&filename=movie_data.csv.zip&disposition=attachment&hash=&limit=0&content_type=application%2Fzip&owner_uid=311020858&fsize=59193190&hid=3878edd4d4ad6cb963756162c172f4c8&media_type=compressed&tknv=v2&etag=8ad3c6f276eeaa2fa83ca7d3031a0acf&rtoken=wuDpu1jSMgUI&force_default=yes&ycrid=na-1bdbf9186e87accdf5928df7b9bb8a97-downloader17e&ts=5fb6c4d82a2c0&s=b4e1462deddb04e23b950ce346731c2e269722682c08a5a826965e4cd29d0b2b&pb=U2FsdGVkX1_6bkqI_R6ap2kZ6EyEsReF37aQ2tUAWS5AVuttsL0pS-DGyoZmMDRAxIAbGMfCqsM0MrGRDUAr_dtbZNAwDygK0Rra_d3bdL0"
# extract the zip archive
unzip -n data/movie_data.csv.zip -d data

echo

# preprocess the csv files before feeding to PostgreSQL
pwd
python scripts/preprocess/preprocess_csv.py
