#"!/bin/bash
echo "" > README.md
for picture in *.jpg; do
  echo "($picture)" >> README.md
done
