#!/usr/bin/env bash
die() {
    [ "$#" -eq 1 ] && echo "$1" || echo 'Some Error Occured!'
    exit 1
}

usage() {
    cat << EOM
Move solutions between two leetcode-cli accounts managed by lcpp.

OPTIONS
    -f -> Specify username to account to migrate solutions from.
    -n -> Specify number of solutions to migrate.

FLAGS
    -p -> Specify whether to push migrated solutions to github or not.
EOM
}

while getopts "f:n:ph" opt; do case "$opt" in
    'f')
        from="$OPTARG"
    ;;
    'n')
        solcount="$OPTARG"
    ;;
    'p')
        push='true'
    ;;
    'h')
        usage && exit 0
    ;;
    '*')
        usage && exit 1
    ;;
esac done

# Process option variables
[ -z "$from" ] && usage && die "Specify name of account to migrate solcount from."
[ -z "$solcount" ] && solcount=5
[ -z "$push" ] && push='false'

oldroot="$XDG_DATA_HOME/leetcode/$from/code"
newroot="$XDG_DATA_HOME/leetcode/$(lcpp whoami)/code"

# Find the top (lexicographically) N solutions from the "from" account.
migrations=$(git --git-dir="$oldroot/.git" --work-tree="$oldroot" status -s | cut -d ' ' -f 2 | head -n $solcount)

# Check if enough solutions are available to migrate.
realcount="$(printf "$migrations\n" | wc -l)"
[ $realcount -lt $solcount ] && die "$solcount solutions expected, found $realcount."

# Move solutions from old account to new one.
printf "$migrations\n" | xargs -I {} mv "$oldroot/{}" "$newroot"

# Extract problem numbers and extension, then submit the migrated solutions.
printf "Please wait ..."
while IFS=. read pnum pname pext; do
    case "$pext" in
        'c') lang='c' ;;
        'py') lang='python3' ;;
        'cpp') lang='cpp' ;;
        'java') lang='java' ;;
        *) die "Unknown language '$lang' for migration." ;;
    esac

    sed -i "s/^lang = .*$/lang = '$lang'/" "$newroot/../leetcode.toml" && sleep 10
    leetcode exec "$pnum"
done <<< "$migrations"

# Optionally push the newly submitted solutions on github.
[ "$push" = 'true' ] && ./autocommiter.py
