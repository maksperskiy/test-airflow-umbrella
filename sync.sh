git submodule update --recursive --remote --init 

while IFS= read -r line; do
    repo=$(echo "$line" | cut -d ' ' -f 1)
    path=$(echo "$line" | cut -d ' ' -f 2)

    mkdir -p $repo
    cp -r $repo-tmp/$path ./$repo/ 
    rm -rf $repo-tmp
done < submodules

if [[ `git status --porcelain` ]]; then
  echo "The code has been changed!"
  git add .
  git commit -m "Code update"
  git push
fi
