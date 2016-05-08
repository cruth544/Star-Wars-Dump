#"!/bin/bash
echo "" > README.md
for picture in *.jpg; do
  echo "![alt text]($picture starwars)" >> README.md
done
