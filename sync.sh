FILE=submodules.cfg
row_number=0
while IFS= read -r line; do
    row_number=$(echo $row_number + 1 | bc)

    repo=$(echo "$line" | cut -d ' ' -f 1)
    branch=$(echo "$line" | cut -d ' ' -f 2)
    name=$(echo "$line" | cut -d ' ' -f 3)
    path=$(echo "$line" | cut -d ' ' -f 4)
    latest_commit_hash=$(echo "$line" | cut -d ' ' -f 5)

    LATEST_COMMIT_HASH=$(git ls-remote "$repo" "$branch" | awk '{print $1}')
    if [ "$LATEST_COMMIT_HASH" = "$latest_commit_hash" ]; then
        echo "$name wasn't changed"
    else
        git clone -b $branch $repo $name-tmp

        mkdir -p modules
        mkdir -p $name
        cp -r $name-tmp/$path ./modules/$name/ 
        rm -rf $name-tmp

        if [ "$latest_commit_hash" = "" ]; then
            new_content=$(sed "${row_number} s/$/ ${LATEST_COMMIT_HASH}/" $FILE)
        else
            new_content=$(sed "${row_number} s/${latest_commit_hash}/${LATEST_COMMIT_HASH}/" $FILE)
        fi
        sed "${row_number} s|${line}|${new_content}|g" "${FILE}" > ${FILE}.tmp

        mv ${FILE}.tmp ${FILE}
        rm ${FILE}.tmp

        echo "$name was updated"
    fi


done < $FILE

if [[ `git status --porcelain` ]]; then
  echo "The code has been changed successfully!"
  git add .
  git commit -m "Code update"
  git push
fi
