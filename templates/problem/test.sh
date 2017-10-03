#!/bin/bash

EXEC=./main
INPUT_NAME=tests/test.in.
OUTPUT_NAME=tests/test.out.
MY_OUT=tests/test.ans.

rm -R $MY_OUT* &>/dev/null
for test_file in $INPUT_NAME*
do
    i=$((${#INPUT_NAME}))
    test_case=${test_file:$i}
    if ! `which time` -o time.out -f "(%es)" $EXEC < $INPUT_NAME$test_case > $MY_OUT$test_case; then
        echo [1m[31mSample test \#$test_case: Runtime Error[0m `cat time.out`
        echo ========================================
        echo Sample Input \#$test_case
        cat $INPUT_NAME$test_case

    else
        if diff --brief --ignore-trailing-space $MY_OUT$test_case $OUTPUT_NAME$test_case; then
            echo [1m[32mSample test \#$test_case: Accepted[0m `cat time.out`

        else
            echo [1m[31mSample test \#$test_case: Wrong Answer[0m `cat time.out`
            echo ========================================
            echo Sample Input \#$test_case
            cat $INPUT_NAME$test_case
            echo ========================================
            echo Sample Output \#$test_case
            cat $OUTPUT_NAME$test_case
            echo ========================================
            echo My Output \#$test_case
            cat $MY_OUT$test_case
            echo ========================================
        fi
    fi
done

rm time.out &>/dev/null
