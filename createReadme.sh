#"!/bin/bash
echo "" > README.md
for picture in Picture-Directory/*.jpg; do
  echo "<img src='$picture'>" >> README.md
done
for picture in Picture-Directory/*.png; do
  echo "<img src='$picture'>" >> README.md
done
  
