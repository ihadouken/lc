int finalValueAfterOperations(char ** operations, int operationsSize){
    int i, val;
    val = 0;

    for (i = 0; i < operationsSize; ++i)
        /* For both prefix and postfix operations, increments and decrements can
         * differentiated by just checking the middle char. Ex:- ++i and i++ both
         * have + as middle char. ASCII value for + is 43 and for - its 45. The
         * following code increments (+1) or decrements (-1) accordingly.
         */
        val += 44 - operations[i][1];

    return val;
}
