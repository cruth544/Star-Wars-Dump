#"!/bin/bash
echo "" > README.md
for picture in *.jpg; do
  echo "<img src='$picture'>" >> README.md
done
