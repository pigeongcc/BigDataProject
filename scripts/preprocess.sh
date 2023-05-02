#!/bin/bash

# download dataset files from source (Kaggle)
echo "Downloading 1/3: users_export.csv ..."
wget -nc -O data/users_export.csv "https://storage.googleapis.com/kagglesdsdata/datasets/1300195/3341890/users_export.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230502%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230502T135026Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2408cb5d9dbc811cb13df62535091a7d43e554aaa7af74090c9acd52fefe42b24c4582bd98a0d5b50fc2695455cfc9b7aabf4753b562c04c2622cc0d9c85d880422a8d7e25e467724b6b939911b264b17d589c061786027441082baebba3afec2785dd3f42307202de2bdd8545f4a9b3b918912567ffccbcbc7ff6d69ee3fef23a744848e6b6323b33bc2be3c4d04c39e3f3070928c4b36c5d0859527288ccbd5716950eea098de0301dd4a82763c86d6cf5f0722d9d664fd7923174bbef966c1b40b57834be06401e8b4436d89cab36711119acaf78f4702028f1288a9186f2c624b50b2321488a441bf4bcd387cb9a06e0a666d4532742e3c441326eddd175"

echo "Downloading 2/3: ratings_export.csv.zip ..."
wget -nc -O data/ratings_export.csv.zip "https://storage.googleapis.com/kaggle-data-sets/1300195/3341890/compressed/ratings_export.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230502%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230502T135024Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5271ec6012563506952e6ca21802c81f9a1b9c78c9def3de1c7b7aeedab77c41191e2386f68e79a196a90a1bd277f8f2d50773e8c7a92443572b93cabc24d3e1432807e3f92706ebfc8606d9e1eef4de23ad0dcd24b84f0c592d2ca4f2e72aedda51fb940ef102b5a2ea2f9c47030bf6419dfc8578972421da99fa54d07db67772b788ae6c643a83e54b49e1ae9503542a6c125394620789c32e36ff070c2301c0cc17ffad86f161783aad8c822201c6ae2745ef7a1d308bf638646ae121062057aa8c79b0416765d4c3c4f81686f3afbe2f86e4380ef8ecb9c3c35c00fb45bbbf723a19ef77c20e958ba4380033a30e50c789dfb0a5ccabd0558fd42aaf39fb"

echo "Downloading 3/3: movie_data.csv.zip ..."
wget -nc -O data/movie_data.csv.zip "https://storage.googleapis.com/kaggle-data-sets/1300195/3341890/compressed/movie_data.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230502%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230502T135019Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6d871bca06e1f1cd67438e402c7c0f3eb3b8fd14e29fcde35d3dfca900d38120c778ca02365d42cac33f84cea433ab4c6ef4f506c5d70a46d4eb7e5c2463b028dff159ed40038cda5c815eb00489309c72ce0cf4e2655744352e973a58158c639c88e0aef13c19043141edae8e4da122e8612e6f22bae4e229f2901651b8dc0818abb60ad257178326eba2031a38944941644214cf1ca4b2afcd4b736851c1c18833e81f0822fa2b2f988a74c1ffd7fe740cadaac8b0c3ff329cd8ac7d32ec879c433ca41d7d421b6d9a4aff489686f28b0c643b12b75a95bfbb04ea281cb10194b5a8783fbe73d20c047fc71036c46604bf0c86e3811b3c1f57b4d491df23f6"